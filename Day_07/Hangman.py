import random
import subprocess

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
print(logo)

#generate a random word
word_file = "/usr/share/dict/words"
words = open(word_file).read().splitlines()
hangman = random.choice(words).lower()


#generate as many blanks as letters in word
hint = ["_" for letter in hangman]

#error counter
error = 6

#end of game trigger
end_of_game = False

#stages of your hangman
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

while not end_of_game:
    print(stages[error])
    print("".join(hint))
    #print(f"Psst, the solution is {hangman}.")




    #ask user to guess a letter
    guess = input("Guess a letter: ").lower()

    #did user guess the word
    if guess == hangman:
        print("You win!")
        end_of_game = True


    #is guess letter in the word
    if guess == hangman or "".join(hint) == hangman:
        print("You win!")
        end_of_game = True
    elif guess in hangman:
        for i in range(len(hangman)):
            if hangman[i] == guess:
                hint[i] = guess
    else:
        error -= 1
    subprocess.run('clear')
    if error == 0:
        print(stages[error])
        print("You're dead!")
        print(f"The word was {hangman}!")
        end_of_game = True