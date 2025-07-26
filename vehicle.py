from abc import ABC, abstractmethod
class Vehicle(ABC):
    def wheels(self):
        pass

class Car(Vehicle):
    
    def wheels(self):
        print("I have four wheels.")

class Rickshaw(Vehicle):
    
    def wheels(self):
        print("\nI have three wheels.")

class Bicycle(Vehicle):
    
    def wheels(self):
        print("\nI have two wheels.") 
        
class Truck(Vehicle):
    
    def wheels(self):
        print("\nI have four wheels.")

R = Car()
R.wheels()         
       
K = Rickshaw() 
K.wheels()

R = Bicycle()
R.wheels()

K = Truck()
K.wheels()         
         