import random

class SecretWord:
    def __init__(self,word=None):
        if word == None:
            with open(r'./week_2\words.txt', "r") as f:
                word = f.readlines()
                word = "Vancouver"              
            
        self.word = word.lower()
        
    def show_letters(self,letters):
        # word = "_" * len(self.word)
        # for letter in letters:
        #     word = word.replace(letter.lower(),letter.upper())
        # word = " ".join(word)
        word = self.word.upper()
        letters = [x.upper() for x in letters]
        reveal = ["_"] * len(word)
        for i in range(len(reveal)):
            if word[i] in letters:
                reveal[i] = word[i]
        reveal = " ".join(reveal)
        return reveal
    
    def check_letters(self,letters):
        for letter in letters:
            if letter.lower() not in self.word:
                return False
        return True
    
    def check(self,word):
        if word.lower() == self.word:
            return True
        else:
            return False


    