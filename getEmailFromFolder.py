#Note - Make sure to change the name of the path
import re
import string
from os import listdir
from os.path import isfile, join


def lastCapital(inputStr):
    indexUpper = ""
    for i in range(len(inputStr)):
        if inputStr[i] in string.ascii_uppercase:
            indexUpper = i
    return indexUpper


folderName = "sourceCodeDirectoryOct2013"
path = "C:\\Users\\Daniel\\Documents\\GitHub\\MNSU_EmailExtract\\" + folderName
onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
outputFile = open("xcodeList2.csv", "w")
biggest = 0
for fileName in onlyfiles:
    textFile = open(folderName + "\\" + fileName, "r")
    fullText = textFile.read().split()
    textFile.close()
    fullTextStr = " ".join(fullText)
    for word in fullText:
        if "@" in word:
            data = {}
            start = fullTextStr.lower().index("name:")
            end = fullTextStr.index(word) + len(word) - 1
            infoSection = fullTextStr[start:end]
            if "www" in infoSection:
                infoSection = infoSection[:infoSection.index("www")]
            infoSection = re.sub(r"<.*?>", "", infoSection)
            dataList = infoSection.split(":")

            for i in range(1, len(dataList) - 1):
                dataInfo = dataList[i]
                dataInfoPrevious = dataList[i - 1]

                lastC = lastCapital(dataInfo)
                lastP = lastCapital(dataInfoPrevious)

                value = dataInfo[:lastC].strip()
                key = dataInfoPrevious[lastP:]

                data[key] = value
            else:  # for last element
                dataInfo = dataList[-1]
                dataInfoPrevious = dataList[-2]

                lastP = lastCapital(dataInfoPrevious)

                value = dataInfo.strip()
                key = dataInfoPrevious[lastP:]

                data[key] = value

            if data.get("Type") == "student" and (
                "Technology" in str(data.get("Department"))
                    or "Information" in str(data.get("Department"))
                    or "Engineering" in str(data.get("Department"))):
                outline = ""
                outline += str(data.get("Name")) + ","
                outline += str(data.get("Type")) + ","
                outline += str(data.get("Title")) + ","
                outline += str(data.get("Department")) + ","
                outline += str(data.get("Address")) + ","
                outline += str(data.get("Phone")) + ","
                outline += str(data.get("Email")) + ","
                outputFile.write(outline + "\n")
outputFile.close()
