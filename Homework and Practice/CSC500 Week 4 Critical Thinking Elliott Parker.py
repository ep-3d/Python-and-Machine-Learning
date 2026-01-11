# My Variables
num_years = int(input("Please enter the number of years you want to calculate: "))
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September","October", "November", "December"]
total_rainfall = []

# Nested for looping through years in months
for i in range (num_years):
    for j in range(len(months)):
        inches_rain = int(input("Please enter the total rain for {}: ".format(months[j])))
        total_rainfall.append(inches_rain)

# Calculations
total_months = num_years * len(months)
collected_rain = sum(total_rainfall)
average_rain = collected_rain / total_months

# Output
print()
print()
print("The total number of years is {}.".format(num_years))
print("There were {} total months counted.".format(total_months)) #number of months
print("Over that period {} total inches of rain fell.".format(collected_rain)) #total inches of rainfall
print("The average rainfall over that period was {} inches per month".format(average_rain)) #average rainfall for the entire period
