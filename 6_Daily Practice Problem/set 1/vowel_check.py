"""vowel or consonant"""

print("Enter a character")
char = input()
if len(char) == 1:
    if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
        print(char, "is a vowel")
    elif char == "A" or char == "E" or char == "I" or char == "O" or char == "U":
        print(char, "is a vowel")
    elif "A" < char <= "z":
        print(char, "is a consonant")
    else:
        print("Enter a valid input")

else:
    print("Enter a valid input")

