import inflect
from emojize import get_input

p = inflect.engine()

def main():
    names = []
    while True:
        try:
            name = get_input()
            names.append(name)
            

        except EOFError:
            print()
            print("Adieu, adieu to", p.join(names))
            break

    

if __name__ == "__main__":
    main()