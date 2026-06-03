VOWELS = ["a", "e", "i", "o", "u"]

def shorten(word):
    newword = ""
    for letter in word:
        if letter.lower() in VOWELS:
            letter = ""
        newword += letter
    return newword

def main():
    for _ in range(3):
        user_input = input("Input: ").strip()
        print("Output:", shorten(user_input))
    
if __name__ == "__main__":
    main()