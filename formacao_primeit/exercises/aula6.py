# Unit 6
file_demo = open("./demofile.txt")

print(file_demo.read())
print(file_demo.readline())
print(file_demo.readlines())

document = open("./hours.txt")

for lines in document:
    print(lines.strip())


file_py = open("./file_py.py", "w")
file_py.write('file_py = open("file_py.txt", "w")\n')
file_py.write('file_py.write("Hello, world!\\n")\n')
file_py.write('file_py.write(r"How Are you?\n")\n')
file_py.write('file_py.close()\n')
file_py.write('print(open("./file_py.txt").read())')
file_py.close()

# Unit 7
scores = [9, 14, 18, 19, 16]
counts = [0] * 4

print(scores[0] + scores[4])
print(counts)
print(scores[3])
print(scores[-3])
print(scores[2:5])
print(scores[3:])
print(scores[:3])
print(scores[-3:])

file_hours = open("hours")

# Search word? part
imdb_file = open("imdb.txt")

for rows in imdb_file:
    tokens = rows.split()
    rank = int(tokens[0])
    votes = int(tokens[1])
    rating = float(tokens[2])
    title = " ".join(tokens[3:])
    print(str(rank)+str(votes)+str(rating)+title)

