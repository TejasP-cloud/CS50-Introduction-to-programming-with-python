def main():
    price = dollars_to_float(input("How much was the meal in dollars: "))
    percentage = percentage_to_float(input("What percentage would you like to tip: "))
    tip = price * percentage
    print(f"Leave ${tip:.2f} as a tip.")

def dollars_to_float(dollars):
    dollars = dollars.replace("$", "")
    return float(dollars)

def percentage_to_float(percentage):
    percentage = percentage.replace("%", "")
    return float(percentage) / 100

main()
main()
main()