def start():

    people_dic = {
        'brett':['Male', 'Weight 175'],
        'nancy':['Female', 'Weight 125'],
        'patrick':['Male', 'Weight 195'],
        'briar':['Female', 'Weight 115'],
        'adam':['Male', 'Weight 215']}
    Name = input('type in a name: ').lower()
    print('you typed in the name ' + Name.capitalize())
    
    try:
        persons_data = people_dic[Name]
        print("Name: " + Name.capitalize())
        print("Sex: " + persons_data[0])
        print("Weight: " + persons_data[1])
        more()
    except:
        print("that name, " + Name + ", was not fount in the dictionary")
        more()
        
def more():
    More = input('Would you like to search for another name?')
    if More == 'No':
        quit()
    if More == 'Yes':
        start()
    else:
        print('Please enter yes or no')
        more()
start()
