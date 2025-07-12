class Dog:
    def __init__(self, name, age, breeds):
        self.name = name
        self.age = age
        self.breeds = breeds
    
    def average_grade(self):
        return sum(self.breeds) / len(self.breeds) if self.breeds else 0  
    
    def add_grade(self, breed):
        self.breeds.append(breed)
        
    def __str__(self):
        return f"Dog(name = {self.name}, age = {self.age}, breeds = {self.breeds} )" 

dogs = [
    Dog("Poodle", 24, [45, 33, 21]) ,
    Dog("Sparkle", 92, [19, 53, 20]) , 
    Dog("Snowy", 67, [88, 40, 72])    
]       

for dog in dogs:
    print(dog)
    print(f"Average Grade: {dog.average_grade(): .2f}")

dogs[0].add_grade(100)
print("\nAfter adding a new grade to Alice: ")
print(dogs[0])
print(f"New average grade: {dogs[0].average_grade(): .2f}")    