def write():
    filename = input('Enter file name')
    file = open(filename, 'w')
    file.write('I like cats')

def read():
    filename = input('Enter file name to read')
    file = open(filename, 'r')
    lines = file.read()
    print(lines)

def append():
    filename = input('Enter file to append')
    file = open(filename, 'a')
    file.write('I like dogs \n')
    file.close()

write()
read()
append()