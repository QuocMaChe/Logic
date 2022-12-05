import os
from handleFile import readFile
from helper import check
from pl_Resolution import plResolution
#
def main():
    # Duong dan den SRC
    dirPath = os.path.dirname(os.path.realpath(__file__))
    # Duong dan /SRC/input folder
    inputFolder = os.path.join(dirPath, "input")
    # Duong dan /SRC/output folder
    outputFolder = os.path.join(dirPath, "output")
    for file in os.listdir(inputFolder):
        # Duong dan den folder input
        inputPath = os.path.join(inputFolder, file)
        # Duong dan den folder output
        outputPath = os.path.join(outputFolder, 'output' + inputPath[-5] + '.txt')
        
        List = readFile(inputPath)
        plResolution(List, outputPath)

if __name__ == "__main__":
    main()