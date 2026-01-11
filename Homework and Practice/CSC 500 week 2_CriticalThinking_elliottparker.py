sales_tax =0.07

item1 = float(input("Enter the price of your FIRST item:"))
item2 = float(input("Enter the price of your SECOND item:"))
item3 = float(input("Enter the price of your THIRD item:"))
item4 = float(input("Enter the price of your FOURTH item:"))
item5 = float(input("Enter the price of your FIFTH item:"))

subtotal=(item1 + item2 + item3 + item4 + item5)
subtotal = round(subtotal,2)
calc_tax = subtotal * sales_tax
calc_tax = round(calc_tax,2)

print()
print()

print('subtotal = ', subtotal,)
print('sales tax = ', calc_tax)
print('total = ', round((calc_tax + subtotal),2))