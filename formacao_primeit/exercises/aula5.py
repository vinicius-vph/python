# range from 'a' to 'z
def character_range(char1, char2):
    for char in range(ord(char1), ord(char2) + 1):
        yield (char)


for letter in character_range('a', 'z'):
    print(chr(letter), end=', ')



f = open("demofile.txt", "r")
print(f.read())
print(f.readline())

for x in f:
  print(x)


import random
import os

letters=('John','Doe','Jane')
numbers=('1','2','3','4','5','6','7','8','9','10')

file_name="".join(random.choice(letters)+random.choice(numbers))+".txt"

f = open(file_name, "w")
f.write("Woops! I have deleted the content!")
f.close()

print(file_name)

y = open(file_name, "r")
for z in y:
  print(z)

y.close()
os.remove(file_name)


hours_file = open("hours.txt")
rows = hours_file.readlines()
print(rows)
