def convert(sentence):
    sentence = sentence.replace(":)", "🙂")
    sentence = sentence.replace(":(", "🙁")
    return sentence

def main():
    user1 = input("Enter a sentence: ")
    print(convert(user1))

    user2 = input("Enter a sentence: ")
    print(convert(user2))

    user3 = input("Enter a sentence: ")
    print(convert(user3))

main()