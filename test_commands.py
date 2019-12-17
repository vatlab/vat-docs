import re
import os
import shutil
import subprocess


def get_markdown_files(folder, filetype):
    findFiles = []
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(filetype):
                findFiles.append(os.path.join(root, file))
    return findFiles


def buildAndClean(func):
    def inner(*args, **kwargs):
        print("before test.")
        try:
            os.mkdir("test_doc")
        except FileExistsError:
            shutil.rmtree("test_doc")
            os.mkdir("test_doc")
        os.chdir("./test_doc/")
        returned_value = func(*args, **kwargs)
        print("after test.")
        os.chdir("../")
        # shutil.rmtree("test_doc")
        return returned_value
    return inner


class MarkDownFile:

    def __init__(self, filePath):
        self.filePath = filePath
        self.commands = []
        self.outputCheck = {}
        self.get_commands()

    def get_commands(self):
        print(self.filePath)
        with open(self.filePath) as openFile:
            output = []
            commandFlag = False
            lastCommand = ""
            for line in openFile:
                if re.search(r"^\s*%", line):
                    lastCommand = line.replace("%", "").strip()
                    self.commands.append(lastCommand)
                    commandFlag = True
                elif re.match(r'[ \t]', line):
                    if commandFlag:
                        output.append(line)
                else:
                    if commandFlag:
                        self.outputCheck[lastCommand] = output
                        output = []
                        commandFlag = False

    @buildAndClean
    def run_commands(self):
        if len(self.commands) > 0:
            exclude = ["-h", "--update_resource"]
            self.commands = filter(lambda s: not any(x in s for x in exclude), self.commands)
            outputFilePath = "test_commands.sh"
            outputFile = open(outputFilePath, "w")
            for command in self.commands:
                outputFile.write("echo \"" + command.replace("\"", "") + "\"\n")
                outputFile.write(command + "\n")
                outputFile.write("echo\n")
            outputFile.close()
            subprocess.call(['chmod', '777', outputFilePath])
            process = subprocess.Popen(["/bin/sh", outputFilePath], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, bufsize=1)
            for line in iter(process.stdout.readline, b''):
                print(line.decode("utf-8").strip())
            process.stdout.close()
            process.wait()

    @buildAndClean
    def update_output(self):
        updateMarkdown_path = "."+self.filePath.replace(".md", "_update.md")
        print(updateMarkdown_path)
        os.environ["STOREMODE"] = "hdf5"
        excludeOutput = ["Calculating phenotype", "WARNING", "100%", "0.0%", "warnings", "UserWarning", "Running", "..........", "/Users/", "Saving to", "Importing genotypes", "Copying samples"]
        excludeCommands = ["vtools init", "vtools admin --load_snapshot", "vtools import V*_hg38.vcf --build hg38", "my_vcf.fmt"]
        outputUpdates = []
        updateMarkdown = open(updateMarkdown_path, "w")
        with open("."+self.filePath) as openFile:
            commandFlag = False
            output = []
            lastCommand = ""
            for line in openFile:
                if re.search(r"^\s*%", line):
                    print("Command line", line.rstrip())
                    updateMarkdown.write(line)
                    lastCommand = line.replace("%", "", 1).strip()
                    if lastCommand == 'export STOREMODE="sqlite"' or lastCommand == 'export STOREMODE="hdf5"':
                        print(lastCommand.split("=")[1].replace("\"", ""))
                        os.environ["STOREMODE"] = lastCommand.split("=")[1].replace("\"", "")
                    if lastCommand == 'vtools admin --update_resource':
                        continue
                    commandFlag = True
                    outputFilePath = "test_commands.sh"
                    outputFile = open(outputFilePath, "w")
                    outputFile.write(lastCommand + "\n")
                    outputFile.close()
                    subprocess.call(['chmod', '777', outputFilePath])
                    process = subprocess.Popen(["/bin/sh", outputFilePath], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, bufsize=1)
                    for outputLine in iter(process.stdout.readline, b''):
                        outputLine = outputLine.decode("utf-8")
                        outputLine = "\t"+outputLine
                        if "ERROR" in outputLine:
                            print(outputLine)
                        if not any(x in outputLine for x in excludeOutput) and not any(x in line for x in excludeCommands):
                            if re.match(r'[ \t]', outputLine):
                                pass
                            else:
                                outputLine = "\t"+outputLine
                                # print(outputLine.rstrip())
                            updateMarkdown.write(outputLine)
                            outputUpdates.append("\t"+outputLine.strip()+"\n")
                elif re.match(r'[ \t]', line):
                    if commandFlag:
                        output.append("\t"+line.strip()+"\n")
                else:
                    if commandFlag:
                        updatedOutput = "".join(outputUpdates)
                        originalOutput = "".join(output)
                        if "-h" not in lastCommand:
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
                                updateMarkdown.write(originalOutput)
                        else:
                            updateMarkdown.write(line)
                        outputUpdates = []
                        output = []
                        commandFlag = False
                    else:
                        updateMarkdown.write(line)
        updateMarkdown.close()

# markDownFiles = get_markdown_files("./content/Documentation/vtools_commands", ".md")
# for markDownFile in markDownFiles:
#     file = MarkDownFile(markDownFile)
#     print(markDownFile)
#     # file.get_commands()
#     # for key, value in file.outputCheck.items():
#     #     print(key)
#     #     print("".join(value))
#     file.run_commands()


markDownFile = "./content/Documentation/vtools_commands/admin.md"
file = MarkDownFile(markDownFile)
file.update_output()
