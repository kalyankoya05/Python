try:
    with open('/workspaces/Python/Files/text.txt') as file:
        print(file.read())
except FileNotFoundError:
    print("file not found")
