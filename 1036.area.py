import random  

def main():
        print("\nChoose an operation: ")
        print("1. Area of Circle ")
        print("2. Area of Triangle")
        print("3. Area of Rectangle ")
        print("4. Exit ")
        print("==========================")
        
        choice = input("Enter your choice(1-4): ")
       
        if choice == '1':
            r = float(input("Enter the radius: ") )
            print("Area: ", (3.14*r)**2)
        elif choice == '2':
            b = float(input("Enter the base: ")) 
            h = float(input("Enter the height: ")) 
            print("Area: ", (b*h)/2)
        elif choice == '3':
            l = float(input("Enter the length: ") )
            w = float(input("Enter the width: ") )
            print("Area: ", l*w)
        elif choice == '4':
            print("Exiting...")
            print("Thanks for playing!")    
      
        else:
            print("Invalid choice. Please enter from 1 to 4.")
    
if __name__ == "__main__" :
    main()                
            