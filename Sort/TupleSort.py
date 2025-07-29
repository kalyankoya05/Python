students = [("Kalyan","A",26),
             ("Koya","A",24),
             ("Nani","D",30),
             ("Sai","C",27),
             ("Amma","D",50)]

# students.sort()

# for i in students:
#     print(i)

# grade = lambda grades:grades[1]
# students.sort(key=grade)
# for i in students:
#     print(i)

age = lambda ages:ages[2]
students.sort(key=age,reverse=True)
for i in students:
    print(i)