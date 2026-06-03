import emoji
import requests
import json

def get_input():
    user_input = input("Input: ")
    return user_input

def main():
    while True:
        try:
            user_input = get_input()
            output = emoji.emojize(user_input, language="alias")
            print("Output:", output)
        except EOFError:
            print("Exiting Program")
            break
        

if __name__ == "__main__":
    main()