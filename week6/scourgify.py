import sys
import csv

def main():
    valid_commandline()  # first check if arguments are valid

    try:
        with open(sys.argv[1]) as infile:  # open the input file (e.g. before.csv)
            reader = csv.DictReader(infile)  # reads each row as a dictionary like {"name": "Potter, Harry", "house": "Gryffindor"}

            rows = []  # empty list to store cleaned rows

            for i in reader:  # loop through every student
                last, first = i["name"].split(", ")  # split "Potter, Harry" into last="Potter", first="Harry"
                rows.append({"first": first, "last": last, "house": i["house"]})  # store cleaned row

    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")  # if file doesn't exist, exit with error

    with open(sys.argv[2], "w", newline="") as outfile:  # create/open the output file (e.g. after.csv)
        writer = csv.DictWriter(outfile, fieldnames=["first", "last", "house"])  # tell it what columns to write
        writer.writeheader()  # writes the header row: first,last,house
        writer.writerows(rows)  # writes all the cleaned student rows


def valid_commandline():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv"):
        sys.exit("Not a csv file")


if __name__ == "__main__":
    main()