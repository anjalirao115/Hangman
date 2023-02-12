#%%
import random

class Hangman:
    '''
    A Hangman Game that asks the user for a letter and checks if it is in the word.
    It starts with a default number of lives and a random word from the word_list.
    '''

    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.word = random.choice(self.word_list)
        self.num_letters = len(self.word)
        self.num_lives = num_lives
        self.word_guessed = ['_'] * len(self.word)
        print(f"The mystery word (fruit) has {len(self.word)} characters")
        print(self.word_guessed)

    def check_letter(self, guess):
        '''
        Checks if the letter is in the word.
        If it is, it replaces the '_' in the word_guessed list with the letter.
        If it is not, it reduces the number of lives by 1.
        '''
        if guess in self.word:
            for i in range(len(self.word)):
                if self.word[i] == guess:
                    self.word_guessed[i] = guess
            print(self.word_guessed)               

        else:
            self.num_lives = self.num_lives -1
            print(f"Sorry, {guess} is not in the word, {self.num_lives} lives left.")

    def ask_letter(self):
        '''
        Asks the user for a letter and checks two things:
        1. If the letter has already been tried
        2. If the character is a single character
        If it passes both checks, it calls the check_letter method.
        '''
        list_letters = []
        while True:
            guess = input("Enter a letter: ").lower()

            if guess.isalpha()==False or len(guess)!=1:
                print("Oops! That is not a valid input.")
                continue
            
            if guess in list_letters:
                print(f"{guess} is already guessed.")
                continue

            else:
                list_letters.append(guess)
                self.check_letter(guess)

            # first condition to break the while loop
            if list(self.word_guessed)==list(self.word):
                print("Congratulation, You won!")
                break
            
            # second condition to break the while loop
            if self.num_lives==0:
                print(f"Game Over! The word is {self.word}")
                break


def play_game(word_list):
    game = Hangman(word_list, num_lives=5)
    game.ask_letter()

if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    play_game(word_list)


# %%
