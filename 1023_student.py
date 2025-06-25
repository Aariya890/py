students = {}

def display_menu():
    print("\n===================Student Management System======================")
    print("1. Add students")
    print("2. Display all students")

def add_students():
    studentId = input("Enter student Id: ") 
    if studentId in students:
        print("Student already exists.")   
        return
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    grade = int(input("Enter student grade: "))
    try:
        marks = float(input("Enter student marks: "))
    except ValueError:
        print("Invalid marks input.")
    students[studentId] = {
        "name": name,
        "age" : age,
        "grade" : grade,
        "marks" : marks
    }    
    print("\nStudent updates succesfully!")

def display_students():
    if not students:
        print("No records to display.")
        return
    print("\n All student records: ")     
    
    for sid, info in students.items():
        print(f"Student Id: {sid}")
        for key, value in info.items():
            print(f"{key.capitalize()}: {value}")

def main():
    while True:
        display_menu()
        choice = int(input("Enter your choice(1-2): "))    
        if choice == 1:
            add_students()
        elif choice == 2:
            display_students()    
        else:
            print("Invalid value! Please enter from 1 to 2.")  

if __name__ == "__main__":
    main()             