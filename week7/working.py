import re

def main():
    print(convert(input("Hours: ")))


def convert(s):
    matches = re.findall(r"(\d{1,2})(?::(\d{2}))?\s*(AM|PM)", s, re.IGNORECASE)

    # extract start time
    start_hour   = int(matches[0][0])
    start_min    = matches[0][1] if matches[0][1] != "" else "00"
    start_period = matches[0][2].upper()

    # extract end time
    end_hour   = int(matches[1][0])
    end_min    = matches[1][1] if matches[1][1] != "" else "00"
    end_period = matches[1][2].upper()

    # convert both
    start_hour = convert_time(start_hour, start_period)
    end_hour   = convert_time(end_hour, end_period)

    return f"{start_hour:02}:{start_min} to {end_hour:02}:{end_min}"


def convert_time(hour, period):
    if period == "AM":
        if hour == 12:
            return 0       # 12 AM → 0
        else:
            return hour    # 1-11 AM → stays same

    if period == "PM":
        if hour == 12:
            return 12      # 12 PM → stays 12
        else:
            return hour + 12   # 1-11 PM → add 12


if __name__ == "__main__":
    main()