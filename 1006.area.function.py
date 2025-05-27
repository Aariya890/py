def area_of_square(side):
    area = side ** 2
    return area

def area_of_rectangle(w, l):
    area = w * l
    return area

def area_of_circle(r):
    area = 3.14 * r ** 2
    return area

def area_of_triangle(b, h):
    area = (b * h) / 2
    return area

print("--------------------------------------------")
print("-------------Area Calculator----------------")
print("--------------------------------------------")   

print("Choose a shape to calculate the area:")
print("1. Square")
print("2. Rectangle")
print("3. Circle")
print("4. Triangle")

choice = int(input("Enter your choice: "))

if choice == 1:
    side = float(input("Enter the length of the side of the square: "))
    area = area_of_square(side)
    print(f"The area of the square is: {area:0.2f}")
    
if choice == 2:
    l = float(input("Enter the length of the rectangle: "))
    w = float(input("Enter the width of the rectangle: "))
    area = area_of_rectangle(w, l)
    print(f"The area of the rectangle is: {area:0.2f}")
    
if choice == 3:
    side = float(input("Enter the length of the side of the square: "))
    area = area_of_circle(r)
    print(f"The area of the square is: {area:0.2f}")
    
if choice == 4:
    side = float(input("Enter the length of the side of the square: "))
    area = area_of_square(side)
    print(f"The area of the square is: {area:0.2f}")            
    