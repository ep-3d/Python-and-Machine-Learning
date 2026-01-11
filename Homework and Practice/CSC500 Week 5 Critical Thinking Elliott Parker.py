#Color Selection
first_color = input("Please type your 1st color ('red', 'blue' or 'yellow'): ").lower()
while (first_color != 'red') and (first_color != 'blue') and (first_color != 'yellow'):
    print("Invalid color, try again.")
    first_color = input("Please type your 1st color ('red', 'blue' or 'yellow'): ").lower()

second_color = input("Please type your 2nd color ('red', 'blue' or 'yellow'): ").lower()
while (second_color != 'red') and (second_color != 'blue') and (second_color != 'yellow'):
    print("Invalid color, try again.")
    second_color = input("Please type your 2nd color ('red', 'blue' or 'yellow'): ").lower()

# Red
if (first_color == "red") and (second_color == "blue"):
    print("{} and {} make PURPLE".format(first_color, second_color))
elif (first_color == "red") and (second_color == "yellow"):
    print("{} and {} make ORANGE".format(first_color, second_color))
elif (first_color == "red") and (second_color == "red"):
    print("{} and {} make RED".format(first_color, second_color))

# Blue
elif (first_color == "blue") and (second_color == "blue"):
    print("{} and {} make BLUE".format(first_color, second_color))
elif (first_color == "blue") and (second_color == "red"):
    print("{} and {} make PURPLE".format(first_color, second_color))
elif (first_color == "blue") and (second_color == "yellow"):
    print("{} and {} make GREEN".format(first_color, second_color))

# Yellow
elif (first_color == "yellow") and (second_color == "yellow"):
    print("{} and {} make YELLOW".format(first_color, second_color))
elif (first_color == "yellow") and (second_color == "red"):
    print("{} and {} make ORANGE".format(first_color, second_color))
else:
    (first_color == "yellow") and (second_color == "blue")
    print("{} and {} make GREEN".format(first_color, second_color))