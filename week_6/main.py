class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def hi (self):
        print(f"Hi, I'm {self.name} and I'm a {self.species}")
        
    def something(self):
        print("Something", self.name)


class Cat(Pet):
    def __init__(self, name):
        name = name.upper()
        super().__init__(name, "cat")
        # self.name = name
        # self.species = "Cat"  
        
    def hi(self,name):
        print(f"Meow, I'm {self.name} and I'm a ")
        
    def hi(self,name):
        super().hi()
        print("Meow")
        self.something()
    pass


class Dog(Pet):
    pass

p = Dog("Blue", "Dog")

p.hi()  

c = Cat("Cat")
c.hi('test')
d = Dog("Dog")

d.hi()