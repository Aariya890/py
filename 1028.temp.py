print("==========Temperature Converter=========")
print("Choose from the options: ")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
print("========================================")

option = input("\nNow enter any one option: ")

if option == '1':
    celsius = int(input("Enter the celsius: "))
    F = (celsius * 9/5) +32
    print("Fahrenheit: ", F)
elif option == '2':
    fahren = int(input("Enter the Fahrenheit: "))
    C = (fahren - 32) * 5/9 
    print("Celsius: ", C)   
else:
    print("Invalid value.")     