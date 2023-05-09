
# Unit 4
from math import *

def ftoc(temp):
    tempc = 5.0 / 9.0 * (temp - 32)
    return tempc

ftoc(98.6)

name = input("Howdy. What's yer name? \n")

print(name)

age = int(input("How old are you? "))
print("Your age is", age)
print(65 - age, "years to retirement")

gpa = float(input("What is your GPA? "))

if gpa > 3.5:
    print("You have qualified for the honor roll.")
elif gpa > 2.0:
    print("Welcome to Mars University!")
else:
    print("Your application is denied.")

x = 3
if x in range(0, 10):
    print("x is between 0 and 9")

letter = input("What is your favorite letter? ")
if letter in "aeiou":
    print("It is a vowel!")

name = "Martin Douglas Stepp"
_name_one = name.upper()
_name_two = name.lower().startswith("martin")
len(name)
print(_name_one, ",",_name_two,",", len(name))

for c in "Python":
    print(c)

x = 3; y = 3.14159; z = "hello"
print("%-8s, %04d is close to %.3f" % (z, x, y))

print(ord("a"), ord("z"))
print(chr(97), chr(200))



