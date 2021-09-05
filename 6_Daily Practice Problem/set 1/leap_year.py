"""leap year check"""


def is_leap(year):
    """leap check"""
    if year < 0:
        return -1
    return year % 400 == 0 or year % 4 == 0 and year % 100 != 0


print("Enter the year to be checked for leap year")
year_i = int(input())

if is_leap(year_i)== -1:
    print("Enter a valid year")
elif is_leap(year_i):
    print("It is a leap year")
elif not is_leap(year_i):
    print("It is not a leap year")
