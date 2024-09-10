import math
def get_area(shape):
    shape = shape.lower()
    
    if shape == "rectangle":
        rectangle_area()
    elif shape == "circle":
        circle_area()
    elif shape == "triangle":
        triangle_area()
    else:
        print("Please enter a valid shape")

def rectangle_area():
    lenght = float(input("Enter the lenght: "))
    width = float(input("Enter the width: "))

    area = lenght * width

    print("The area of the rectangle is: ", area)

def circle_area():
    radius = float(input("Enter the radius"))

    area = math.pi * (math.pow(radius, 2))

    print("The area of the circle is {:.2f}: ".format(area))

def triangle_area():
    base = float(input("Enter the base: "))
    height = float(input("Enter the height: "))

    area = 0.5 * base * height

    print("The area of the triangle is: ", area)


def main():
    shape_type = input("Get area for what shape: ")

    get_area(shape_type)

main()