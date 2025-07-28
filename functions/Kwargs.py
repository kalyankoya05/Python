# def hello(first,last):
#     print("Hello "+first + " "+last)

# hello("Kalyan","Koya")

def hello(**kwargs):
    # print("Hello "+ kwargs['first'] + " "+ kwargs['last'])
    print("Hello",end=" ")
    for key,value in kwargs.items():
        print(value,end=" ")


hello(first="Kalyan",middle="Hello",last="Koya")