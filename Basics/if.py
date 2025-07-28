age = int(input("How old are  you?: "))

if age >= 18 and age < 100:
    print("You are an adult!!")
elif age >=100:
    print("you are century old!!!")
elif age < 0:
    print("You are not born!!!")
else:
    print("You are Kid!!!")