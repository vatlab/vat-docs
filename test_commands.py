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
                outputFile.write("echo \"" + command.replace("\"","") + "\"\n")
                outputFile.write(command + "\n")
                outputFile.write("echo\n")
            outputFile.close()
            subprocess.call(['chmod', '777', outputFilePath])
            process = subprocess.Popen(["/bin/sh",outputFilePath], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, bufsize=1)
            for line in iter(process.stdout.readline, b''):
                print(line.decode("utf-8").strip())
            process.stdout.close()
            process.wait()



# markDownFiles = get_markdown_files("./content/Documentation/vtools_commands", ".md")
# for markDownFile in markDownFiles:
#     file = MarkDownFile(markDownFile)
#     print(markDownFile)
#     # file.get_commands()
#     # for key, value in file.outputCheck.items():
#     #     print(key)
#     #     print("".join(value))
#     file.run_commands()

markDownFile = "./content/Documentation/vtools_commands/phenotype.md"
file = MarkDownFile(markDownFile)
file.run_commands()



