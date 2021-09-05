"""triangle type"""


def is_valid_triangle(side1, side2, side3):
    """valid triangle check"""
    if side1+side2 > side3 and side2+side3 > side1 and side3+side1 > side2:
        return True
    return False


def type_of_triangle(side1, side2, side3):
    """type of triangle"""
    sq1 = side1*side1
    sq2 = side2*side2
    sq3 = side3*side3
    if side1 == side2 and side2 == side3:
        print(' Equilateral triangle')
    elif side1 == side2 or side2 == side3 or side1 == side3:
        print('Isosceles Triangle')
    elif sq1 + sq2 == sq3 or sq1 + sq3 == sq2 or sq2 + sq3 == sq1:
        print('Right angled Triangle')
    else:
        print('Scalane Triangle')


side_a = float(input('Enter length of side a: '))
side_b = float(input('Enter length of side b: '))
side_c = float(input('Enter length of side c: '))

# Function call & making decision
if is_valid_triangle(side_a, side_b, side_c):
    type_of_triangle(side_a, side_b, side_c)
else:
    print('Tringle is not possible from given sides.')
