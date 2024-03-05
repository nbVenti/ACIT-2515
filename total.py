#lab 1 NOTE
COURSES = ["ACIT2515", "ACIT1620", "ACIT0220", "ACIT0320","ACIT1420", "ACIT1951", "COMM0330", "COMM0350", "COMM1650","ENGL0220", "ENGL0510", "MATH0150", "ENGL0450", "PROJ0900","PROJ1360"]
import pytest 

class AttributeError(Exception):
    pass

def department_courses(course_list, department):    
    if type(course_list) != list and type(course_list) != tuple:
        return []
    if type(course_list) != (list or tuple):
        return []
    if len(department) <= 3 or len(department)>= 5:
        raise AttributeError("Department must be 4 characters long")
        
    return [x for x in course_list if x[0:4] == department]
    

def text(str) -> str:
    return (str.replace("o" or "O" ,"0").replace("e" or "E", "3").replace("l", "1").replace("I", "|").replace("a","@"))

def test_text():
    assert text("") == ""
    assert text("Hello") == "H3110"
    assert text("Goodbere") == "G00db3r3"
    
def test_department_courses():
    # assert department_courses([], "") == []
    
    # assert department_courses(["ACIT1234"], "") == []
    
    assert department_courses({"ACIT1234"}, "ACIT") == []
    
    assert department_courses(("ACIT1234"), "ACIT") == []
    
    assert department_courses({"ACIT1234"}, "ACIT") == []
    
    assert department_courses({"ACIT1234"}, "ACIT") == []
    
    with pytest.raises(AttributeError):
        department_courses(["ACIT1234"], "ACI")
    
    assert department_courses(["ACIT1234"], "ENGL") == []
    
    assert department_courses(["ACIT1234"], "ACIT") == ["ACIT1234"]
    
    assert department_courses(["ACIT1234", "ACIT5678"], "ACIT") == ["ACIT1234","ACIT5678"]
    
    assert department_courses(["ACIT1234", "ACIT5678", "ENGL1234"], "ACIT") == ["ACIT1234", "ACIT5678"]
    
    assert department_courses(["ACIT1234", "ACIT5678", "ENGL1234"], "ENGL") == ["ENGL1234"]
    
    with pytest.raises(AttributeError):
        department_courses(["ACIT1234", "ACIT5678", "ENGL1234"], "ENG")

# if __name__ == "__main__":
#     test_text()
#     test_department_courses()
#     print("All tests passed!")
    
import random

def get_rand_word():
    with open(r'week_2\words.txt', "r") as f:
        word = f.readlines()
        random_word = random.choice(word).strip("\n")
        print(random_word)
        return random_word

def hangman():
    word = get_rand_word()
    p_guesses = ['_'] * len(word)
    guessed_letters = []
    
    while True:
        print(" ".join(p_guesses))
        while True:
            x = prompt("Enter letters to guess or word")
            if x in guessed_letters:
                print("You already guessed that letter")
            else:
                break
        
        
        if x == word:
            win()

        for i in range(len(word)):
            if x == word[i]:
                p_guesses[i] = x          
        
        if (" ".join(p_guesses).replace(" ", "")) == word:
            win()
        
        guessed_letters.append(x)          

def prompt(user):
    u_input = input(user +"\n>>")
    if u_input.isalpha():
        return u_input
    else:
        prompt(user)
    
def win():
    x = prompt("Do you want to play again")
    if x == "y" or x == 'yes' or x == "Yes":
        hangman()
    else:
        exit()
    

# if __name__ == "__main__":
#     hangman()

class typeError(Exception):
    pass

def average(my_list):
    if not len(my_list):
        return 0 

    try:
        result = sum(my_list)/len(my_list)
    except TypeError:
        raise typeError("The list must contain numbers")

    return result

def test_ave():
    result = average([0,5,10])
    assert result == 5
    
def test_ave2():
    with pytest.raises(typeError):
        average(['a','b','c'])
        
def test_ave3():
    result = average([])
    assert result == 0


list = [1, 2, 3 ,4]

for myVar in range(len(list)):
    print(list[myVar])

# if __name__ == "__main__":
#     test_ave()
#     test_ave2()
#     test_ave3()
    
class Person:
    def __init__(self, name):
        self.name = name
        self.age = 0

    def greet(self):
        return (f"Hello, my name is {self.name} and I am {self.age} years old.")
        
    def birthday(self):
        self.age += 1
        

def create_person():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    p = Person(name)
    p.age = int(age)
    return p
    
def create_from_file():
    with open("person.txt", "r") as file:
        names = [Person(line.strip()) for line in file]   
    return names

# Example usage
person1 = Person("John")
person1.greet()