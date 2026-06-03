import random
import sys

def main():
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            print("Invalid input")
            continue
        except EOFError:
            sys.exit("Exiting program.")
        if level < 1:
            print("Invalid input")
            continue
        else:
            break
    
    #random number
    random_num = random.randint(1, level)

    #guessing number
    while True:
        try:
            guess = int(input("Guess a number: "))
        except ValueError:
            print("Invalid input")
            continue
        if guess < 1:
            print("Invalid input")
            continue
        if guess > random_num:
            print("Too large")
            continue
        elif guess < random_num:
            print("Too small")
            continue
        else:
            print("just right")
            break
            
    

if __name__ == "__main__":
    main()