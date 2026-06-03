
def is_True(value):
    value = value.lower().strip()
    value = " ".join(value.split())
    match value:
        case "42" | "forty-two" | "forty two":
            return True
        case _:
            return False        

def main():
    solution = input("What is the answer to the Ultimate Question of Life, The Universe, and Everything? ")
    if is_True(solution):
        print("Yes")
    else:
        print("No")

main()
