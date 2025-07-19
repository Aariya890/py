leap = int(input("Enter the year(e.g. 2025): "))

if leap % 400 == 0:
    print("It is a leap year.")
elif leap % 100 == 0:
    print("It is not a leap year.")   
elif leap % 4 == 0:
    print("It is a leap year.")  
else:
    print("It is not a leap year.")       
    