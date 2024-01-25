

class Person():
    def __init__(self,name,age):
        self.name = name 
        self.age = age
    
    def say_hi(self):
        print("Hello, my name is",self.name,"and I am",self.age ,"years old.")
        
    def say_bye(self, name):
        print("Goodbye",name)
        
    def birthday(self):
        self.age += 1
        
    pass

p = Person("John", 36)
p2 = Person("Jane", 30)
p2.say_hi()
p3 = Person("Bob", 40)

p3.say_bye(p.name)
