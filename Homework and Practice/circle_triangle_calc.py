

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3}

stock = {"banana": 6,
         "apple": 0,
         "orange": 32,
         "pear": 15}

for food in prices:
    print(food) #name of the food
    print("price: %s" % prices[food]) #price of the food
    print("stock: %s" % stock[food]) #how many are in stock

total = 0

for food in prices:
    print(prices[food] * stock[food])
    total = total+(prices[food] * stock[food])
print (total)

groceries = ["banana","orange","apple"]
