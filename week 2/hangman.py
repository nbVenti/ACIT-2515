import random

True

def get_rand_word():
    with open(r'Week 2\words.txt', "r") as f:
        word = f.readlines()
        random_word = random.choice(word).strip("\n")
        print(random_word)
        return random_word

def hangman():
    word = get_rand_word()
    p_guesses = ['_'] * len(word)
    
    while True:
        print(" ".join(p_guesses))
        x = prompt("Enter letters to guess or word")
        
        if x == word:
            win()

        for i in range(len(word)):
            if x == word[i]:
                p_guesses[i] = x          
        
        if (" ".join(p_guesses).replace(" ", "")) == word:
            win()


                
            

def prompt(user):
    u_input = input(user +"\n>>")
    if u_input.isalpha():
        return u_input
    else:
        prompt(user)
    
def win():
    x = prompt("Do you want to play again")
    print(x)
    if x == "y" or x == 'yes' or x == "Yes":
        hangman()
    else:
        exit()
    
    
hangman()
