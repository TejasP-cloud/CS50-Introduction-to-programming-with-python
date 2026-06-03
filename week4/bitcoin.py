import requests
import sys

def main():
    if len(sys.argv) != 2:
        print("Missing command line argument")
        sys.exit(1)
    try:
        bitcoin = float(sys.argv[1])
    except ValueError:
        print("Missing command line argument")
        sys.exit(1)
    
    response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd")
    data = response.json()
    price = data["bitcoin"]["usd"]
    total = bitcoin * price
    print(f"Current total value of bitcoin: ${total:,.4f}")


if __name__ == "__main__":
    main()