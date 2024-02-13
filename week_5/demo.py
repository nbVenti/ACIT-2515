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