def convert(time):
    time = time.strip().lower()
    clock, period = time.split()
    t = clock.split(":")
    hour = int(t[0])
    minute = int(t[1])
    if period == "pm" and hour != 12:
        hour += 12
    elif period == "am" and hour == 12:
        hour = 0
    total_time = hour + minute / 60
    return total_time


def main():
    user_input = input("What time is it(am or pm)? ")
    x = convert(user_input)
    if 7 <= x < 8:
        print("breakfast time")
    elif 12 <= x < 13:
        print("lunch time")
    elif 18 <= x < 19:
        print("dinner time")

if __name__ == "__main__":
    main()
