"""Python program to find H.C.F of two numbers"""


def compute_hcf(var1, var2):
    """hcf calculator function"""
    if var1 > var2:
        smaller = var2
    else:
        smaller = var1
    for var_i in range(1, smaller+1):
        if (var1 % var_i == 0) and (var2 % var_i == 0):
            hcf = var_i
    return hcf


print("Enter two numbers")
num = list(map(int, input().strip().split()))

print("The H.C.F. is", compute_hcf(num[0], num[1]))
