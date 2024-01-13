class Dog:
    
    dogs = [] # class variable # for the entier class not only for instance
    
    def __init__(self, name):
        self.name = name
        self.dogs.append(self)
        
    @classmethod # decoraters
    def num_dogs(cls):
        return len(cls.dogs)
    
    @staticmethod # work without instance
    def bark(n):
        for _ in range(n):
            print("Bark!")
            
print(Dog.num_dogs())
print(Dog.bark(3))           
tim = Dog('Tim')
jim = Dog('Jim')

print(Dog.dogs)



