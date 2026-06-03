import sys
import random
import pyfiglet

def main():
    user_input = input("Input: ")
    figlet = pyfiglet.Figlet()
    fonts = figlet.getFonts()

    if len(sys.argv) == 1:
        font = random.choice(fonts)
    elif len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"]:
        font = sys.argv[2]
        if font not in fonts:
            sys.exit("Invalid font")
    else:
        sys.exit("Invalid usage")

    figlet = pyfiglet.Figlet(font=font)
    output = figlet.renderText(user_input)
    print(output)

if __name__ == "__main__":
    main()