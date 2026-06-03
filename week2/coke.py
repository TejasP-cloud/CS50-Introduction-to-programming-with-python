COKE_PRICE = 50
VALID_COINS = [5, 10, 25]


def display_welcome():
    print("=== Coke Machine ===")
    print("Accepted coins: 5, 10, 25")
    print("Press Q anytime to quit\n")


def display_amount_due(amount_due):
    print(f"Amount Due: {amount_due}")


def get_coin():
    coin = input("Insert Coin: ").strip().lower()
    return coin


def is_quit_command(user_input):
    return user_input == "q"


def is_number(user_input):
    return user_input.isdigit()


def convert_to_integer(user_input):
    return int(user_input)


def is_valid_coin(coin):
    return coin in VALID_COINS


def process_coin(amount_due, coin):
    return amount_due - coin


def calculate_change(amount_due):
    if amount_due < 0:
        return abs(amount_due)

    return 0


def display_invalid_message():
    print("Invalid coin. Try again.\n")


def display_goodbye():
    print("\nTransaction cancelled.")
    print("Goodbye!")


def display_change(change):
    print(f"\nChange Owed: {change}")


def main():
    amount_due = COKE_PRICE

    display_welcome()

    while amount_due > 0:
        display_amount_due(amount_due)

        user_input = get_coin()

        if is_quit_command(user_input):
            display_goodbye()
            return

        if not is_number(user_input):
            display_invalid_message()
            continue

        coin = convert_to_integer(user_input)

        if is_valid_coin(coin):
            amount_due = process_coin(amount_due, coin)
        else:
            display_invalid_message()

    change = calculate_change(amount_due)

    display_change(change)


if __name__ == "__main__":
    main()