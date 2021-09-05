"""arithmetic operation"""

print("Enter operator")
print("1 for addition")
print("2 for subtraction")
print("3 for multiplication")
print("4 for division")
op = int(input())
print("Enter 1st number")
num1 = int(input())
print("Enter 2nd number")
num2 = int(input())
if op == 1:
    print(num1, "+", num2, "=", num1 + num2)
elif op == 2:
    print(num1, "-", num2, "=", num1 - num2)
elif op == 3:
    print(num1, "*", num2, "=", num1 * num2)
elif op == 4:
    print(num1, "/", num2, "=", num1 / num2)
else:
    print("Enter valid inputs")
