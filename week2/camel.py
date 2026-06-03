def main():
    for _ in range(2):
        camel_input = input("camelCase: ")
        print("snake_case:", camel_to_snake(camel_input))


def camel_to_snake(camel):
    snake_case = ""
    for letter in camel:
        if letter.isupper():
            snake_case += "_" + letter.lower()
        else:
            snake_case += letter
    return snake_case


if __name__ == "__main__":
    main()