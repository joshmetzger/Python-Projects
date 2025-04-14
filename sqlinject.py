import sqlite3

##firstName = input("Enter yuour first name: ")
##lastName = input("Enter yuour last name: ")
##age = int(input("Enter yuour age: "))
##personData = (firstName, lastName, age)
##
##
##with sqlite3.connect('test_database.db') as connection:
##    c = connection.cursor()
##    c.execute("INSERT INTO People VALUES(?,?,?)", personData)


peopleValues = (('Ron','Obvious',42),('Luigi','Vercotti',43),('Arthur','Belling',28))

with sqlite3.connect('test_database.db') as connection:
    c = connection.cursor()
    c.execute("DROP TABLE IF EXISTS People")
    c.execute("CREATE TABLE People(firstName TEXT, lastName TEXT, Age INT)")
    c.executemany("INSERT INTO People VALUES(?,?,?)", peopleValues)

##    c.execute("SELECT firstName, lastName FROM People WHERE Age > 30")
##    for row in c.fetchall():
##        print(row)


    c.execute("SELECT firstName, lastName FROM People WHERE Age > 30")
    while True:
        row = c.fetchone()
        if row is None:
            break
        print(row)
