num1 = 12
key = False

if num1 == 12:
    if key:
        print('num1 is equal to 12 and they have the key')
    else:
        print('num1 is 12 and they dont have key')
elif num1 < 12:
    print('num1 is less than 12')
else:
    print('num1 not equal to 12')
    


name1 = 'Josh'
name2 = 'Ivan'
name3 = 'Steve'

if name2 == 'Ivan':
    if len(name1) == 3:
        print('hello Ivan')
    else:
        print('Ivan not here')
elif name3[0] == 'S':
    print('hello Steven')
else:
    print('hello Josh')


print(isinstance(name1, str))
