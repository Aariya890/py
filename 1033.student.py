class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades
    
    def average_grade(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0  
    
    def add_grade(self, grade):
        self.grades.append(grade)
        
    def __str__(self):
        return f"Student(name = {self.name}, age = {self.age}, grades = {self.grades} )" 

students = [
    Student("Aariya", 24, [45, 33, 21]) ,
    Student("Mihrima", 92, [19, 53, 20]) , 
    Student("Fariha", 67, [88, 40, 72])    
]       

for student in students:
    print(student)
    print(f"Average Grade: {student.average_grade(): .2f}")

students[0].add_grade(100)
print("\nAfter adding a new grade to Alice: ")
print(students[0])
print(f"New average grade: {students[0].average_grade(): .2f}")    