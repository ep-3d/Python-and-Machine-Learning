class ItemToPurchase:
    def __init__(self, item_name, item_price, item_quantity):
        self.item_name = str(item_name)
        self.item_price = float(item_price)
        self.item_quantity = int(item_quantity)

    def print_item_cost(self):
        print("{} {} @ ${} = ${}".format(self.item_name, self.item_quantity,self.item_price, (self.item_price * self.item_quantity)))
        return ""

item_1 = ItemToPurchase(item_name="bottled water", item_quantity=10, item_price=1)
#print(ItemToPurchase.print_item_cost(item_1))

item_name_1 = str(input("Please enter the 1st item name: "))
item_price_1 = float(input("Please enter the price of the item: "))
item_quant_1 = int(input("Please enter the quantity: "))
print()
item_name_2 = str(input("Please enter the 2nd item name: "))
item_price_2 = float(input("Please enter the price of the item: "))
item_quant_2 = int(input("Please enter the quantity: "))

item_1_classobject = ItemToPurchase(item_name_1,item_price_1,item_quant_1)
item_2_classobject = ItemToPurchase(item_name_2,item_price_2,item_quant_2)
print()
print()
print(ItemToPurchase.print_item_cost(item_1_classobject), end="")
print(ItemToPurchase.print_item_cost(item_2_classobject), end="")

print("Your total today is ${}".format((item_price_1*item_quant_1) + (item_price_2*item_quant_2) ))