import sqlite3

fileList = ('information.docx', 'Hello.txt', 'myImage.png', 'myMovie.mpg', \
            'World.txt', 'data.pdf', 'myPhoto.jpg')


##iterate fileList, find files with .txt
##if match, add file name to txtFiles list

txtFiles = ()

def searchTxt():
    global txtFiles
    for file in fileList:
        if file.endswith('.txt'):
            txtFiles += (file,)

searchTxt()



conn = sqlite3.connect('py_txt.db')

##create db/table
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_py_txt1( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        file_name TEXT \
        )" )
    conn.commit()
conn.close()


conn = sqlite3.connect('py_txt.db')

##insert data from dynamically generate tuple data
with conn:
    cur = conn.cursor()
    ##    dynamically insert data
    for file in txtFiles:
        cur.execute("INSERT INTO tbl_py_txt1(file_name) VALUES (?)", \
            [file])
##            ('{}'.format(file)))
    conn.commit()
conn.close()
            












if __name__ == "__main__":
    searchTxt()
