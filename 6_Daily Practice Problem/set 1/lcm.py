"""Python program to find LCM of two numbers"""


def compute_lcm(var1, var2):
    """lcm calculator function"""
    if var1 < var2:
        lcm_num = var2
    else:
        lcm_num = var1
    while (lcm_num % var1 != 0) or (lcm_num % var2 != 0):
        lcm_num = lcm_num+1
    return lcm_num


print("Enter two numbers")
num = num = list(map(int, input().strip().split()))

print("The L.C.M is", compute_lcm(num[0], num[1]))
