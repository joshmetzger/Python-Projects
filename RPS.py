def start():
    print('This is my RPS game')
    Player_one = 'Josh'
    Player_two = 'Steve'

    def choices(Player_one_choice, Player_two_choice):
        if Player_one_choice == 'rock' and Player_two_choice == 'paper':
            return('paper covers rock, ' + Player_two + ' wins!')
        elif Player_one_choice == 'paper' and Player_two_choice == 'rock':
            return('paper covers rock, ' + Player_one + ' wins!')
        elif Player_one_choice == 'scissors' and Player_two_choice == 'paper':
            return('scissors cuts paper, ' + Player_one + ' wins!')
        elif Player_one_choice == 'rock' and Player_two_choice == 'scissors':
            return('rock smashes scissors, ' + Player_one + ' wins!')
        elif Player_one_choice == 'paper' and Player_two_choice == 'scissors':
            return('scissors cuts paper, ' + Player_two + ' wins!')
        elif Player_one_choice == 'scissors' and Player_two_choice == 'rock':
            return('rock smashes scissors, ' + Player_two + ' wins!')
        elif Player_one_choice == Player_two_choice:
            return('Jack and Erick tied!')
        else:
            return('please type rock, paper or scissors')

    player_one_choose = input('Does ' + Player_one + ' choose rock, paper, or scissors? ').lower()
    player_two_choose = input('Does ' + Player_two + ' choose rock, paper, or scissors? ').lower()

    print(choices(player_one_choose, player_two_choose))

    def Play_Again():
        Again = input("Would you like to play again? ").lower()
        if Again == 'No'.lower():
            quit()
        if Again == 'Yes'.lower():
            start()
        else:
            print('Please enter Yes or No.')
            Play_Again()
    Play_Again()
start()
