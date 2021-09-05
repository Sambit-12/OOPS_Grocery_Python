"""no of primes in range n"""

print("Enter a positive number")
num = int(input())
TOTAL = 0
for it in range(2, num + 1):
    for jt in range(2, it):
        if it % jt == 0:
            break
    else:
        TOTAL += 1
print("No of prime numbers in range", num, "is", TOTAL)
