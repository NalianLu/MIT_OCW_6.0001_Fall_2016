# Problem Set 2, hangman.py
# Name: Norah Lu
# Collaborators:
# Time spent: 9:25am-

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


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
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    unique_char = list(set(list(secret_word)))
    result = True
    for c in unique_char:
        if c not in letters_guessed:
            result = False
            break
    return result




def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    unique_char = list(set(list(secret_word)))
    guessed_char=[] # initialize
    for c in unique_char:
        if c in letters_guessed:
            guessed_char.append(c)
    result = list('_'*len(secret_word)) # initialize
    index = 0 # initialize
    for c in secret_word:
        if c in guessed_char:
            result[index] = c
        index += 1
    result = ' '.join(result) # list -> string
    return result



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    available_letter = string.ascii_lowercase # initialize
    for l in letters_guessed:
        available_letter = available_letter.replace(l,'')
    return available_letter

    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    
    # Initialize
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is',len(secret_word),'letters long.')
    letters_guessed = [] # initialize
    num_warn = 3 # get 3 warnings at the beginning of the game
    print('You have', num_warn, 'warnings left')
    num_guess = 6 # start with 6 guesses
    
    # Game
    while num_guess>0 and (not is_word_guessed(secret_word, letters_guessed)):
        # Before Next Round
        print('-------------')
        print('You have', num_guess ,'guesses left.')
        Available_letter = get_available_letters(letters_guessed)
        print('Available letters:',Available_letter)
        # User Input
        user_letter = input('Please guess a letter:')
        # Input Validation
        if str.isalpha(user_letter):
            user_letter = str.lower(user_letter)
            # Check Correctness
            if user_letter in letters_guessed:
                num_warn -= 1
                if num_warn >= 0:
                    print("Oops! You've already guessed that letter.", 
                          'You have', num_warn, 'warnings left:',
                          get_guessed_word(secret_word, letters_guessed))
                else:
                    num_guess -= 1
                    if num_guess > 0:
                        print("Oops! You've already guessed that letter.",
                            'You have no warnings left so you lose one guess:',
                            get_guessed_word(secret_word, letters_guessed))
                    else:
                        break
            elif user_letter in secret_word:
                letters_guessed.append(user_letter)
                print('Good guess:', get_guessed_word(secret_word, letters_guessed))
            else:
                letters_guessed.append(user_letter)
                if user_letter in ['a','e','i','o']:
                    num_guess -= 2
                    if num_guess <= 0:
                        print('Oops! That letter is not in my word:', get_guessed_word(secret_word, letters_guessed))
                        break
                    else:
                        print('Oops! That letter is not in my word.')
                        print('Please guess a letter:', get_guessed_word(secret_word, letters_guessed))
                else:
                    num_guess -= 1
                    if num_guess == 0:
                        print('Oops! That letter is not in my word:', get_guessed_word(secret_word, letters_guessed))
                        break
                    else:
                        print('Oops! That letter is not in my word.')
                        print('Please guess a letter:', get_guessed_word(secret_word, letters_guessed))
        else:
            num_warn -= 1
            if num_warn >= 0:
                print('Oops! That is not a valid letter.',
                      'You have', num_warn, 'warnings left:',
                      get_guessed_word(secret_word, letters_guessed))
            else:
                num_guess -= 1
                if num_guess > 0:
                    print('Oops! That is not a valid letter.',
                        'You have no warnings left so you lose one guess:',
                        get_guessed_word(secret_word, letters_guessed))
                else:
                    break

    # total score
    num_unique_letter = len(set(list(secret_word)))
    score = num_guess*num_unique_letter
    
    # win
    if is_word_guessed(secret_word, letters_guessed):
        print('-------------')
        print('Congratulations, you won!')
        print('Your total score for this game is:', score)
    else:
        print('-------------')
        print('Sorry, you ran out of guesses. The word was '+secret_word+'.')

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    my_word = my_word.replace(" ", "") # remove space
    my_letter = list(set(list(my_word.replace("_", "")))) # unique letter
    result = True # initialize
    if len(my_word) != len(other_word):
        result = False
    else:
        for (index,item) in enumerate(my_word):
            if str.isalpha(item):
                if my_word[index] != other_word[index]:
                    result = False
            else:
                if other_word[index] in my_letter:
                    result = False
    return result



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    match = []
    for word in wordlist:
        if match_with_gaps(my_word, word):
            match.append(word)
    if len(match) == 0:
        print('No matches found')
    else:
        print(" ".join(match))



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    # Initialize
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is',len(secret_word),'letters long.')
    letters_guessed = [] # initialize
    num_warn = 3 # get 3 warnings at the beginning of the game
    print('You have', num_warn, 'warnings left')
    num_guess = 6 # start with 6 guesses
    
    # Game
    while num_guess>0 and (not is_word_guessed(secret_word, letters_guessed)):
        # Before Next Round
        print('-------------')
        print('You have', num_guess ,'guesses left.')
        Available_letter = get_available_letters(letters_guessed)
        print('Available letters:',Available_letter)
        # User Input
        user_letter = input('Please guess a letter:')
        # Input Validation
        if str.isalpha(user_letter):
            user_letter = str.lower(user_letter)
            # Check Correctness
            if user_letter in letters_guessed:
                num_warn -= 1
                if num_warn >= 0:
                    print("Oops! You've already guessed that letter.", 
                          'You have', num_warn, 'warnings left:',
                          get_guessed_word(secret_word, letters_guessed))
                else:
                    num_guess -= 1
                    if num_guess > 0:
                        print("Oops! You've already guessed that letter.",
                            'You have no warnings left so you lose one guess:',
                            get_guessed_word(secret_word, letters_guessed))
                    else:
                        break
            elif user_letter in secret_word:
                letters_guessed.append(user_letter)
                print('Good guess:', get_guessed_word(secret_word, letters_guessed))
            else:
                letters_guessed.append(user_letter)
                if user_letter in ['a','e','i','o']:
                    num_guess -= 2
                    if num_guess <= 0:
                        print('Oops! That letter is not in my word:', get_guessed_word(secret_word, letters_guessed))
                        break
                    else:
                        print('Oops! That letter is not in my word.')
                        print('Please guess a letter:', get_guessed_word(secret_word, letters_guessed))
                else:
                    num_guess -= 1
                    if num_guess == 0:
                        print('Oops! That letter is not in my word:', get_guessed_word(secret_word, letters_guessed))
                        break
                    else:
                        print('Oops! That letter is not in my word.')
                        print('Please guess a letter:', get_guessed_word(secret_word, letters_guessed))
        elif user_letter == '*':
            print('Possible word matches are:')
            show_possible_matches(get_guessed_word(secret_word, letters_guessed))

        else:
            num_warn -= 1
            if num_warn >= 0:
                print('Oops! That is not a valid letter.',
                      'You have', num_warn, 'warnings left:',
                      get_guessed_word(secret_word, letters_guessed))
            else:
                num_guess -= 1
                if num_guess > 0:
                    print('Oops! That is not a valid letter.',
                        'You have no warnings left so you lose one guess:',
                        get_guessed_word(secret_word, letters_guessed))
                else:
                    break

    # total score
    num_unique_letter = len(set(list(secret_word)))
    score = num_guess*num_unique_letter
    
    # win
    if is_word_guessed(secret_word, letters_guessed):
        print('-------------')
        print('Congratulations, you won!')
        print('Your total score for this game is:', score)
    else:
        print('-------------')
        print('Sorry, you ran out of guesses. The word was '+secret_word+'.')



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #secret_word = 'else' # only for test !!! 
    #print(secret_word) # only for test !!!
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    # secret_word = 'apple' # only for test !!!
    hangman_with_hints(secret_word)