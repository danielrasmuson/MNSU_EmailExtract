import codecs
import os  
import re
for fn in os.listdir('./sourceCodeDirectory'):
    # os.rename(fn, fn[1:]) #rename
    # os.remove(filePath) #delete
    # os.system('command to execute')
    # textFile = open(fn,"r", 'utf-8')
    # with codecs.open(fn,'r',encoding='utf8') as f:
# 
        # text = f.read()
        # text = unicode(text, errors='replace')
        # print text
    textFile = open(fn,"r")

    text = textFile.read()
    print dir(text)
    # print text.encode('utf-8')
    # print text.decode().encode('uft-8')
    print 
    # for char in text:
        # print char

    # cleanText = re.sub(r'[^\\x00-\\x7f]', ' ', text) #replace
    # print cleanText
    # s = s.replaceAll("[^\\x00-\\x7f]", "");
    # text
    # s = s.replaceAll("[^\\x00-\\x7f]", "");
    # print(dir(textFile))
    # print(textFile.encoding)
    # print(textFile.readline())
    # print(textFile.readline())
    # print(textFile.readline())
    # fullText = textFile.read()
    textFile.close()
    
    # process Unicode text
    # with codecs.open(fn,'w',encoding='utf8') as f:
        # f.write(text)
    # fullText = textFile.read()
    # textFile.close()
    # print(fullText)
    break
