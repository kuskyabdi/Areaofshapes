pi = 3.142

# Get user input
user_input = input("Which shape area would you like to calculate?\n(circle, square, rectangle, triangle)\n").lower()

# Calculate area based on user input
if user_input == "circle":
    radius = float(input("Please enter the radius of the circle:\n"))
    area = pi * (radius ** 2)
    print(f"The area of the circle is {area:.2f}")
elif user_input == "square":
    length = float(input("Enter the length of the square:\n"))
    area = length ** 2
    print(f"The area of the square is {area:.2f}")
elif user_input == "rectangle":
    height = float(input("Enter the height of the rectangle:\n"))
    width = float(input("Enter the width of the rectangle:\n"))
    area = height * width
    print(f"The area of the rectangle is {area:.2f}")
elif user_input == "triangle":
    height = float(input("Enter the height of the triangle:\n"))
    base = float(input("Enter the base of the triangle:\n"))
    area = 0.5 * height * base
    print(f"The area of the triangle is {area:.2f}")
else:
    print("Invalid input. Please choose from circle, square, rectangle, or triangle.")

