""""
ACIT2515 Lab

Week 2 -- complete this file!

"""
import random

# The number of turns allowed is a global constant
NB_TURNS = 10

def pick_random_word():
    """Opens the words.txt file, picks and returns a random word from the file"""
    # WRITE YOUR CODE HERE !
    with open(r'week_2\words.txt', "r") as f:
        word = f.readlines()
        random_word = random.choice(word).strip("\n")
    print(random_word)
    return random_word
    

def reveal_letters(word, letters): 
    """
    This function RETURNS A STRING.
    This function scans the word letter by letter.
    First, make sure word is uppercase, and all letters are uppercase.
    If the letter of the word is in the list of letters, keep it.
    Otherwise, replace it with an underscore (_).
    Make sure all letters are separated by a space, then return the string.

    DO NOT USE PRINT!

    Example:
    >>> reveal_letters("VANCOUVER", ["A", "V"])   
    'V A _ _ _ _ V _ _'
    >>> reveal_letters("TIM", ["G", "V"])
    '_ _ _'
    >>> reveal_letters("PIZZA", ["A", "I", "P", "Z"])
    'P I Z Z A'
    """
    # WRITE YOUR CODE HERE
    word = word.upper(); letters = [x.upper() for x in letters]; reveal = ["_"] * len(word)
    for i in range(len(reveal)):
        if word[i] in letters:
            reveal[i] = word[i]
    reveal = " ".join(reveal)

    return reveal

def test_reveal():
    assert reveal_letters("VANCOUVER", ["A", "V"]) == 'V A _ _ _ _ V _ _'
    assert reveal_letters("TIM", ["G", "V"]) == '_ _ _'
    assert reveal_letters("PIZZA", ["A", "I", "P", "Z"]) == 'P I Z Z A'
    assert reveal_letters("1", ["1"]) == '1'

def all_letters_found(word, letters):
    """Returns True if all letters in word are in the list 'letters'"""
    
    counter = 0
    for i in letters:
        for u in word:
            if u == i:        
                counter += 1
    if counter >= len(word):
        return True
    else:
        return False
    
    
    
def main(turns):
    """
    Runs the game. Allows for "turns" loops (attempts).
    At each turn:
    1. Ask the user for a letter
    2. Add the letter to the list of letters already tried by the player
    3. If the letter was already tried, ask again
    4. Use the reveal_letters function to display hints about the word
    5. Remove 1 to the number of tries left
    6. Check if the player
        - won (= word has been found)
        - lost (= word has not been found, no tries left)

    Do not forget to pick a random word first :-)

    """
    # WRITE YOUR CODE HERE
    word = pick_random_word()
    guessed_letters = []
    while turns > 0:
        u_input = input("Enter a letter\n>>")
        if u_input.isalpha():
            if u_input in guessed_letters:
                print("guess again")
            else:
                guessed_letters.append(u_input)
                turns -= 1
                if all_letters_found(word, guessed_letters) == True:
                    print("You win")
                    break
                else:
                    print(reveal_letters(word, guessed_letters))
    

if __name__ == "__main__":
    main(NB_TURNS)
    