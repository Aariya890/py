class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary
    def display_info(self):
        print(f"Name: {self.name}, Id: {self.emp_id}, Salary: {self.salary}")    
        
class Manager(Employee):
    def __init__(self, name, emp_id, salary, department):
        super().__init__(name, emp_id, salary)
        self.department = department
        
    def display_info(self):
        super().display_info()    
        print(f"Department: {self.department}")

class Developer(Employee):
    def __init__(self, name, emp_id, salary, programming_language):
        super().__init__(name, emp_id, salary)
        self.programming_language = programming_language 
    
    def display_info(self):
        super().display_info()    
        print(f"Programming language: {self.programming_language}")

if __name__ == "__main__":
    emp = Employee("Aariya", 101, 50000 ) 
    mgr = Manager("Arshiya", 102, 60000, "Sales" ) 
    dev = Developer("Alisha", 103, 70000, "Python")
    
    emp.display_info() 
    mgr.display_info() 
    dev.display_info()            