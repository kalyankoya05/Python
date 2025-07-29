
store = [("shirt",20.00),
         ("Phant",25.00),
         ("Jacket",50.00),
         ("Socks",10.00)]

to_euros = lambda data: (data[0],data[1]*0.82)
to_dollars = lambda data: (data[0],data[1]/0.82)


# store_euros = list(map(to_euros,store))
store_dollars = list(map(to_dollars,store))

for i in store_dollars:
    print(i)

