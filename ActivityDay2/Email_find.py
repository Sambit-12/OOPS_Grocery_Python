from os import lstat
import re
s = open("Employee.txt",'r',encoding='utf-8')
contents = s.read()
lst = re.findall('[^,;\s]+@[^,;\s]+',contents)
print(lst)