print(f"Welcome to the Scientific name QUIZ!\n")
score = 0

#Question 1
one = str(input("What is the scientific name of ant? ")).lower()
if one == "Formicidae":
    print("Correct!")
    score += 1
    print("Incorrect! The correct answer is Formicidae.")    

#Question 2
one = str(input("What is the scientific name of hen? ")).lower()
if one == "Gallus gallus domesticus":
    print("Correct!")
    score += 1
    print("Incorrect! The correct answer is Gallus gallus domesticus.")    

#Question 3
one = str(input("What is the scientific name of horse? ")).lower()
if one == "Equus caballus":
    print("Correct!")
    score += 1
    print("Incorrect! The correct answer is Equus caballus.")    

#Question 4
one = str(input("What is the scientific name of guava? ")).lower()
if one == "Myrtaceae":
    print("Correct!")
    score += 1
    print("Incorrect! The correct answer is Myrtaceae.")    

#Question 5
one = str(input("What is the scientific name of apple? ")).lower()
if one == "Rosaceae":
    print("Correct!")
    score += 1
    print("Incorrect! The correct answer is Rosaceae.")   

# Grading
if score == 5:
    print("Congratulations! You scored 5 out of 5. Your grade is A+.") 
elif score == 4:
    print("Great! You scored 4 out of 5. Your grade is A.") 
elif score == 3:
    print(" You scored 3 out of 5. Your grade is B.")  
elif score == 2:
    print("You scored 2 out of 5. Your grade is C.")    
elif score == 1:
    print("You scored 1 out of 5. Your grade is D.")                     
else:
    print("You scored 0 out of 5. Your grade is F.")
