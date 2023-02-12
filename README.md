# Hangman Game


The code is written for a classic Hangman game in which a player thinks of a word and the other player tries to guess that word within a certain number of attempts. This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

Following is some description of the code:

## Random selection of a word
The programme selects a word randomly from a list of words provided. It finds out the length of characters and prints '_'  *  len(word) as a guessed word (word_guessed).

## Number of lives
The programme is written to provide 5 lives to the user to correctly guess the word.

The code mainly works on two methods inside the Hangman class:

## method 1: ask_letter

The method asks the user for a letter and checks the following to ensure a valid input:
1. If the input is a sigle character
2. If the input is an alphabetical character 
3. If the letter has already been tried

## method 2: check_letter

If the input passes the above checks outlined in ask_letter method, it is given as input to check_letter method. It checks if the letter is in the word.
* If it is, it replaces the '_' in the word_guessed with the letter.
* If it is not, it reduces the number of lives by 1.

The two methods are called insided a while loop, which breaks when one of the following two conditions are met:
1. When the user correctly guesses the word while number of remanining lives are more than zero
2. When the remaining number of lives reaches zero