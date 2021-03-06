# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : <your name>
# Collaborators : <your collaborators>
# Time spent    : <total time>

import math
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    '*': 0, 'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "ps3_words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:  # for each letter in the word
        freq[x] = freq.get(x,0) + 1  # dict[key] = dict.get(key, 0) + 1  ### for each key, take value, if it doesn't exist it is zero. add one.
    return freq


def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.
    You may assume that the input word is always either a string of letters, 
    or the empty string "". You may not assume that the string will only contain 
    lowercase letters, so you will have to handle uppercase and mixed case strings 
    appropriately. 

	The score for a word is the product of two components:

	The first component is the sum of the points for letters in the word.
	The second component is the larger of:
            1, or
            7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
            and n is the hand length when the word was played
    word: string
    n: int >= 0
    returns: int >= 0
    """
    wordlen = len(word)
    word = list(word.lower())
    letter_score = 0

    for letter in word:
        letter_score += SCRABBLE_LETTER_VALUES.get(letter)
        # print(f"letter: {letter}, letter_score: {letter_score}")

    wordlen_score = 7 * wordlen - 3 * (n - wordlen)
    if wordlen_score <= 0:
        wordlen_score = 1

    return wordlen_score * letter_score


def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    
    for letter in hand.keys():
        for j in range(hand[letter]):
            print(letter, end=' ')      # print all on the same line
    print()                             # print an empty line


def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """

    hand = {}
    num_vowels = int(math.ceil(n / 3))  # return smallest integer >= to n/3

    hand['*'] = hand.get('*', 0) + 1

    for i in range(1, num_vowels):  # the 0th element is the wildcard, '*'
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1

    for i in range(num_vowels, n):
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1

    return hand


def update_hand(hand, word):
    """
    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.
    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)
    returns: dictionary (string -> int)
    """
    newhand = hand.copy()
    value = 0

    for letter in word.lower():
        try:
            value = newhand.pop(letter)
        except KeyError:
            pass
        # print("letter: {}, value: {}, hand: {}".format(letter, value, hand))
        try:
            if value >= 2:
                newhand[letter] = value - 1
        except UnboundLocalError:
            pass   # print(hand)
    return newhand
        # pop it from the dict. update value. if value > 0, add back to dict.


def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.

    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """

    # needs to handle wildcards
    # list of words with wildcards replaced.
    # if one of those words is in the word list, pass.
    word_lowercase = word.lower()  # convert word to lowercase
    wildcard_word_list = []  # list of potential words it could be, if the word has a wildcard value
    if word_lowercase.find('*') >= 0:
        for vowel in VOWELS:
            wildcard_word_list.append(word_lowercase.replace('*', vowel))
    else:
        wildcard_word_list.append(word_lowercase)

    if len(list(set(wildcard_word_list) & set(word_list))) >= 1:
        pass
    else:
        return False

    # convert word into a dictionary
    word_dict = get_frequency_dict(word_lowercase)
    # look through all keys in word dictionary and see if value >= that key value in the hand
    for letter in word_dict.keys():
        # print(f"letter: {letter}, in word: {word_dict[letter]}, in hand: {hand.get(letter, 0)}")
        if letter == '*':
            pass
        elif word_dict[letter] <= hand.get(letter, 0):
            # print("you do have enough {}'s in your hand".format(letter))
            pass
        else:
            # print("Not enough {}'s in your hand".format(letter))
            return False
    return True


# word = "e*m"
# hand = {'a': 1, 'r': 1, 'e': 1, 'j': 2, 'm': 1, '*': 1}
#
# word_list = load_words()
# is_valid_word(word, hand, word_list)


def calculate_handlen(hand):
    """
    Returns the length (number of letters) in the current hand.

    hand: dictionary (string-> int)
    returns: integer
    """
    handlen = 0
    for letter in hand.keys():
        handlen += hand.get(letter, 0)
    return handlen


# hand = {'a': 1, 'r': 1, 'e': 3, 'j': 2, 'm': 1, '*': 1}
# print(calculate_handlen(hand))


def play_hand(hand, word_list):

    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.

    * The user may input a word.

    * When any word is entered (valid or invalid), it uses up letters
      from the hand.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two
      exclamation points (the string '!!') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand

    """

    # Keep track of the total score
    total_score = 0
    # As long as there are still letters left in the hand:
    while calculate_handlen(hand) > 0:
        # Display the hand

        print("Current Hand: ", end='')
        display_hand(hand)
        # Ask user for input
        player_input = input("Enter word, or \"!!\" to indicate that you are finished: ")
        # If the input is two exclamation points:
        if player_input == "!!":
            # End the game (break out of the loop)
            break
        # Otherwise (the input is not two exclamation points)
        else:
            # If the word is valid:
            if is_valid_word(player_input, hand, word_list):
                # Tell the user how many points the word earned,
                word_score = get_word_score(player_input, calculate_handlen(hand))
                total_score += word_score
                # and the updated total score
                print(f"\"{player_input}\" earned {word_score} points.  Total: {total_score} points.")
            # Otherwise (the word is not valid):
            else:
                # Reject invalid word (print a message)
                print("That is not a valid word. Please choose another word.")
            # update the user's hand by removing the letters of their inputted word
            hand = update_hand(hand, player_input)
    if calculate_handlen(hand) == 0:
        print("Ran out of letters. ", end='')
    # Game is over (user entered '!!' or ran out of letters),
    # so tell user the total score
    print("Total score: {} points".format(total_score))
    # Return the total score as result of function
    return total_score


# word_list = load_words()
# hand1 = deal_hand(8)
# play_hand(hand1, word_list)
#
# Problem #6: Playing a game
#


#
# procedure you will use to substitute a letter in a hand
#


def substitute_hand(hand, letter):
    """
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provide a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.

    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """

    new_hand = hand.copy()
    new_letter = random.choice(VOWELS + CONSONANTS)
    while new_letter in new_hand:
        new_letter = random.choice(VOWELS + CONSONANTS)

    # print("new letter is :{}".format(new_letter))
    new_hand[new_letter] = new_hand[letter]
    del new_hand[letter]
    return new_hand

# hand = {'a': 1, 'r': 1, 'e': 3, 'j': 2, 'm': 1, '*': 1}
# print(substitute_hand(hand, 'j'))


def play_game(word_list):
    """
    Allow the user to play a series of hands

    * Asks the user to input a total number of hands

    * Accumulates the score for each hand into a total score for the 
      entire series
 
    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to
      substitute letters in the future.

    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep 
      the better of the two scores for that hand.  This can only be done once 
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.

            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.
      
    * Returns the total score for the series of hands

    word_list: list of lowercase strings
    """

    number_of_hands = int(input("Enter the total number of hands: "))
    # track the option to substitute
    has_substituted = 0
    # track the option to replay a hand
    has_replayed = 0
    # track the total score after each hand
    total_score = 0
    # while there are still more hands to go:
    while number_of_hands > 0:

        # deal the hand and display it
        current_hand = deal_hand(HAND_SIZE)
        print("Current hand: {}".format(display_hand(current_hand)))
        # if they still have the option to substitute:
        if has_substituted == 0:
            # ask if they want to substitute, and do it
            substitute = input("Would you like to substitute a letter? ")
            if substitute.lower() == "yes":
                letter = input("Which letter would you like to replace: ")
                # save this as the hand.
                current_hand = substitute_hand(current_hand, letter)
                # eliminate option to substitute
                has_substituted = 1

        # play the hand, display the score
        hand_score = play_hand(current_hand, word_list)
        print("Total score for this hand: {}".format(hand_score))
        print("-----------")
        # if they still have the option to replay:
        if has_replayed == 0:
            replay = input("Would you like to replay the hand? ")
            # if they want to replay the hand
            if replay.lower() == "yes":
                # replay the hand
                replay_score = play_hand(current_hand, word_list)
                # save the replay score
                # if the replay score > saved score, use that score
                if replay_score > hand_score:
                    hand_score = replay_score
        # update total score
        total_score += hand_score
        number_of_hands -= 1

    print("Total score for all hands: {}".format(total_score))


word_list = load_words()
play_game(word_list)

#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
# #
# if __name__ == '__main__':
#     word_list = load_words()
#     play_game(word_list)

