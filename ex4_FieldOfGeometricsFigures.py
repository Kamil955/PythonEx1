geometric_figures = ['triangle', 'circle', 'rectangle']
print ("Hello there! I am a field of geometric figures. I will help you calculate the area of the figure you want.")
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("I can calculate the area of the following figures: ", geometric_figures)
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
input_figure = input("Enter the name of the figure which area you want to count: ")

if input_figure == 'triangle':
    base = input("Enter the base of the triangle: ")
    height = input("Enter the height of the triangle: ")
    area = int(base) * int(height) / 2
    print("The area of the triangle is", area)
elif input_figure == 'circle':
    radius = input("Enter the radius of the circle: ")
    area = 3.14 * int(radius) ** 2
    print("The area of the circle is", area)

elif input_figure == 'rectangle':
    width = input("Enter the width of the rectangle: ")
    length = input("Enter the length of the rectangle: ")
    area = int(width) * int(length)
    print("The area of the rectangle is", area)
