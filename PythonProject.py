import math

import time
timestamp = time.strftime('%H:%M:%S')
print("Don't Hurry, Its", timestamp, "You're not late")

def shape():
    print("Choose the shape you want to calculate->")
    print("1. square")
    print("2. Rectangle")
    print('3. circle')
    print("4. Triangle")
    print('5. Sphere')
    print('6. Cylinder')
    print("7. Cone")
    print("8. Cuboid")
    print("9. Cube")
    print("10. Let's have quiz")
    selection = int(input("Enter your selection -> "))

    match selection:
        case 1:
            square()
        case 2:
            rectangle()
        case 3:
            circle()
        case 4:
            triangle()
        case 5:
            sphere()
        case 6:
            cylinder()
        case 7:
            cone()
        case 8:
            cuboid()
        case 9:
            cube()
        case 10:
            Quiz()
        case _ :  
            print("Seriously !!! Are You Jocking?? -_-")

def square():
    side = float(input("Enter the side of the square: "))
    area = side * side
    perimeter = 4 * side
    print("Area of the square is: ", area)
    print("Perimeter of the square is: ", perimeter)
def rectangle():
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = length * width
    perimeter = 2 * (length + width)
    print("Area of the rectangle is: ", area)
    print("Perimeter of the rectangle is: ", perimeter)

def circle():
    radius = float(input("Enter the radius of the circle: "))
    area = math.pi * radius * radius
    circumference = 2 * math.pi * radius
    print("Area of the circle is: ", area)
    print("Circumference of the circle is: ", circumference) 
   
def triangle():
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    side1 = float(input("Enter the first side of the triangle: "))
    side2 = float(input("Enter the second side of the triangle: "))
    area = 1/2 * base * height
    perimeter = base + side1 + side2
    print("Area of the triangle is: ", area)
    print("Perimeter of the triangle is: ", perimeter)

def sphere():
    radius = float(input("Enter the radius of the sphere: "))
    volume = (4/3) * math.pi * radius * radius * radius
    surface_area = 4 * math.pi * radius * radius
    print("Volume of the sphere is: ", volume)
    print("Surface area of the sphere is: ", surface_area)

def cylinder():
    radius = float(input("Enter the radius of the cylinder: "))
    height = float(input("Enter the height of the cylinder: "))
    volume = math.pi * radius * radius * height
    total_surface_area = 2 * math.pi * radius * (radius + height)
    curved_surface_area = 2 * math.pi * radius * height
    print("Volume of the cylinder is: ", volume)
    print("Total surface area of the cylinder is: ", total_surface_area)
    print("Curved surface area of the cylinder is: ", curved_surface_area)
    
def cone():
    radius = float(input("Enter the radius of the cone: "))
    height = float(input("Enter the height of the cone: "))
    slant_height = math.sqrt(radius**2 + height**2)
    volume = (1/3) * math.pi * radius**2 * height
    surface_area = math.pi * radius * (radius + slant_height)
    print("Volume of the cone is: ", volume)
    print("Surface area of the cone is: ", surface_area)

def cuboid():
    length = float(input("Enter the length of the cuboid: "))
    width = float(input("Enter the width of the cuboid: "))
    height = float(input("Enter the height of the cuboid: "))
    volume = length * width * height
    surface_area = 2 * (length * width + width * height + height * length)
    print("Volume of the cuboid is: ", volume)
    print("Surface area of the cuboid is: ", surface_area)

def cube():
    side = float(input("Enter the side length of the cube: "))
    volume = side ** 3
    surface_area = 6 * side ** 2
    print("Volume of the cube is: ", volume)
    print("Surface area of the cube is: ", surface_area)

def Quiz():
    start_time = time.time()
    
    print("Welcome to the Quiz :)\n")
    print("Complete the quiz within 30  minutes!")
    print('Your time starts now...')
    score = 0

    print("Question 1: What is the formula for the area of a rectangle?\n")
    print("a. length x width")
    print("b. 2 x (length + width)")
    print("c. length x width x height")
    print("d. (length + width) / 2")
    answer = input("Enter your answer: ")
    if answer.lower() == "a":
        score += 5
        print("Correct!")
    else:
        print("Incorrect. The correct answer is a) length x width.")

    print("Question 2: What is the perimeter of a square with side length 5 cm?\n")
    print("a. 10 cm")
    print("b. 15 cm")
    print("c. 20 cm")
    print("d. 25 cm")
    answer = input("Enter your answer: ")
    if answer.lower() == "c":
        score += 5
        print("Correct!")
    else:
        print("Incorrect. The correct answer is c) 20 cm.")

    print("Question 3: What is the formula for the area of a circle?\n")
    print("a. πr^2")
    print("b. 2πr")
    print("c. πr")
    print("d. 2r")
    answer = input("Enter your answer: ")
    if answer.lower() == "a":
        score += 5
        print("Correct!")
    else:
        print("Incorrect. The correct answer is a) πr^2.")

    print("Question 4: What is the perimeter of a triangle with sides 3 cm, 4 cm, and 5 cm?\n")
    print("a. 6 cm")
    print("b. 8 cm")
    print("c. 10 cm")
    print("d. 12 cm")
    answer = input("Enter your answer: ")
    if answer.lower() == "d":
        score += 5
        print("Correct!")
    else:
        print("Incorrect. The correct answer is d) 12 cm.")

    print("Question 5: What is the formula for the area of a parallelogram?\n")
    print("a. base x height")
    print("b. 2 x (base + height)")
    print("c. base x height x slant height")
    print("d. (base + height) / 2")
    answer = input("Enter your answer: ")
    if answer.lower() == "a":
        score += 5
        print("Correct!")
    else:
        print("Incorrect. The correct answer is a) base x height.")

    print("Question 6: What is the perimeter of a rectangle with length 8 cm and width 4 cm?\n")
    print("a. 16 cm")
    print("b. 20 cm")
    print("c. 24 cm")
    print("d. 32 cm")
    answer = input("Enter your answer: ")
    if answer.lower() == "c":
        score += 5
        print("Correct!")
    else:
        print("Incorrect. The correct answer is c) 24 cm.")

    print("Question 7: What is the formula for the circumference of a circle?\n")
    print("a. πr^2")
    print("b. 2πr")
    print("c. πr")
    print("d. 2r")
    answer = input("Enter your answer: ")
    if answer.lower() == "b":
        score += 5
        print("Correct!")
    else:
        print("Incorrect. The correct answer is b) 2πr.")

    print("Question 8: What is the area of a triangle with base 6 cm and height 8 cm?\n")
    print("a. 12 cm²")
    print("b. 24 cm²")
    print("c. 28 cm²")
    print("d. 48 cm²")
    answer = input("Enter your answer: ")
    if answer.lower() == "b":
        score += 5
        print("Correct!")
    else:
        print("Incorrect. The correct answer is b) 24 cm².")

    print(f"\nYour final score is {score} out of 40.")
    
    if score < 10:
        print("Learn Formulas for better score")
    elif 10 <= score < 30:
        print("Can be improved!")
    else:
        print("Great! keep it up")
    
    
if __name__ == "__main__":
    shape()