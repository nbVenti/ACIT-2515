class Parent:
  def __init__(self):
    self.number = 10

class Child(Parent):
  def __init__(self):
    self.number = 40
    super().__init__()

instance = Child()

print(instance.number)