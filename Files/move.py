import os

source = "/workspaces/Python/Files/text.txt"
destination = "/workspaces/Python/Exceptions"

try:
    if os.path.exists(destination):
        print("Available")
    else:
        os.replace(source,destination)
        print(source+ " moved")
except FileNotFoundError:
    print(source+ " Not Fount")