"""No.of combinations for n teams to play each other,  i.e. compute nCr"""


print("Enter the no of teams")
num = int(input())
print("No of combinations is", int(num*(num-1)/2))
