#Note - Make sure to change the name of the path
import codecs
import re
import string
from os import listdir
from os.path import isfile, join

# from chardet import detect

def lastCapital(inputStr):
    indexUpper = ""
    for i in range(len(inputStr)):
        if inputStr[i] in string.ascii_uppercase:
            indexUpper = i
    return indexUpper


folderName = "sourceCodeDirectory"
# path = "\\Users\\danielrasmuson\\Desktop\\MNSU_EmailExtract\\"+folderName
path = "./"+folderName
onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
outputFile = open("xcodeList2.csv", "w")
biggest = 0
for fileName in onlyfiles:
    # textFile = open(folderName + "/" + fileName, "r", )

    # encoding = lambda x: detect(x)['encoding']
    # print encoding(line)
    #open it with utf-8 encoding 
    # f=codecs.open(folderName + "/" + fileName,"r",encoding='utf-8')
    #read the file to unicode string
    # sfile=f.read()

    #check the encoding type
    # print type(file) #it's unicode

    #unicode should be encoded to standard string to display it properly
    # cleanText = sfile.encode('utf-8')
    #check the type of encoded string

    # print type(sfile.encode('utf-8'))
    # text = textFile.read()
    # cleanText = filter(lambda x: x in string.printable, text)
    # f = open(folderName + "/" + fileName, 'w')
    # f.write(foo.encode('utf8'))
    # f.close()
    # f = codecs.open(folderName + "/" + fileName, encoding='utf-8')
    # cleanText = ""
    # for line in f:
    #     cleanText += repr(line)
    #     print(cleanText)

    fullText = cleanText.decode('utf-8').read()

    fullText = cleanText.split()
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
