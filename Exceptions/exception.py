try:
    numerator = int(input("Enter numerator: "))
    denominator = int(input("Enter denominator: "))

    result = numerator/denominator

   
except ZeroDivisionError as e:
    print(e)
    print("You cant divide by zero")
except ValueError as e:
    print(e)
    print("Enter a numeric value")

except Exception as e :
    print(e)
    print("Divided by zero is not possible!!!")

else:
    print(result)

finally:
    print("Finally")