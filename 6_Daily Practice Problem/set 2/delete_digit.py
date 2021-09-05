"""delete smallest digit of a 4 digit num"""

print("Enter a 4 digit number")
num = input()
num_list = [num[0], num[1], num[2], num[3]]
num_list.remove(min(num_list))
print("Number after removing smallest digit is", end="")
print(100*int(num_list[0]) + 10*int(num_list[1]) + int(num_list[2]))
