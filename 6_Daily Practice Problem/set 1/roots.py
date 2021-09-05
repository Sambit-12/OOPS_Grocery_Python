"""roots of quadratic equation"""
import cmath

print("Quadratic Equation is ax2 + bx +c = 0")
a_val = float(input('Enter the value of a: '))
b_val = float(input('Enter the value of b: '))
c_val = float(input('Enter the value of c: '))


dis = (b_val ** 2) - (4 * a_val * c_val)

root1 = (-b_val - cmath.sqrt(dis)) / (2 * a_val)
root2 = (-b_val + cmath.sqrt(dis)) / (2 * a_val)

# printing the results
print('The roots are', root1, "and", root2)
