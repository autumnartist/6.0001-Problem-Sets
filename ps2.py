# Problem Set 2, hangman.py
# Name: Autumn Artist
# Collaborators: Dan Ajayi
# Time spent: 5:00

import random
import string

# -----------------------------------
# HELPER CODE
# -----------------------------------

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    returns: list, a list of valid words. Words are strings of lowercase letters.    
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    returns: a word from wordlist at random
    """
    return random.choice(wordlist)

# -----------------------------------
# END OF HELPER CODE
# -----------------------------------


# Load the list of words to be accessed from anywhere in the program
wordlist = load_words()

def has_player_won(secret_word, letters_guessed):
    '''
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: boolean, True if all the letters of secret_word are in letters_guessed,
        False otherwise
    '''
    # num counts the number of letters that are shared by both the letters guessed and the secret word
    num = 0
    # in the case that the secret word is an empty string the player will automatically win
    if len(secret_word) == 0:
        return True
    # goes through the letters guessed arrays using a for loop
    for i in letters_guessed:
        # goes through each letter in the secret word 
        # nested this way --> also accounts for same letters that are in the secret word
        for x in secret_word:
            # if the letter is shared by both the guessed letters and is also in the secret word
            if i == x:
                num += 1
                # if the num is equal to the length of the secret word - the player has won
                if num == len(secret_word):
                    return True
    return False
                


def get_word_progress(secret_word, letters_guessed):
    '''
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters and plus signs (+) that represents
        which letters in secret_word have not been guessed so far
    '''
    # empty list to hold each letter and change it if needed
    word = []
    # converting the array to a str in order to print as if a word
    text = ""
    # showing the each letter as a +
    for x in range(len(secret_word)):
        word.append("+")
    #Takes each individual letter in the secret word and checks if its inside the letters guessed list
    for x in range(len(secret_word)):
        letter1 = str(secret_word[x])
        for i in letters_guessed:
            letter2 = str(i)
            # if the one of the letters in the secret word was guessed it would change the word list 
            # by going from that specific index and changes the "+" that's stored by default to 
            # the actual letter, while leaving the rest letters as a plus
            if letter1 == letter2:
                word[x] = i
    # takes each element of the list and adds it to the text as a string
    for l in word:
        text += l
    return text


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters that represents which
      letters have not yet been guessed. The letters should be returned in
      alphabetical order
    '''
    #guess for the string
    guess = ""
    #empty list for each letter of the alphabet
    alphabet = []
    #Makes the alphabet array list
    for i in range(len(string.ascii_lowercase)):
        alphabet.append(string.ascii_lowercase[i])
    # for loop which checks which letters have already been guessed 
    # done by a for loop through the letters_guessed list, if the alphabet list 
    # and the guessed list share any of the same letters, the letter is removed
    # from the alphabet list
    for i in letters_guessed:
        letter1 = str(i)
        for x in alphabet:
            letter2 = str(x)
            if letter1 == letter2:
                alphabet.remove(letter1)
    # need it to return the list as a text 
    # converts the list of letters left into a string and is returned 
    for x in alphabet:
        letter3 = str(x)
        guess += letter3
    return guess

#To see if a letter is a vowel
def isVowel(letter):
    vowels = ["a", "e", "i", "o", "u"]
    for i in vowels:
        if letter == str(i):
            return True
    return False

# To recieve a random letter user hasn't already guessed that's within the
# secret word
def get_hint(secret_word, func): 
    # func in this case would be get_available letters
    # letters in the secret word that haven't already been guessed will go
    # inside the string choose_from
    choose_from = ""
    # for every letter in the available letters left --> if it is also in the 
    # secret word it is added to the string choose_from
    for i in func:
        for x in secret_word:
            if i == x:
                choose_from += i    
    # new will be a random index between 0 and the last index in the string of 
    # choose_from -- given be len(choose_from)-1
    new = random.randint(0, len(choose_from)-1)
    # the random int is then used to show the letter assigned to that index 
    # and is returned
    revealed_letter = choose_from[new]
    return revealed_letter
    
#To find number of unquie letter
def unique_letters(secret_word):
    #list to add all the unquie letters into
    word_list = []
    for i in secret_word:
        # goes throuogh each letter in the specific word and if it isn't 
        # already in the word_list then it is added, this stops the same letter
        # from being counted towards the number of unique letters
        if i not in word_list:
            word_list.append(i)
    # returns the length of the word_list
    return len(word_list)      

def hangman(secret_word, with_help):
    '''
    secret_word: string, the secret word to guess.
    with_help: boolean, this enables help functionality if true.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses they start with.

    * The user should start with 10 guesses.

    * Before each round, you should display to the user how many guesses
      they have left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a single letter (or help character '!'
      for with_help functionality)

    * If the user inputs an incorrect consonant, then the user loses ONE guess,
      while if the user inputs an incorrect vowel (a, e, i, o, u),
      then the user loses TWO guesses.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    -----------------------------------
    with_help functionality
    -----------------------------------
    * If the guess is the symbol !, you should reveal to the user one of the
      letters missing from the word at the cost of 3 guesses. If the user does
      not have 3 guesses remaining, print a warning message. Otherwise, add
      this letter to their guessed word and continue playing normally.

    Follows the other limitations detailed in the problem write-up.
    '''
    #Set Up
    print("Welcome to Hangman!")
    word_length = len(secret_word)
    num_guesses = 10
    #gussed_letters will keep the letters guessed within an arrary
    guessed_letters = []
    print(f'I am thinking of a word that is {word_length} letters long.')
    #Game plays as long as you have more guesses than 0
    while num_guesses > 0:
        print("--------------")
        print(f'You have {num_guesses} guesses left')
        # saving letters still available
        letters_left = get_available_letters(guessed_letters)
        letters = ""
        # each letter within the list will be saved in the string letters and 
        # printed for the user to see 
        for i in letters_left:
            letters += str(i)
        print(f'Available letters: {letters}')
        guess = str(input("Please guess a letter: "))
        #Getting help
        # if the user inputs a "!" and the with_help function is on 
        if guess == "!" and with_help == True:
            # user won't get help if the number of guesses left is less than 3
            if num_guesses >= 3:
                # a hint cost 3 guesses
                num_guesses -= 3
                # reveals a letter from the secret word and updates the user
                # by showing the letters they have and whats left
                hint_letter = get_hint(secret_word, letters_left)
                print(f'Letter revealed: {hint_letter}')
                guessed_letters.append(hint_letter)
                print(f'{get_word_progress(secret_word, guessed_letters)}')
            else:
                # in the case where the user doesn't have more than 3 guesses left
                # the code won't run but will let the user know
                print(f'Oops! Not enough guesses left: {get_word_progress(secret_word, guessed_letters)}')
        # if the guess is part of the alphabet 
        # ie no special characters, the code only accepts letters
        elif guess.isalpha():
            guess = guess.lower()
            # checking if user guessed the same letter
            # if the user's guess is already contained within the 
            # guessed_letters list it will notify the user
            if guess in guessed_letters:
               print(f"Oops! You've already guessed that letter: {get_word_progress(secret_word, guessed_letters)}")
            else:
            # if the user guessed a new letter its added to the list of letters guessed
                guessed_letters.append(guess)
            # tests if the guessed letter is contained in the secret word  
            if guess in secret_word:
                print(f'Good guess: {get_word_progress(secret_word, guessed_letters)}')
            else:
                print(f'Oops! That letter is not in my word: {get_word_progress(secret_word, guessed_letters)}')
                # number of guesses decrease by 2 if the guessed letter was a vowel
                # if not and the guessed letter is a consant then the number of 
                # guesses decreases by 1
                if isVowel(guess):
                    num_guesses -= 2
                else:
                    num_guesses -= 1
        else:
            # code won't run if the user inputs a character that isn't "!" or a 
            # letter but lets the user input another guess without decreasing 
            # the number of guesses
            print("Oops! That is not a valid letter. Please input a letter from the alphabet: {get_word_progress(secret_word, guessed_letters)}")
        # if the player has won the congraulatory message is sent 
        if has_player_won(secret_word, guessed_letters) == True:
            print("--------------")
            print("Congratulations, you won!")
            # finds the total score by taking into account the number of unique 
            # letters in the secret word, the number of guesses left and the 
            # length of the secret word
            total_score = 4*unique_letters(secret_word)*num_guesses + 2*len(secret_word)
            print(f'Your total score for this game is: {total_score}')
            # after the user wins the game (code) will stop running
            break
        # if the player hasn't won but has lost all of their guesses, the player
        # loses and the losing message is sent
        if num_guesses <= 0:
            print("--------------")
            # lets the user know what the secret word was
            print(f'Sorry, you ran out of guesses. The word was {secret_word}.')
            # game (code) stops running
            break



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the lines to test

if __name__ == "__main__":
    # To test your game, uncomment the following two lines.
    secret_word = choose_word(wordlist)
    with_help = True
    hangman(secret_word, with_help)

    # After you complete with_help functionality, change with_help to True
    # and try entering "!" as a guess!

    ###############

    # SUBMISSION INSTRUCTIONS
    # -----------------------
    # It doesn't matter if the lines above are commented in or not
    # when you submit your pset. However, please run ps2_student_tester.py
    # one more time before submitting to make sure all the tests pass.
    pass