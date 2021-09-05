""" finding quadrant of a point"""


def find_quadrant(x_val, y_val):
    """quadrant check"""
    if x_val == 0 and y_val == 0:
        print("Point is on the origin")
    elif x_val == 0:
        print("Point is on Y axis")
    elif y_val == 0:
        print("Point is on X axis")
    elif x_val > 0 and y_val > 0:
        print("Point is in 1st Quadrant")
    elif x_val < 0 and y_val > 0:
        print("Point is in 2nd Quadrant")
    elif x_val < 0 and y_val < 0:
        print("Point is in 3rd Quadrant")
    elif x_val > 0 and y_val < 0:
        print("Point is in 4th Quadrant")
    return 0


print("Enter the value of X")
x_val_i = float(input())
print("Enter the value of Y")
y_val_i = float(input())

find_quadrant(x_val_i, y_val_i)
