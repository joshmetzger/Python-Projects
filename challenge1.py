import time

num = 3
junt = 'junt'
dec = 12.3
stuff = [4,5,8,90,2]

print(num)
print(num + dec)
print(num * dec)
print(dec / num)
print(dec % num)

if (12/3 == 4) and (7 == 7):
    print('both true')
elif (7+1 == 80) or (7-200 == 4):
    print('one is true')
elif 4 not in stuff:
    print('aww yeah it ain\'t')
else:
    print('nope')

counter = 0
while counter < 4:
    print(str(counter) + 'junt')
    counter = counter + 1

for stu in stuff:
    print(stu)

tuppy = ('robot', 'carrot', 'coffee')
for item in tuppy:
    print(item)


def str_dump():
    user_input = input('guess the magic word: ')
    if user_input == 'please':
        print('yessssss')
    else:
        print('fix my fuccing phone')

str_dump()
