#time in 24 hour format
def convert(time):
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes)
    t = hours + minutes / 60
    return t

def main():
    user_input = input("What time is it? ")
    x = convert(user_input)
    if x >= 7 and x <= 8:
        print("breakfast time")
    
    elif x >= 12 and x <= 13:
        print("lunch time")
    elif x >= 18 and x <= 19:
        print("dinner time")
if __name__ == "__main__":
    main()
