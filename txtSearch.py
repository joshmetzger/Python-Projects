import os

# view idrectory contents:
directory = '/Users/joshmetzger/Documents/Python Files/pyFiles_txtSearch'

viewDir = os.listdir(directory)

def printDirContents():
    for file in viewDir:
        fPath = os.path.join(directory, file)

        #if file has .txt extenstion, print to screen
        if file.endswith('.txt'):
            print(fPath)
            print(os.path.getmtime(fPath))





if __name__ == "__main__":
    printDirContents()
