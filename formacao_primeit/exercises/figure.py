def top():
    print("    _______")
    print("  /         \\")
    print(" /           \\")

def bottom():
    print(" \\           /")
    print("  \\ _______ /")

def line():
    print("+-------------+")

def egg():
    top()
    bottom()
    print()

def cup():
    bottom()
    line()
    print()

def stop():
    top()
    print(" |    STOP   |")
    bottom()
    print()

def hat():
    top()
    line()
    print()

egg()
cup()
stop()
hat()
