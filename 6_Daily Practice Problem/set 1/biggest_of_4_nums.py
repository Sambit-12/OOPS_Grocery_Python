"""Calculator to calculate biggest of four numbers"""
print("This is a calculator to find biggest of four numbers")
print("----------------------------------------------------")
print("Enter four numbers")

num = list(map(float, input().strip().split()))

print("Biggest of four numbers is", max(num))
