TAX_RATE = 0.10

menu = {
    "burger": 70.00,
    "pizza" : 300.00,
    "Fried chicken" : 90.00,
    "Fries" : 50.00,
    "Pasta" : 100.00,
    "Ice-cream" : 250.00,
    "Caramel pudding" : 250.00,
    "Shawarma" : 100.00,
    "Dounut" : 70.00,
    "Sushi" : 350.00,
}

order = {}

def take_order():

    while True:
        item = input("Enter the item you want to order (or type 'done' to finish): ").strip()
        if item == 'done':
            break
        if item in menu:
            quantity = int(input(f"How many {item}s would you like to order? "))
            if item in order:
                order[item] += quantity
            else:
                order[item] = quantity
        else:
            print("Sorry, we don't have that item.")
    
def calculate_total(): 
    total = 0.0
    for item, quantity in order.items():
        total += menu[item] * quantity
    tax = total * TAX_RATE
    total_with_tax = total + tax
    return total, tax, total_with_tax 

def print_bill():
    print("\n--- Bill Summary ---")
    total, tax, total_with_tax = calculate_total()
    for item, quantity in order.items():
        print(f"{item.title()} x {quantity} = Rs. {menu[item] * quantity:.2f}")
    print(f"Subtotal: Rs. {total:.2f}")
    print(f"Tax (10%): Rs. {tax:.2f}") 
    print(f"Total Amount: Rs. {total_with_tax:.2f}")   
    
    

def show_menu():
    print("\nMenu:")
    for item, price in menu.items():
        print(f"{item}: Rs. {price:.2f}")
        
if __name__ == "__main__":
    show_menu()
    take_order()
    print_bill()
    print("\nThank you for dining with us!")