"""delete smallest digit of a 4 digit num"""
n= 10 # len of num
print("Enter a number")
num = input()
num_list = []
for i in range (n):
    num_list.append(int(num[i]))
num_list.remove(min(num_list))
print("Number after removing smallest digit is ", end="")
for i in range(0,n-1):
    print(num_list[i], end="")
##print(100*int(num_list[0]) + 10*int(num_list[1]) + int(num_list[2]))
