from curses.ascii import islower


import re

def count_letters(string):
    return len(string)

def count_words(string):
    return len(string.split())

def count_upper_case_letters(string):
    return len(re.findall(r'[A-Z]', string))

def count_lower_case_letters(string):
    return len(re.findall(r'[a-z]', string))

def count_numbers(string):
    return len(re.findall(r'\d', string))

def reverse_string(string):
    return string[::-1]

def is_palindrome(string):
    return string == string[::-1]

def to_upper_case(string):
    return string.upper()

def to_lower_case(string):
    return string.lower()

def strip_whitespace(string):
    return string.strip()

def split_string(string):
    return string.split()

string = "The quick brown fox jumps over the lazy dog"
print("Number of letters:", count_letters(string))
print("Number of words:", count_words(string))
print("Number of uppercase letters:", count_upper_case_letters(string))
print("Number of lowercase letters:", count_lower_case_letters(string))
print("Number of numbers:", count_numbers(string))
print("Reversed string:", reverse_string(string))
print("Is palindrome:", is_palindrome(string))
print("Uppercase:", to_upper_case(string))
print("Lowercase:", to_lower_case(string))
print("Stripped whitespace:", strip_whitespace(string))
print("Split string:", split_string(string))

def thirdTask(str):
    l = 0
    u = 0
    for elem in str:
        if islower(elem):
            l += 1
        else:
            u += 1
    if l >= u:
        return str.lower()
    else:
        return str.upper()

def isUpperOrLower(str):
    k = 0
    for elem in str:
        if elem.islower():
            k -= 1
        else:
            k += 1
    if k <= 0:
        return str.lower()
    else:
        return str.upper()

def lastTask():
        while True:
            a = input("Enter first number: ")
            b = input("Enter second number: ")
            if a.isdigit() and b.isdigit():
                a = int(a)
                b = int(b)
                print("The sum is:", a + b)
                break
            else:
                print("Invalid input. Please enter only numbers.")


print(isUpperOrLower("HEllO woRLD"))

