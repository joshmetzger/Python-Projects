##print(dir(str))
##print(help(str))

import os


def writeData():
    data = "\nHello world!"
    with open('testy.py', 'a') as f:
        f.write(data)
        f.close()
    

def openFile():
    with open('testy.py', 'r') as f:
        data = f.read()
        print(data)
        f.close()



if __name__ == "__main__":
    writeData()
    openFile()


