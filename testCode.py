mySentence = 'loves the color'

color_list = ['red', 'blue', 'green', 'pink', 'black', 'teal']

def color_function(name):
    lst = []
    for i in color_list:
        msg = "{0} {1} {2}".format(name, mySentence, i)
        lst.append(msg)
    return lst

def get_name():
    go = True
    while go:
        name = input('What is your name? ')
        if name == '':
            print("please enter your name!")
        elif name == 'Sally':
            print("Sally, you may not move ahead")
        else:
            go = False
    lst = color_function(name)
    for i in lst:
        print(i)

get_name()


def tell_hoe_toSuggDigg(name):
    print("{0}, go aheed and sigg this digg".format(name))


tell_hoe_toSuggDigg('LeghAnne')
