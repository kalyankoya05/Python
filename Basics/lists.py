food = ["Mutton","Chicken","Biryani"]
 
# print(food)
# print(food[1])

food.append("Ice Cream")
food.remove("Biryani")
food.pop()
food.insert(0,"Haleem")
food.sort()
food.clear()

for x in food:
    print(x)