"""code to find the odd man out of a list"""

arr = [4, 4, 4, 4, 4, 4, 4, 4, "a"]
print("array is", arr)
ele_count = {}
for ele in arr:
    if ele in ele_count:
        ele_count[ele] += 1
    else:
        # setting the count to 1
        ele_count[ele] = 1
# printing the elements frequencies
for key, value in ele_count.items():
    if value == 1:
        print("odd element is ", key)
