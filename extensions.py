def extension(file):
    file = file.lower().strip()
    if file.endswith(".jpg") or file.endswith(".jpeg"):
        return "image/jpeg"
    elif file.endswith(".png"):
        return "image/png"
    elif file.endswith(".gif"):
        return "image/gif"
    elif file.endswith(".pdf"):
        return "application/pdf"
    elif file.endswith(".txt"):
        return "text/plain"
    elif file.endswith(".zip"):
        return "application/zip"
    else:
        return "application/octet-stream"

def main():
    user_input = input("File name: ")
    print(extension(user_input))

main()
