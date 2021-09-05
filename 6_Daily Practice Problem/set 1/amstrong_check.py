"""Function To check Amstrong Number"""


def order(var2):
    """Function to check no of digits in a number"""
    order_n = 0
    while var2 != 0:
        order_n = order_n + 1
        var2 = var2 // 10

    return order_n


def is_armstrong(var1):
    """Fuction to check amstrong"""
    num_order = order(var1)
    temp = var1
    sum1 = 0

    while temp != 0:
        res = temp % 10
        sum1 = sum1 + pow(res, num_order)
        temp = temp // 10

    # If condition satisfies
    return sum1 == var1


# Driver code
print("Enter a number")
number = int(input())
if is_armstrong(number):
    print(number, "is a Amstrong number")
else:
    print(number, "is not a Amstrong number")
