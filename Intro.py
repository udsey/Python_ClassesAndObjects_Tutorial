#help(int) - to call help of class

class Cat(object):
    def __init__(self, name): #constructor method
        self.name = name # atribute of class
        
    def speak(self): # method
        print(f'Hi, my name is {self.name}')

    def add_age(self, age):
        self.age = age
    
tim = Cat('Tim') # call __init__
tim.speak()
bob = Cat('Bob') #instance of class
bob.speak()
print(bob.name)
tim.add_age(2)
print(tim.age)
print(bob.age)