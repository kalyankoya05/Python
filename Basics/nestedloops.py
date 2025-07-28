rows = int(input("How Many rows?: "))
columns = int(input("How Many cloumns?: "))

symbol = input("Enter a symbol?: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()