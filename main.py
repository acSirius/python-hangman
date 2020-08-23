##Hangman game
import random

print(' Hangman game, guess the countrie!\n\n')

a_file = open('countries.txt', 'r')
list_of_lists = [(line.strip()).split() for line in a_file]
a_file.close()

word_arr= random.choice(list_of_lists)
word = word_arr[0].lower()
guess = ''

wrong_letters_list = []

## Every letter turned into a undersore
for letter in word:
    guess = guess + '_'

guess_list = list(guess)

while guess != word:
    ## Ask for a guess
    wrong_letters = ', '.join(wrong_letters_list)
    if len(wrong_letters) > 0:
        print(f'The following letters arent in the word: {wrong_letters}')
    print(f'This is the word so far: {guess}')
    guessed_letter = input('Guess a letter: ').lower()

    if len(guessed_letter) == 1:
        ## Check if the guessed letter is in the word to guess
        if guessed_letter in word:
            ## Find what index guessed letter is in word
            print(f'You guessed it right, the letter {guessed_letter} was part of the word')
            i = 0 
            while i < len(word):
                if word[i] == guessed_letter:
                    guess_list[i] = guessed_letter
                    guess = ''.join(guess_list)
                
                i = i + 1
        else:
            print(f'Wrong! The letter {guessed_letter} isnt a part of the word')
            wrong_letters_list.append(guessed_letter)

    else:
        print('Please only enter one letter!')

    print('\n')

print(f'You guessed it!\nThe word was {guess}')