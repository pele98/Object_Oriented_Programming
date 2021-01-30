fruits = ["Apple", "Pear", "Peach", "Banana"]
prices = [0.35, 0.40, 0.40, 0.28]

fruit_dictionary = dict(zip(prices, fruits))

print(fruit_dictionary)

fruit_dictionary.pop(min(prices))

print(fruit_dictionary)