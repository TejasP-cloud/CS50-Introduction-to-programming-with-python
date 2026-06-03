MENU = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 10.00,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total = 0

def user_input():
    try:
        item = input("Item:").strip().title()
        return item
    except (EOFError, KeyboardInterrupt):
        print("\nExiting program.")
        return None


def calculate_price(item):
    global total
    if item in MENU:
        total += MENU[item]
        print(f"Total: ${total:.2f}")


def main():     
    while True:
        item = user_input()
        if item is None:
            break
        calculate_price(item)

if __name__ == "__main__":
    main()