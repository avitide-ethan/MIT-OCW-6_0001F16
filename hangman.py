# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "hangman_words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
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
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program


def is_word_guessed(secret_word, letters_guessed):
    """
    :param secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    :param letters_guessed:  list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    :return: boolean, True if all the letters of secret_word are in letters_guessed; False otherwise
    """
    # convert secret word to unique list of letters
    unique_secret_word_letters = set(list(secret_word))
    for letter in letters_guessed:
        try:
            unique_secret_word_letters.remove(letter)
            # print(unique_secret_word_letters)
        except KeyError:
            pass
    if len(unique_secret_word_letters) == 0:
        return True
    else:
        return False


def get_guessed_word(secret_word, letters_guessed):
    """
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    """
    # convert secret word to list of letters
    secret_word_list = list(secret_word)
    secret_word_list_reveal = ['_ '] * len(secret_word_list)
    # print(f"Secret word list: {secret_word_list}, secret word list hidden: {secret_word_list_reveal}")
    # iterate through letters_guessed
    for secret_letter_index in range(len(secret_word)):
        for letter_guessed in letters_guessed:
            if secret_word[secret_letter_index] == letter_guessed:
                secret_word_list_reveal[secret_letter_index] = letter_guessed
    secret_word_string_reveal = ''
    for element in secret_word_list_reveal:
        secret_word_string_reveal += element
        # print("Element: {}, String: {}".format(element, secret_word_string_reveal))
    return secret_word_string_reveal


def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    """
    alphabet_list = ('a b c d e f g h i j k l m n o p q r s t u v w x y z').split(' ')
    for letter in letters_guessed:
        try:
            alphabet_list.remove(letter)
        except ValueError:
            pass
    available_letters = ''
    for element in alphabet_list:
        available_letters += element
    return available_letters


def guess_state(letter_guessed, secret_word):
    for secret_letter_index in range(len(secret_word)):
        if secret_word[secret_letter_index] == letter_guessed:
            return True
    return False


def you_win(secret_word, num_guesses):
    print("Congrats Willis, you win!!")
    print(f"Your total score for this game is: {len(secret_word) * (num_guesses - 1)}")


def get_validate_guess(num_warnings):
    user_input = input("Please guess a letter. \n> ")
    if str.isalpha(user_input.lower()):
        return user_input.lower(), num_warnings
    else:
        print("You done fucked up Willis! One warning used up!")
        return None, num_warnings - 1


def hangman(secret_word):
    """
    secret_word: string, the secret word to guess.
    Starts up an interactive game of Hangman.
    """
    print("Welcome to hangman.")
    print(f"I'm thinking of a word that is {len(secret_word)} letters long.")
    letters_guessed = []
    num_guesses = 8
    num_warnings = 3
    while num_guesses > 0 and num_warnings > 0:

        print(f"You have {num_guesses} guesses, and {num_warnings} warnings.")
        print(f"Available letters: {get_available_letters(letters_guessed)}")
        letter_guessed, num_warnings = get_validate_guess(num_warnings)
        if letter_guessed == None:
            continue
        letters_guessed.append(letter_guessed)

        if guess_state(letter_guessed, secret_word):
            print("Damn! Good guess son!")
            num_guesses += 1
        else:
            print("Nope! Bad guess")
        print("------------------------")
        print(get_guessed_word(secret_word, letters_guessed) + "\n")
        if is_word_guessed(secret_word, letters_guessed):
            you_win(secret_word, num_guesses)
            return
        num_guesses -= 1

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
# (hint: you might want to pick your own
# secret_word while you're doing your own testing)
# -----------------------------------


def match_with_gaps(my_word, other_word):
    """
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    """

    my_word = my_word.replace(' ', '')  # remove spaces from my_word
    # print(f"my_word: {my_word}, other_word: {other_word}")

    if len(my_word) != len(other_word):
        # print("Lengths don't match")
        return False  # check length

    my_word_list = list(my_word)
    other_word_list = list(other_word)
    # print(f"my_word_list: {my_word_list}, other_word_list: {other_word_list}")

    for index in range(len(my_word_list)):  # can be a letter or _
        if my_word_list[index] == other_word_list[index]:  # if the letters are equal
            pass
        elif my_word_list[index] == "_":
            if other_word_list[index] in my_word_list:  # if "_" in my_word is already present in other word
                return False
            pass
        else:  # if the letters don't match
            return False
    return True

    # to be true:
    # lengths must be the same
    # letters in my_word are all present in other_word
    # underscore in my_word can't be a letter already present in other word


def show_possible_matches(my_word, wordlist):
    """
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    """
    number_possible_matches = 0
    for word in wordlist:
        if match_with_gaps(my_word, word):
            print(word + " ", end='')
            number_possible_matches += 1
    if number_possible_matches == 0:
        print("No matches. This is a dumb word.")
    print("\n")


def get_validate_guess_with_hints(num_warnings):
    user_input = input("Please guess a letter. \n> ")
    if str.isalpha(user_input.lower()):
        return user_input.lower(), num_warnings
    elif user_input == '*':
        print("Alright, here's a hint. Your word could be any of the following words: ")
        return '*', num_warnings
    else:
        print("You done fucked up Willis! One warning used up!")
        return None, num_warnings - 1


def hangman_with_hints(secret_word):
    """
    secret_word: string, the secret word to guess.
    Starts up an interactive game of Hangman.
    """
    print("Welcome to hangman.")
    print(f"I'm thinking of a word that is {len(secret_word)} letters long.")
    letters_guessed = []
    num_guesses = 6
    num_warnings = 3
    while num_guesses > 0 and num_warnings > 0:

        print(f"You have {num_guesses} guesses, and {num_warnings} warnings.")
        print(f"Available letters: {get_available_letters(letters_guessed)}")
        letter_guessed, num_warnings = get_validate_guess_with_hints(num_warnings)
        if letter_guessed == None:
            continue
        elif letter_guessed == '*':
            show_possible_matches(get_guessed_word(secret_word, letters_guessed), wordlist)
            continue

        letters_guessed.append(letter_guessed)

        if guess_state(letter_guessed, secret_word):
            print("Damn! Good guess son!")
            num_guesses += 1
        else:
            print("Nope! Bad guess")
        print("------------------------")
        print(get_guessed_word(secret_word, letters_guessed) + "\n")
        if is_word_guessed(secret_word, letters_guessed):
            you_win(secret_word, num_guesses)
            return
        num_guesses -= 1


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


# if __name__ == "__main__":
#     # pass
#
#     # To test part 2, comment out the pass line above and
#     # uncomment the following two lines.
#
#     secret_word = choose_word(wordlist)
#     hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 

wordlist = load_words()

secret_word = choose_word(wordlist)
hangman_with_hints(secret_word)
# secret_word = choose_word(wordlist)
# # secret_word = 'appetizer'
# hangman(secret_word)

# show_possible_matches("a_ _ le", wordlist)