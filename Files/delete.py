import os

# os.remove('/workspaces/Python/Files/copy.txt')

# path = '/workspaces/Python/Files/copy.txt'
# try:
#     os.remove(path)
# except FileNotFoundError:
#     print("File not found")

path = '/workspaces/Python/Files/remove'

try:
    os.rmdir(path)
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("You dont have permission")
else:
    print(path+" was deleted")