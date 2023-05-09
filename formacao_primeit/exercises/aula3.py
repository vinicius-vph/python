# Unit 3

# custom mirror
def diamond(start, stop, step, gridType):
    def grid():
        print("#" + 16 * "=" +"#")
    if gridType == "top":
        grid()
    for line in range(start, stop, step):
        print("|" +(-2 * line + 8) * " " + \
        "<>" + (2 * line - 2) * "." + \
        (2 * line - 2) * "." + "<>" + (-2 * line + 8) * " " +"|"
        )
    if gridType == "bottom":
        grid()

diamond(1,5,1,"top")
diamond(4,0,-1,"bottom")

def print_many(message, n):
    for i in range(n):
        print(message)
print_many("hello", 4)

def box(width,heigth):
    for line in range(heigth):
        if line==0:
            print("*"*width) 
        print("*"+" "*(width-2)+"*")
        if line==heigth-1:
            print("*"*width)

box(20,10)

