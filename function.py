def countWordsFromFile():
    filename = input('Enter your file name')
    file = open(filename, 'r')
    numberofwords = 0
    for line in file:
        words = line.split()
        numberofwords = numberofwords + len(words)
    print('Number of words in the file is:')
    print(numberofwords)

countWordsFromFile()