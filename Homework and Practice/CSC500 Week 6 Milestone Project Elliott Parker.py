class ItemToPurchase:  # Below is copied from Week 3 Milestone Project
    def __init__(self, item_name="None", item_price=0, item_quantity=0, description = "None"):#constructor to initialize ItemToPurchase
        self.item_name = str(item_name)
        self.item_price = float(item_price)
        self.item_quantity = float(item_quantity)
        self.description = description #this is referenced in the modify() method and has to be in here or it cant referenced it later.

    def print_item_cost(self):
        print("{} {} @ ${} = ${}".format(self.item_name, self.item_quantity,self.item_price, (self.item_price * self.item_quantity)))
        return ""

    def print_item_description(self):
        print(self.item_name,end=": ")
        print(self.description) #Shopping cart does not have a description section, was I supposed to add it?

class ShoppingCart:#Parameterized constructor with parameters:
    def __init__(self, customer_name="None", date="January 1, 2020", cart_items = []):
        self.customer_name = customer_name
        self.current_date = date
        self.cart_items = cart_items
        self.number_of_cart_items = 0

    def add_item(self, item): #Adds an item to cart_items list.
        self.cart_items.append(item)

    def remove_item(self, item_name): #Removes item from cart_items list.
        is_item_in_my_cart = False
        for item in self.cart_items:
            if(item.item_name==item_name):
                self.cart_items.remove(item)
                is_item_in_my_cart = True
                break
        if(not is_item_in_my_cart):
            print("Item not found.")

    def modify_item(self,item,item_quantity=-1,item_price=-1,item_description="none"):
        is_item_in_my_cart = False
        for i in self.cart_items:
            if (i.item_name == item.item_name):
                if(item_price!=-1):
                    i.item_price = item_price
                if(item_quantity!=-1):
                    i.item_quantity = item_quantity
                if(item_description!="none"):
                    i.item_description = item_description
                is_item_in_my_cart = True
                break
        if (not is_item_in_my_cart):
            print("Item not found.")

    def get_num_items_in_cart(self):
        if len(self.cart_items)==0:
            print("Shopping cart is empty")
        elif len(self.cart_items)!=0:
            cart_count = 0
            for i in self.cart_items:
                cart_count = cart_count + i.item_quantity
            return cart_count

    def get_cost_of_cart(self):
        total_cart_cost = 0
        for i in self.cart_items:
            total_cart_cost = total_cart_cost + (i.item_price * i.item_quantity)
        return total_cart_cost

    def print_total(self):
        if(self.get_num_items_in_cart() == 0):
            print("SHOPPING CART IS EMPTY")
        else:
            print(self.customer_name)
            print(self.current_date)
            print("Number of Items:", self.get_num_items_in_cart())
            print()
            for i in self.cart_items:
                i.print_item_cost()
            print("Total: $",end="")
            print(self.get_cost_of_cart())

    def print_descriptions(self):
        if (self.get_num_items_in_cart()  == 0):
            print("SHOPPING CART IS EMPTY")
        else:
            print(self.customer_name, end="'s Shopping Cart - ")
            print(self.current_date)
            print("Item Descriptions")
            for i in self.cart_items:
                i.print_item_description()

def grabcustomer_input():
    print(" a - Add item to cart\n "
          "r - Remove item from cart\n "
          "c - Change item quantity\n "
          "i - Output items' descriptions\n "
          "o - Output shopping cart\n "
          "q - Quit")
    return input()

def print_menu(cart):
    while(True):
        user_input = grabcustomer_input()
        if(user_input=='a'):
            print("ADD ITEM TO CART")
            item_name = input("Enter the item name:\n")
            description = input("Enter the item description:\n")
            item_price = input("Enter the item price:\n")
            item_quantity = input("Enter the item quantity:\n")
            item = ItemToPurchase(item_name,float(item_price),float(item_quantity),description)
            cart.add_item(item)

        if(user_input=='r'):
            print("REMOVE ITEM FROM CART")
            item_name = input("Enter name of item to remove:")
            cart.remove_item(item_name)

        if(user_input=='c'):
            print("CHANGE ITEM QUANTITY")
            name = input("Enter the item name:")
            quantity = input("Enter the new quantity:")
            Item = ItemToPurchase(name)
            cart.modify_item(Item,int(quantity))

        if(user_input=='i'):
            print("OUTPUT ITEMS' DESCRIPTIONS")
            cart.print_descriptions()

        if(user_input=='o'):
            print("OUTPUT SHOPPING CART")
            cart.print_total()

        if(user_input=='q'):
            # break the while loop
            break

# #Not going to be able to pass everything through all at onc.
# #Instantiate Customers
# aa = ShoppingCart("Joe", "January 1, 2020")
# bb = ShoppingCart("Mary", "January 2, 2020")

# #Not going to be able to pass everything through all at once... ***double check***..
# #Instantiate Items to Purchase
# yy = ItemToPurchase(item_name='pears' , item_price = 0.29 , item_quantity = 5, description = 'fruit')
# zz = ItemToPurchase(item_name='oranges' , item_price = 0.35 , item_quantity = 2, description = 'fruit')
# nn = ItemToPurchase(item_name='banana' , item_price = 0.50 , item_quantity = 6, description = 'fruit')
# kk = ItemToPurchase(item_name='Tuna Fish' , item_price = 11.19 , item_quantity = 1, description = 'seafood')
# jj = ItemToPurchase(item_name='Sea Bass' , item_price = 14.99 , item_quantity = 2, description = 'seafood')
# rr = ItemToPurchase(item_name='onion' , item_price = 0.99 , item_quantity = 3, description = 'produce')

def pleasework_prettyplease():
    name = input("Enter customer's name:\n")
    date = input("Enter today's date:\n")
    print("Customer name:",end=" ")
    print(name)
    print("Today's date:",end=" ")
    print(date)
    cart = ShoppingCart(name,date)
    # prints menu and modify cart items as entered by user interaction through menu
    print_menu(cart)

if __name__ == "__main__":
    pleasework_prettyplease()



#

#
# print(aa.get_num_items_in_cart())
# print(kk.item_price)