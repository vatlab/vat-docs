import re
import os
import shutil
import subprocess
import argparse
from datetime import datetime


def get_markdown_files(folder, filetype):
    findFiles = []
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(filetype) and not file.endswith("_update.md"):
                findFiles.append(os.path.join(root, file))
    return findFiles


def buildAndClean(func):
    def inner(*args, **kwargs):
        print("----Start----.")
        try:
            os.mkdir("test_doc")
        except FileExistsError:
            shutil.rmtree("test_doc")
            os.mkdir("test_doc")
        os.chdir("./test_doc/")
        returned_value = func(*args, **kwargs)
        print("----Done-----.")
        os.chdir("../")
        try:
            shutil.rmtree("test_doc")
        except FileNotFoundError:
            os.chdir("../")
            shutil.rmtree("test_doc")
        return returned_value
    return inner


def getDateTime():
    now = datetime.now()
    dt_string = now.strftime("%m/%d/%Y %H:%M:%S")
    return dt_string


class MarkDownFile:

    def __init__(self, markdown_path):
        self.markdown_path = markdown_path
        self.updateMarkdown_path = "."+self.markdown_path.replace(".md", "_update.md")
        self.excludeLineOutput = ["Calculating phenotype", "WARNING", "100%", "0.0%", "warnings", "UserWarning", "ERROR", "Running", "..........", "/Users/", "Saving to", "Importing genotypes", "Copying samples"]
        self.excludeCommandsOutput = ["vtools init", "vtools admin --load_snapshot", "vtools import V*_hg38.vcf --build hg38"]
        self.skipCommands = ["vtools admin --update_resource"]

    def checkCommand(self, command):
        # if command == 'export STOREMODE="sqlite"' or command == 'export STOREMODE="hdf5"':
        if 'export STOREMODE=' in command:
            print(command.split("=")[1].replace("\"", ""))
            os.environ["STOREMODE"] = command.split("=")[1].replace("\"", "")
            return False
        elif command in self.skipCommands:
            return True
        elif re.search(r"^\s*cd", command):
            os.chdir(command.split(" ")[1])
            return True
        elif re.search(r"^\s*mkdir", command):
            os.mkdir(command.split(" ")[1])
            return True
        return False

    def runCommand(self, command):
        outputUpdates = []
        commandFilePath = "test_commands.sh"
        commandFile = open(commandFilePath, "w")
        commandFile.write(command + "\n")
        commandFile.close()
        subprocess.call(['chmod', '777', commandFilePath])
        process = subprocess.Popen(["/bin/sh", commandFilePath], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, bufsize=1)
        for outputLine in iter(process.stdout.readline, b''):
            outputLine = outputLine.decode("utf-8")
            outputLine = "\t"+outputLine
            if "ERROR" in outputLine:
                print(outputLine)
            if not any(x in outputLine for x in self.excludeLineOutput) and not any(x in command for x in self.excludeCommandsOutput):
                if re.match(r'[ \t]', outputLine):
                    pass
                else:
                    outputLine = "\t"+outputLine
                    # print(outputLine.rstrip())
                self.updateMarkdown.write(outputLine)
                outputUpdates.append("\t"+outputLine.strip()+"\n")
        return outputUpdates

    def compareOutput(self, command, outputUpdates, output):
        updatedOutput = "".join(outputUpdates)
        originalOutput = "".join(output)
        if "-h" not in command:
            if (updatedOutput.strip() != originalOutput.strip()):
                print("Update output\n", updatedOutput)
                print("Original output", originalOutput)
            else:
                print("\tUpdated ouput is the same as the original output.")
        if len(updatedOutput) == 0:
            if len(originalOutput) == 0:
                print("\tNo output for this command.")
            else:
                print("\tNo output from current version, use original output in the doc.")
                self.updateMarkdown.write(originalOutput)
        # else:
        #     self.updateMarkdown.write(line)

    @buildAndClean
    def update_output(self):
        os.environ["STOREMODE"] = "hdf5"
        self.updateMarkdown = open(self.updateMarkdown_path, "w")
        with open("."+self.markdown_path) as openFile:
            commandFlag = False
            output = []
            outputUpdates = []
            for line in openFile:
                if re.search(r"^\s*%", line):
                    print("Command line", line.rstrip())
                    self.updateMarkdown.write(line)
                    lastCommand = line.replace("%", "", 1).strip()
                    if self.checkCommand(lastCommand):
                        continue
                    commandFlag = True
                    outputUpdates = self.runCommand(lastCommand)
                elif re.match(r'[ \t]', line):
                    if commandFlag:
                        output.append("\t"+line.strip()+"\n")
                else:
                    if commandFlag:
                        self.compareOutput(lastCommand, outputUpdates, output)
                        outputUpdates = []
                        output = []
                        commandFlag = False
                        if len(line) != 0:
                            self.updateMarkdown.write(line)
                    else:
                        self.updateMarkdown.write(line)
        self.updateMarkdown.write("\n<!-- Last Updated at "+getDateTime()+". -->")
        self.updateMarkdown.close()


helpText = "\
    python test_commands.py -f path_to_markdown_file \n\
    (a *_update.md file will be generated, please review the ouput for accuracy.)\n\
    python test_commands.py -d \n\
    (only markdown files in ./content/Documentation/vtools_commands/ will be updated.)\n"
parser = argparse.ArgumentParser(description=helpText, formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument("-f", "--file", help="file path to the Markdown file to be updated.")
parser.add_argument("-d", "--directory", help="directory path to folder with Markdown files, default to vtools_commands folder", action="store_true")
args = parser.parse_args()
# Stip these files for now
skipFiles = ["show.md"]
if args.file:
    file = MarkDownFile(args.file)
    file.update_output()
elif args.directory:
    markDownFiles = get_markdown_files("./content/Documentation/vtools_commands", ".md")
    for markDownFile in markDownFiles:
        if os.path.basename(markDownFile) not in skipFiles:
            file = MarkDownFile(markDownFile)
            print(markDownFile)
            file.update_output()
