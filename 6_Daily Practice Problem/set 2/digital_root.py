"""digital root"""


print("Enter a positive number")
num = int(input())
print("Digital root of", num, "is", num % 9 or 9)
