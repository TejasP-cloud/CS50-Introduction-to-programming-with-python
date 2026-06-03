from validator_collection import checkers, validators

email = input("Enter email: ")

if checkers.is_email(email):
    print("Valid")
else:
    print("Invalid")

validators.email(email)