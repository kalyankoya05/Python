# def add(num1,num2):
#     sum = num1 + num2
#     return sum

# print(add(1,2))

def add(*nums):
    sum = 0
    for i in nums:
        sum += i
    return sum

print(add(1,2,3,4,5,6,7))