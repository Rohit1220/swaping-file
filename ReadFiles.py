def readWord():
    fileName = input("enter file name : ")
    count = 0
    file = open(fileName, 'r')
    for eachWord in file:
        words = eachWord.split()
        count = count + len(words)
    
    print("number of word in the file are : ", count)

readWord()
