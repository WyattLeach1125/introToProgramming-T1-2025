
x = float(input("Insert a number for x: "))
y = float(input("Insert a number for y: "))


def add(x, y):
    print(x + y)

def subtract(x, y):
    print(x - y)

def multiply(x, y):
    print(x * y)

def divide(x, y):
    print(x / y)

def exponent(x, y):
    print("exponent of x:", x * x)
    print("exponent of y:", y * y)

def modulus(x, y):
    print("x devided by y has a remainder of:", x % y)

def floor_division(x, y):
    print(x // y)

add(x, y)
subtract(x, y)
multiply(x, y)
divide(x, y)
exponent(x, y)
modulus(x, y)
floor_division(x, y)
