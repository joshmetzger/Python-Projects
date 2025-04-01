Name = input('Please enter the name of the person who created this game: ')
print('This game was made by the amazing ' + Name + '!')
print('Welcome to my guessing game')
print('In this program, you will try to guess a word that I chose.')
print('good luck')

def start():
    player_name = input('what is the name of the player? ')
    print('greetings, ' + player_name + ', it is time to guess')
    secret_word = 'Ostrich'.lower()
    guesses = ''
    turns_left = 11
    while turns_left > 0:
        wrong_answers = 0
        for letter in secret_word:
            if letter in guesses:
                print(letter)
            else:
                print('_')
                wrong_answers += 1
        if wrong_answers == 0:
            print('YOU WIN! you guessed the word: ' + secret_word + '!!!')
            break
        guess = input('guess a letter here: ').lower()
        guesses += guess

        if guess not in secret_word:
            turns_left -= 1
            print('Oops! this letter is not in the word, try again')
            print('you have ' + str(turns_left) + ' more guess left')
            if turns_left == 0:
                print('GAME OVER')
                
    def play_again():
        again = input('would you like to play again? ').lower()
        if again == 'No'.lower():
            quit()
        if again == 'Yes'.lower():
            start()
        else:
            print('please enter Yes or No.')
            play_again()
    play_again()
start()
