from datetime import date
import sys
import inflect

def main():
    p = inflect.engine()
    dob = get_birthday()
    minutes = convert_to_minutes(dob)
    words = p.number_to_words(minutes, andword="")
    print(words.capitalize() + " minutes")



def get_birthday():
    try:
        birthday = input("Enter of date of birth: ")
        birthday = date.fromisoformat(birthday)
        return birthday
    except ValueError:
        sys.exit("Invalid date of birth format.")

def convert_to_minutes(dob):
    today = date.today()
    return (today - dob).days * 24 * 60
    


if __name__ == "__main__":
    main()