print("=" * 40)
print("Welcome to the Due Amount Game!")
print("=" * 40)
print("Instructions: ")
print(" - Enter the  total amount you owe.")
print(" - Enter the amount you want to pay.")
print("=" * 40)

total_amount = int(input("Enter the total amount you owe: "))
paid = int(input("Enter the amount you want to pay: "))
print("\n")

due_amount = total_amount - paid

print(f"The due amount is: {due_amount}")

