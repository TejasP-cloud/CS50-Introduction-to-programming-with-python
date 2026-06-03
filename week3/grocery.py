grocery = {}

def get_input():
    items = input("Enter Item: ").upper().strip()
    return items
    
def main():
    while True:
        try:
            items = get_input()
            if items in grocery:
                grocery[items] += 1
            else:
                grocery[items] = 1
        except EOFError:
            print("Exiting program")
            break
        
    for items in sorted(grocery):
        print(grocery[items], items)

if __name__ == "__main__":
    main()
    
