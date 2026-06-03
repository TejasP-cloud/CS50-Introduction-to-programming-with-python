def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def main():
    x, y, z = input("enter a number, one operation and another number: ").split()
    if y == "+":
        num = add(float(x), float(z))
        print(f"{num:.1f}")
    elif y == "-":
        num = subtract(float(x), float(z))
        print(f"{num:.1f}")
    elif y == "*":
        num = multiply(float(x), float(z))
        print(f"{num:.1f}")
    elif y == "/":
        num = divide(float(x), float(z))
        print(f"{num:.1f}")
    else:
        print("Error: Invalid operation")

main()
