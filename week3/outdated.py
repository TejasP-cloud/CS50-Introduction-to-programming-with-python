months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def user_input():
    date = input("Date: ").strip()
    return date

def main():
    while True:
        try:
            date = user_input()
            if "/" in date:
                month, day, year = date.split("/")
                month = int(month)
                day = int(date)
                year = int(year)
            else:
                month, day, year = date.split(" ")
                day = day.replace(",", "")
                month = months.index(month) + 1
                if month > 12 or day > 31:
                    continue
            print(f"year{year:04}, month{month:02}, day{day:02}")
            break
        except ValueError:
            pass
   
    
if __name__ == "__main__":
    main()



