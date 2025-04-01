import math

days = ['Mon', 'Tues', 'Wed', 'Thurs', 'Fri', 'Sat', 'Sun']

for day in days:
    print(day)

print(days.count('Tues'))

days.sort()
print(days)


lammy = lambda x: (x - 3000) * x + 20
print(lammy(7))

def lilFunc(x,y):
    total = x + x + y - x + x
    print(total)

junt = lilFunc

junt(3,5)


name = "python"

def getName():
    name = "C#"
    print("I am coding with {}".format(name))

getName()
