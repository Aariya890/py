print("====================================")
print("        BMI Calculator")
print("====================================")

w = float(input("Enter your Weight(kg): "))
h = float(input("Enter your height(m): "))

bmi = w / h**2

print("BMI: ", bmi)

if bmi < 18.5:
    print("You are underweight. Try to gain weight.")
elif 18.5 <= bmi <= 24.9:
    print("You are in normal weight. Keep it up!")    
elif 25 <= bmi <= 29.9:
    print("You are overweight.")    
elif 30 <= bmi <= 34.9:
    print("You are obese.")   
elif bmi > 35:
    print("You are extremely obese.")     