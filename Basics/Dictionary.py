capitals = {'USA':'Washington DC',
            'India':'New Delhi',
            'China':'Beijing',
            'Russia':'Moscow'}

# print(capitals['Russia'])
# print(capitals['Germany'])

# print(capitals.get('Germany'))

# print(capitals.keys())
# print(capitals.items())
# print(capitals.values())

capitals.update({'Germany':'Berlin'})
capitals.update({'USA':'New York'})
capitals.pop('China')
capitals.clear()

for key,value in capitals.items():
    print(key,value)