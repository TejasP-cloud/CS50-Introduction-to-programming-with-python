def main():
    for _ in range(6):
        vanity_plate = input("Plate: ").strip()
        if is_valid_plate(vanity_plate):
            print("Valid")
        else:
            print("Invalid")

def is_valid_plate(plate):
    if len(plate) < 2 or len(plate) > 6:
        return False
    
    if not plate[0].isalpha() or not plate[1].isalpha():
        return False
    
    for char in plate:
        if not char.isalnum():
            return False
        
    numbers_started = False
    for char in plate:
        if char.isdigit():
            if not numbers_started and char == '0':
                return False
            numbers_started = True
        elif numbers_started and char.isalpha():
            return False
    return True
        


if __name__ == "__main__":
    main()