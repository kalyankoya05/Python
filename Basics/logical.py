temp = int(input("What is the temperature outside?: "))

if temp>=0 and temp <=30:
    print("The temp is good today")
    print("Go outside")
elif temp <0 or temp >30:
    print("Bad Temp")
    print("Stay indoor")

if not(temp>=0 and temp <=30):
    print("The temp is good today")
    print("Go outside")
elif not(temp <0 or temp >30):
    print("Bad Temp")
    print("Stay indoor")

