import urllib.request


def writeToFile(saveName, sourceCode):
    textFile = open("sourceCodeDirectory\\" + saveName + ".txt", "w")
    textFile.write(sourceCode)
    textFile.close()


def grabSource(inputUrl):
    #get url source code
    with urllib.request.urlopen(inputUrl) as url:
            s = url.read()
    s = str(s)
    return s

for x in range(108, 123):  # represents letters
    print(x,chr(x))
    x = chr(x)
    sourceCode = grabSource("http://www.mnsu.edu/find/people.php?givenname="+x+"&sn=&employeetype=")
    writeToFile(x+"_",sourceCode)
    print(x,sourceCode.count("Displaying the first 20 matches. Please be more specific."))
    if sourceCode.count("Displaying the first 20 matches. Please be more specific.") >= 1:
        for i in range(97,123):
            i = chr(i)
            sourceCode = grabSource("http://www.mnsu.edu/find/people.php?givenname="+x+"&sn="+i+"&employeetype=")
            writeToFile(x+"_"+i,sourceCode)
            # print(x,i,sourceCode.count("Displaying the first 20 matches. Please be more specific."))
            if sourceCode.count("Displaying the first 20 matches. Please be more specific.") >= 1:
                for y in range(97,123):
                    y = chr(y)
                    sourceCode = grabSource("http://www.mnsu.edu/find/people.php?givenname="+x+"&sn="+i+y+"&employeetype=")
                    writeToFile(x+"_"+i+y,sourceCode)
                    # print(x,i+y,sourceCode.count("Displaying the first 20 matches. Please be more specific."))
                    if sourceCode.count("Displaying the first 20 matches. Please be more specific.") >= 1:
                        for z in range(97,123):
                            z = chr(z)
                            sourceCode = grabSource("http://www.mnsu.edu/find/people.php?givenname="+x+z+"&sn="+i+y+"&employeetype=")
                            writeToFile(x+z+"_"+i+y,sourceCode)
                            # print(x+z,i+y,sourceCode.count("Displaying the first 20 matches. Please be more specific."))
                            if sourceCode.count("Displaying the first 20 matches. Please be more specific.") >= 1:
                                for u in range(97,123):
                                    u = chr(u)
                                    sourceCode = grabSource("http://www.mnsu.edu/find/people.php?givenname="+x+z+"&sn="+i+y+u+"&employeetype=")
                                    writeToFile(x+z+"_"+i+y+u,sourceCode)
                                    # print(x+z,i+y+u,sourceCode.count("Displaying the first 20 matches. Please be more specific."))
                                    if sourceCode.count("Displaying the first 20 matches. Please be more specific.") >= 1:
                                        print()
                                        print()
                                        print()
                                        print("PROBLEMS")
                                        print()
                                        print()
                                        print()

