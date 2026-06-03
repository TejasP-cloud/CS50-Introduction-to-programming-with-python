import re

def main():

    print(validate(input("IPv4 Address: ")))


def validate(ip):
    match = re.fullmatch(r"(\d+)\.(\d+)\.(\d+)\.(\d+)", ip)
    
    if match:
        for i in range(1, 5):
            if not 0 <= int(match.group(i)) <=255:
                return False
        return True
    else:
        return False



if __name__ == "__main__":
    main()