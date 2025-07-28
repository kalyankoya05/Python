utensils = {"fork","Spoon","Knief"}
dishes = {"bowl","plate","cup","Knief"}

# utensils.add("napkin")
# utensils.remove("fork")
# utensils.clear()
# utensils.update(dishes)

dinner_table = utensils.union(dishes)

for x in dinner_table:
    print(x)