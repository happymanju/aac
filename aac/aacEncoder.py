import os


class BatchScripter:
    def __init__(self, targetFolderPath):
        self.ffmpegPath = "C:\\ffmpeg\\bin"
        self.targetFileExtension = ".flac"
        self.targetFolderPath = targetFolderPath

    def mkScript(self):

        filePaths = getFilePaths(self.targetFolderPath)

        os.chdir(self.ffmpegPath)
        staged_script = open("aac_encode.bat", "w")
        for file in filePaths:
            staged_script.write(writeLine(file))

        staged_script.close()

        return

    def getFilePaths(self, path):
        os.chdir(path)

        filePaths = []
        fileNames = os.listdir()
        for file in fileNames:
            if self.targetFileExtension in file:
                filePaths.append(os.path.abspath(file))

        if 'aac' not in os.listdir():
            os.mkdir(".\\aac")

        return filePaths

    def writeLine(self, file):
        outputFilePath = file.replace(self.targetFileExtension, ".m4a")

        line = 'ffmpeg -i "{i}" -c:a aac -b:a 256k "{o}"\n'.format(
            i=file, o=outputFilePath)

        return line