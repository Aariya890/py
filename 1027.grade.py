marks = int(input("Enter your grade(0-100): "))

if  80 <= marks <= 100:
    print("You got A+. Congrats!")
elif 70 <= marks <= 79:
    print("You got A.")
elif 60 <= marks <= 69:
    print("You got A-.")    
elif 50 <= marks <= 59:
    print("You got B.") 
elif 40 <= marks <= 49:
    print("You got C.") 
elif 33 <= marks <= 39:
    print("You got D.") 
elif 0 <= marks <= 32:
    print("You got F.")  

else:
    print("Invalid value input. Please input from 0 to 100.")                   