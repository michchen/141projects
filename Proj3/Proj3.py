# Proj3.py
# Fall 2013
# CS 141
#
# Created by: Michelle Chen
# mchen01@email.wm.edu
# (937)423-9630
#
# This program offers 5 word games that use dictionary.txt as the source.
# Game 1 finds words with only one vowel and excludes a specific letter
# Game 2 finds words with i, j, t, and x only once
# Game 3 finds words with all but one letter of a user-given string
# Game 4 finds words with all the letters of another word (with a max length)
# Game 5 finds palindromes of a specific length
# If the user inputs a 'q' the game will quit

dictionary = open("dictionary.txt", "r")
import string

###
def one_vowel():
    """Finds word of a user specified length and excludes a user specified
    letter"""
    length = (input("Please enter the word length you are looking for: "))  
    for number in length:
        while number in length not in string.digits:
            print("Incorrect input")
            length = input("Please enter an integer length: ")
        # Makes sure that the length inputed is an integer value
    print(length)
    print("")
    length = int(length)
    # converts the length to an integer to use later
    
    excluded_letter = input("Please enter the letter you'd like to exclude: ")
    while excluded_letter not in string.ascii_letters \
          or len(excluded_letter) > 1:
        print("Incorrect input")
        excluded_letter = input("Please enter one letter: ")
        # Makes sure that the input is a letter
    print(excluded_letter)
    print("")
    
    for word in dictionary:
        word = word.strip()
        vowel_count = 0
        if excluded_letter not in word:
            # Finds the words that exclude a certain letter
            if len(word) == length:
                for letter in word:
                    vowels = "aeiou"
                    if letter in vowels:
                        vowel_count += 1
                    #Makes sure that there is only one vowel
                if vowel_count == 1:
                    print(word)
    print("")
###


###
def ijtx_once():
    """Finds words that use i, j, t, and x exactly once"""
    for word in dictionary:
        word = word.strip()
        i_count = 0
        j_count = 0
        t_count = 0
        x_count = 0
        # Initializing the letter counters for later
        
        for letter in word:
            if letter == "i":
                i_count += 1
            if letter == "j":
                j_count += 1
            if letter == "t":
                t_count += 1
            if letter == "x":
                x_count += 1
            # Counts the occurrence of certain letters
            
        if i_count == 1 and j_count == 1 and t_count == 1 and x_count == 1:
            print(word)
    
    print("")
###         


###
def all_but_one():
    """Prints words that contain all but one letter in a string of characters"""
    string_count = 0
    characters = input("Please enter a string of characters: ")
    print(characters)
    print("")
    
    for word in dictionary:
        word = word.strip()
        string_count = 0
        for letter in characters:
            if letter in word:
                string_count += 1
            # Looks for matching letters in the string characters and keeps
            # a count
        if string_count == (len(characters) - 1):
            # If the count is one less than the length of characters
            # it fulfills the requirement and will print
            print(word)
    
    print("")
###
                

###
def letters_of_another_word():
    """Finds words that contain all the letters of a user specificed word"""
    base_word = input("Enter word: ")
    for letter in base_word:
        while letter not in string.ascii_letters:
            print("Incorrect input")
            base_word = input("Please enter a word: ")
            # Ensures the input is letters
    print(base_word)
    print("")
    
    length = input("What is the maximum length of the words you want: ")
    for number in length:
        while number in length not in string.digits:
            print("Incorrect input")
            length = input("Please enter an integer length: ")
        # Makes sure the input is integer values
    print(length)
    length = int(length)
    print("")
    
    for word in dictionary:
        word = word.strip()
        tempstr = base_word
        # Creates a copy to pop letters out of
        if len(word) <= length:
            for letter in word:
                if letter in base_word:
                    tempstr = ''.join(tempstr.rsplit(letter, 1))
                    # Gets rid of the letters once it finds one occurrence
                if tempstr == '':
                    print(word)
                    # If the tempstr is empty, it has found all of the letters
    print("")
###


###
def palindromes():
    """Finds words of a user specified length that are palindromes"""
    length = input("Enter length of desired words: ")
    for number in length:
        while number in length not in string.digits:
            print("Incorrect input")
            length = input("Please enter an integer length: ")
        # Ensures the value is an integer
    print(length)
    length = int(length)
    print("")
    
    pool = ""
    # Creates a pool to use if there are no words that are palindromes
    
    for word in dictionary:
        word = word.strip().lower()
        # Ensures that the word is all the same case
        if len(word) == length:
            if word == word[::-1]:
                # Sees if the word is a palindrome by checking if
                # the reverse is equal to the original word
                print(word)
                pool = word
    
    if pool == "":
        print("There are no words that fit this criteria.")
    print("")
###


###
def menu():
    """Prints an opening menu"""
    print("Choose which game you want to play")
    print("a) Find words with only one vowel and excluding a specific letter")
    print("b) Find words containing i, j, t, and x exactly once")
    print("c) Find words containing all but one letter of a given string")
    print("d) Find words containing all the letters of another word with a" \
      "maximum length")
    print("e) Find palindromes of a particular length")
    print("q) quit")
    print("")   
###


###
def main():
    """The main shell that calls upon all the other procedures"""
    menu()
    
    choice = input("Enter a choice: ")
    print(choice)
    choice = choice.lower()
    
    while choice != "q":
        dictionary.seek(0)
        if choice == "a":
            one_vowel()
        elif choice == "b":
            ijtx_once()
        elif choice == "c":
            all_but_one()
        elif choice == "d":
            letters_of_another_word()
        elif choice == "e":
            palindromes()
        else:
            print("")
            print("You've entered an incorrect choice. Try again")
            print("")
        # Makes sure the values are all valid and if not prints an error
        
        menu()
        # Reprints the menu choices
        choice = input("Enter a choice: ")
        print(choice)
        choice = choice.lower()        

    if choice == "q":
        print("")
        print("Thanks for playing")
###

main()

dictionary.close()