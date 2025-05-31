TAX_RATE = 0.10

books = {
    "History": 300.00,
    "Fairy tales" : 300.00,
    "Science fiction" : 300.00,
    "Literature" : 300.00,
    "Graphic nobel" : 300.00,
    "Poetry" : 300.00,
    "Cookbooks" : 300.00,
    "Encyclopedia" : 300.00,
    "Biography" : 300.00,
}

order = {}

def take_order():

    while True:
        item = input("Enter the item you want to borrow (or type 'done' to finish): ").strip()
        if item == 'done':
            break
        if item in books:
            quantity = int(input(f"How many {item}s would you like to borrow? "))
            if item in order:
                order[item] += quantity
            else:
                order[item] = quantity
        else:
            print("Sorry, we don't have that book.")
    
def calculate_total(): 
    total = 0.0
    for item, quantity in order.items():
        total += books[item] * quantity
    tax = total * TAX_RATE
    total_with_tax = total + tax
    return total, tax, total_with_tax 

def print_bill():
    print("\n--- Bill Summary ---")
    total, tax, total_with_tax = calculate_total()
    for item, quantity in order.items():
        print(f"{item.title()} x {quantity} = Rs. {books[item] * quantity:.2f}")
    print(f"Subtotal: Rs. {total:.2f}")
    print(f"Tax (10%): Rs. {tax:.2f}") 
    print(f"Total Amount: Rs. {total_with_tax:.2f}")   
    
    

def show_books():
    print("\nBooks:")
    for item, price in books.items():
        print(f"{item}: Rs. {price:.2f}")
        
if __name__ == "__main__":
    show_books()
    take_order()
    print_bill()
    print("\nThank you for borrowing the books!")