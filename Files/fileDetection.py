import os

path = "/workspaces/Python/Files/text.txt"

if os.path.exists(path):
    print("Exists")
    if(os.path.isfile(path)):
        print("Yes file")
    elif(os.path.isdir(path)):
        print("Directory")
else:
    print("Not exists")