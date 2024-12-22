class Animal:
  def __init__(self, name): # constructor
    self.name = name # instance variable unique to each instance

class Dog(Animal): # inheritance
  kind = 'canine' # class variable shared by all instances
  tricks = []
  def __str__(self) -> str: # represent when class presented as string
    return "Dog {}".format(self.name)

  def add_trick(self, trick):
    self.tricks.append(trick)

d = Dog('Fido')
d.add_trick('roll over')
d.add_trick('play dead')

print(d.kind)
print(d.name)
print(d.tricks)