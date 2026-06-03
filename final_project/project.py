def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("  Invalid! Please enter a number.\n")


def get_operator():
    valid = ["+", "-", "*", "/"]
    while True:
        op = input("Enter operator (+, -, *, /): ").strip()
        if op in valid:
            return op
        print("  Invalid! Choose from: + - * /\n")


def calculate(num1, num2, op):
    match op:
        case "+": return num1 + num2
        case "-": return num1 - num2
        case "*": return num1 * num2
        case "/":
            if num2 == 0:
                print("  Error: Cannot divide by zero.\n")
                return None
            return num1 / num2


def main():
    print("==============================")
    print("       Python Calculator      ")
    print("==============================\n")

    while True:
        num1   = get_number("Enter first number:  ")
        num2   = get_number("Enter second number: ")
        op     = get_operator()
        result = calculate(num1, num2, op)

        if result is not None:
            print(f"\n  {num1} {op} {num2} = {result}\n")

        again = input("Calculate again? (y/n): ").strip().lower()
        if again != "y":
            print("\nGoodbye!")
            break
        print()


if __name__ == "__main__":
    main()