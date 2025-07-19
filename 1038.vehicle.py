class Vehicle:
    def __init__(self, name, veh_id, salary):
        self.name = name
        self.emp_id = veh_id
        self.salary = salary
    def display_info(self):
        print(f"Name: {self.name}, Id: {self.emp_id}, Salary: {self.salary}")    
        
class Driver(Vehicle):
    def __init__(self, name, veh_id, salary, brand):
        super().__init__(name, veh_id, salary)
        self.brand = brand
        
    def display_info(self):
        super().display_info()    
        print(f"Brand: {self.brand}")
        
if __name__ == "__main__":
    veh = Vehicle("Bus", 101, 50000 ) 
    dri = Driver("Arshiya", 102, 60000, "Toyota" ) 
    
    
    veh.display_info() 
    dri.display_info() 
            