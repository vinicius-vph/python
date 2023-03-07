# String Multiplication
"hello" * 3
print(10 * "yo ")

# String Concatenation
x = 4
print("Thou shalt not count to " + str(x) + ".")
print(x + 1, "is out of the question.")

# Expressions
x=1
y=5
z=9

a = z+x*y/2-4
b = (z+x)*(y/2)-4
c = z+(x*y)/(2-4)

print(a)
print(b)
print(c)

# The for Loop
def loop_generator(max):  
    for i in range(max):
        print(i)

def loop_generator2(min, max):  
    for i in range(min, max):
        print(i)

def loop_generator3(min, max, step):  
    for i in range(min, max, step):
        print(i)

def loop_generator4(min, max, step):
    for line in range(min, max, step):
        print((5 - line) * "." + str(line))

loop_generator(5)
loop_generator2(-1,5)
loop_generator3(2,8,2)
loop_generator4(2,20,2)

# mirror
def bar():
    print("#" + 16 * "=" + "#")
def top():
    for line in range(1, 5):
        # split a long line by ending it with \
        print("|" + (-2 * line + 8) * " " + \
        "<>" + (4 * line - 4) * "." + "<>" + \
        (-2 * line + 8) * " " + "|")

def bottom():
    for line in range(4, 0, -1):
        print("|" + (-2 * line + 8) * " " + \
        "<>" + (4 * line - 4) * "." + "<>" + \
        (-2 * line + 8) * " " + "|")

# main
bar()
top()
bottom()
bar()

def pizza(start, stop, step):
    print("#" + 16 * "=" +"#")
    for line in range(start, stop, step):
        print("|" +(-2 * line + 8) * " " + \
        "<>" + (2 * line - 2) * "." + \
        (2 * line - 2) * "." + "<>" + (-2 * line + 8) * " " +"|"
        )
pizza(1,5,1)
pizza(4,0,-1)


def forinfor():
    array = []
    for it in (range(1, 5), range(10, 15)): 
        for element in it:
            array.append(element)
    print(array)
            
forinfor()
