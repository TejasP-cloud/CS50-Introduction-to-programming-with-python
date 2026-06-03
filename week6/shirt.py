import sys
from PIL import Image, ImageOps

def main():
    valid_commandline()
    with Image.open(sys.argv[1]) as input_image:
        shirt = Image.open("shirt.png")
        input_fitted = ImageOps.fit(input_image, shirt.size)
        input_fitted.paste(shirt, mask=shirt)
        input_fitted.save(sys.argv[2])
    


def valid_commandline():
    allowed = ("jpg", "jpeg", "png")
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].lower().endswith(allowed) or not sys.argv[2].lower().endswith(allowed):
        sys.exit("Image not found")
    elif sys.argv[1].split(".")[-1] != sys.argv[2].split(".")[-1]:
        sys.exit("Image extensions should be same.")


if __name__ == "__main__":
    main()