# Code for Hangman game

import random

list_letters = []

class Hangman:

    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        #word = random.choice(self.word_list)
        word = 'great'

        print("The mystery word has " + str(len(word)) + " characters")
        word_guessed = ['_'] * len(word)
        print(word_guessed)


    def check_letter(ll) -> None:
        global num_lives
        if ll in word:
            word_guessed[word.index(ll)] = ll
            print('Nice! ' + ll + ' is in the word!')
            print(word_guessed)
            list_letters = word_guessed
            
        else:
            num_lives = num_lives -1
            print('Sorry, ' + ll + ' is not in the word.')
            print('You have ' + str(num_lives) + ' lives left.')


    def ask_letter():
        while True:

            letter_anycase = input()
            letter = letter_anycase.lower()

            if len(letter)!=1:
                print('Please, enter just one character')
                continue

            if not letter.isalpha():
                print('Enter only letters')
                continue

            if letter in list_letters:
                print(letter, " was already tried.")
                continue

            else:
                list_letters.append(letter)  
                check_letter(letter)   

            if num_lives == 0:
                print("You ran out of lives. The word was " + word + '.')
                break
  

def play_game(word_list):
    game = Hangman(word_list, num_lives=5)
    game.ask_letter()

if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    play_game(word_list)
