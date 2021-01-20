import os


def mkScript(folderPath, targetFileExtension=".flac"):

    filePaths = getFilePaths(folderPath)

    os.chdir("C:\\ffmpeg\\bin")
    staged_script = open("aac_encode.bat", "w")
    for file in filePaths:
        staged_script.write(writeLine(file, targetFileExtension))

    staged_script.close()

    return


def getFilePaths(path):
    os.chdir(path)

    filePaths = []
    fileNames = os.listdir()
    for file in fileNames:
        filePaths.append(os.path.abspath(file))

    if 'aac' not in os.listdir():
        os.mkdir(".\\aac")

    return filePaths


def writeLine(file, targetFileExtension=".flac"):
    outputFilePath = file.replace(targetFileExtension, ".m4a")

    line = 'ffmpeg -i "{i}" -c:a aac -b:a 256k "{o}"\n'.format(
        i=file, o=outputFilePath)

    return line
