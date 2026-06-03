import random

def main():
    score = 0
    level = get_level()
    for _ in range(9):
        x = generate_integer(level)
        y = generate_integer(level)
        sum = x + y
        for _ in range(3):
            try:
                check_answer = int(input(f"{x} + {y} = "))
                if sum == check_answer:
                    score += 1
                    break
                else:
                    print("EEE")
            except ValueError:
                print("EEE")
            else:
                print(f"{x} + {y} = {sum}")

    print("Score: ", score) 


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level < 1 or level > 3:
                raise ValueError
            return level
        except ValueError:
            continue

        
def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    else:
        return random.randint(100, 999)

if __name__ == "__main__":
    main()