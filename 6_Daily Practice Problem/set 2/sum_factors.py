"""sum of factors of a number"""


print("Enter a positive number")
num = int(input())
SUM_FACT = 0
for it in range(1, num+1):
    if num % it == 0:
        SUM_FACT += it
print("Sum of factors is", SUM_FACT)
