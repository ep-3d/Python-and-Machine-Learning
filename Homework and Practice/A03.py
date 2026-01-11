"""
# ****************************************************************************
# Author:           Elliott Parker
# Assignment:       Assignment #03
# Date:             July 31, 2023
# Description:      This program takes the user’s first name, location, and a
#                   guess/estimate of the temperature as inputs. An API then
#                   pulls the temperature and humidity for their location, in
#                   as a zip code. I created an API to convert the ZIP to
#                   longitude and latitude coordinates. The program then
#                   calculates the heat index if the temperature is above 80
#                   degrees Fahrenheit. If the temperature is below 50 degrees,
#                   the program will also pull the wind speed. The wind speed
#                   will be used to calculate the wind chill.
#                   (02) Refactoring for functions (02)
#                   (03) Adding while loops, menu and If/Elif/Else statements.
# Revisions:        n/a
# ****************************************************************************
"""
import requests

# Constants:
C_1 = 42.379
C_2 = 2.04901523
C_3 = 10.14333127
C_4 = 0.22475541
C_5 = 6.83783e-3
C_6 = 5.481717e-2
C_7 = 1.22874e-3
C_8 = 8.5282e-4
C_9 = 1.99e-6
D_1 = 35.74
D_2 = 0.6215
D_3 = 35.75
D_4 = 0.16
D_5 = 0.4275

# Variables
temperature = 0
user_name = ""
location = ""
heat_index = 0
wind_chill = 0
relative_humidity = 0
wind_velocity = 0
latitude = 0.0000  # Beaverton Oregon = 45.4869   (−90; 90)
longitude = 0.0000  # Beaverton Oregon = 122.8040  (-180; 180)
part = "minutely,hourly,daily,alerts"
american_units = "imperial"
zip_code = 0
country_code = "US"
place = ""
fav_list = []  # I have to store the favorites somewhere


def main():
	welcome()
	choice = menu()
	print(f"\nYour choice was #{choice}.")
	
	while choice != 4:
		if choice == 1:
			user_name = get_name()
			zip_code = get_location()
			data_zip = geocode(zip_code)
			longitude = get_longitude(data_zip)
			latitude = get_latitude(data_zip)
			place = get_place(data_zip)
			data_1 = weather(longitude, latitude)
			temperature = get_temperature(data_1)
			relative_humidity = get_humidity(data_1)
			wind_velocity = get_wind_vel(data_1)
			heat_index = calc_heat_index(temperature, relative_humidity)
			wind_chill = calc_wind_chill(temperature, wind_velocity)
			outputs(temperature, user_name, place, wind_chill, heat_index)
			choice = menu()
		elif choice == 2:
			# Store your favorite zip codes
			fav_list = menu_option_2()
			choice = menu()   # previously commented out code
			
			""" I previously had commented out choice = menu()
			this resulted in choice not updating and the program
			was stuck in a loop after you selected option 2.
			ChatGPT was no help either. He/She keeps wanting
			to change how my while loops work, even though that
			was not what I was trying to fix. It took 4 hours
			to figue out why I was stuck in a loop."""
		
		elif choice == 3:
			# Show your list of favorites
			print_favs = menu_option_3(fav_list)
			print()
			choice = menu()
		elif choice == 4:
			print("Thank you and goodbye!")
			# exit the program
		else:
			print("Make Better choices...\n")
			choice = menu()
	
	goodbye()


def welcome():
	"""
  Prints a welcome message.
  """
	print("Welcome to the weather App\n")  # Welcome Message


def get_name():  # Inputs
	"""
	Asks the user to enter their name.
	:return: The name entered by the user. Datatype: String
	"""
	user_name = input("\nPlease enter your name: ")
	return user_name


def get_location():  # Inputs
	"""
	Asks the user to enter their zip code.
	:return: The zip code entered by the user. Datatype: Integer
	"""
	zip_code = input("\nPlease enter your zip code: ")
	return zip_code


"""
Legacy code - no longer needed...
	#latitude = input("\nPlease enter your Latitude: ")
	#longitude = input("\nPlease enter your Longitude: ")

"""


def geocode(zip_code):  # API for Direct GeoCoding data
	"""
	Retrieves the geographical data (longitude, latitude,
	and place name) for a given zip code using the OpenWeatherMap API.
	:param zip_code: The zip code for retrieval the data.
		Datatype: Integer
	:return: The API response data in JSON format.
	"""
	API_KEY_zip = "9e3f1ef0cc4f44e4089db52f4de0cf0c"
	API_ENDPOINT_zip = "http://api.openweathermap.org/geo/1.0/zip?"
	part_2 = ",".join([str(zip_code), country_code])
	"""
	I needed ChatGPT's help here because this
	was previously a tuple but when I put the code in
	a function it would only accept a string.
	"""
	
	parameters_zip = {"zip": part_2,
	                  "appid": API_KEY_zip}
	response_zip = requests.get(API_ENDPOINT_zip, params=parameters_zip)
	data_zip = response_zip.json()
	return data_zip


def get_longitude(data_zip):  # Storing API Response Results (GeoCoding)
	"""
	Retrieves the longitude from the API response data.
	:param data_zip: The API response data in JSON format.
	:return: The longitude value. Datatype: Float
	"""
	longitude = data_zip["lon"]
	return longitude


def get_latitude(data_zip):  # Storing API Response Results (GeoCoding)
	"""
	Retrieves the latitude from the API response data.
	:param data_zip: The API response data in JSON format.
	:return: The latitude value. Datatype: Float
	"""
	latitude = data_zip["lat"]
	return latitude


def get_place(data_zip):  # Storing API Response Results (GeoCoding)
	"""
  Retrieves the place name from the API response data.
  :param data_zip: The API response data in JSON format.
  :return: The place name. Datatype: String
  """
	place = data_zip["name"]
	return place


def weather(longitude, latitude):  # API For Weather Data
	"""
	Retrieves weather data for a given longitude and latitude
	using the OpenWeatherMap API.
	:param longitude: The longitude for weather data. Datatype: Float
	:param latitude: The latitude for weather data.Datatype: Float
	:return: The API response data in JSON format.
	"""
	API_KEY = "9e3f1ef0cc4f44e4089db52f4de0cf0c"
	API_ENDPOINT = "https://api.openweathermap.org/data/3.0/onecall?"
	Parameters = {"lat": latitude,
	              "lon": longitude,
	              "exclude": part,
	              "units": american_units,  # default units are in kelvin
	              "appid": API_KEY}
	response = requests.get(API_ENDPOINT, params=Parameters)
	data_1 = response.json()  # Reading the API Response (Weather)
	return data_1


def get_temperature(data_1):  # Storing API Response Results (Weather)
	"""
	Retrieves the current temperature from the API response data.
	:param data_1: The API response data in JSON format.
	:return: The temperature value. Datatype: Float
	"""
	temperature = data_1["current"]["temp"]
	return temperature


def get_humidity(data_1):
	"""
	Retrieves the current humidity from the API response data.
	:param data_1: The API response data in JSON format.
	:return: The humidity value. Datatype: Float
	"""
	relative_humidity = data_1["current"]["humidity"]
	return relative_humidity


def get_wind_vel(data_1):
	"""
	Retrieves the current wind velocity from the API response data.
	:param data_1: The API response data in JSON format.
	:return: The wind velocity value. Datatype: Float
	"""
	wind_velocity = data_1["current"]["wind_speed"]
	return wind_velocity


"""
Previously needed to verify that the API was formatting properly
and making the correct call to the website.

print(Parameters_zip)
print(response_zip)
print(response_zip.url)
print(response_zip.status_code)
print(response_zip.content)
print(Temperature, RelativeHumidity, WindVelocity)
"""


def calc_heat_index(temperature, relative_humidity):  # Calculations
	"""
	Calculates the heat index based on the temperature and relative humidity.
	:param temperature: The current temperature. Datatype: Float
	:param relative_humidity: The current relative humidity. Datatype: Float
	:return: The heat index value. Datatype: Float
	"""
	heat_index = -C_1 + \
	             C_2 * temperature + \
	             C_3 * relative_humidity - \
	             C_4 * temperature * relative_humidity - \
	             C_5 * temperature * temperature - \
	             C_6 * relative_humidity * relative_humidity + \
	             C_7 * temperature * temperature * relative_humidity + \
	             C_8 * temperature * relative_humidity * relative_humidity - \
	             C_9 * temperature * temperature * \
	             relative_humidity * relative_humidity
	return heat_index


def calc_wind_chill(temperature, wind_velocity):  # Calculations
	"""
	Calculates the wind chill based on the temperature and wind velocity.
	:param temperature: The current temperature. Datatype: Float
	:param wind_velocity: The current wind velocity. Datatype: Float
	:return: The wind chill value. Datatype: Float
	"""
	wind_chill = D_1 + \
	             (D_2 * temperature) - \
	             (D_3 * (wind_velocity ** D_4)) + \
	             (D_5 * temperature * (wind_velocity ** D_4))
	return wind_chill


def outputs(temperature, user_name, place, wind_chill, heat_index):  # Outputs
	"""
	Displays the weather information and appropriate messages
	based on the temperature.
	:param temperature: The current temperature. Datatype: Float
	:param user_name: The name of the user. Datatype: String
	:param place: The name of the place. Datatype: String
	:param wind_chill: The calculated wind chill value. Datatype: Float
	:param heat_index: The calculated heat index value. Datatype: Float
	"""
	if temperature < 51:
		print(f"\nHello {user_name}. The current temperature in {place}"
		      + f" is {temperature:.1f}")
		print(f"\nAnd with the wind chill it feels like {wind_chill:.1f}")
	elif temperature > 79:
		print(f"\nHello {user_name}. The current temperature in {place}"
		      + f" is {temperature:.1f}")
		print(f"\nAnd with the heat index it feels like {heat_index:.1f}")
	else:
		print(f"\nHello {user_name}. The current temperature in {place}"
		      + f" is {temperature:.1f}")
		print("You should wear a sweater")


def goodbye():
	"""
	Prints a goodbye message.
	"""
	print("Thank you and Goodbye!")


"""Assignment 3 code [function definitions] starts here:"""


def menu():
	"""
	Displays a menu and prompts the user for a selection.
	:return: The user's selection as an integer. Datatype: Int
	"""
	print("[1] Get Current Weather")
	print("[2] Store Favorite Location")
	print("[3] View Favorites")
	print("[4] Exit\n")
	
	choice = int(input("Please enter your selection: "))
	return choice


def menu_option_2():
	"""
	Prompts the user to enter favorite zip codes and stores them in a list.
	Continues to prompt until the user chooses not to enter a new zip code.
	:return: A list of favorite zip codes. Datatype: List of Int
	"""
	fav_list = []
	while True:
		enter_new_zip = input("\nEnter new Zip Code? [y] / [n]: ")
		if enter_new_zip == "y":
			new_fav_zip = int(input("\nPlease enter your favorite zip: "))
			fav_list.append(new_fav_zip)
			print(f"\n{new_fav_zip} has been added to your favorites.")
			print("\nShowing list for reference", fav_list)
		elif enter_new_zip == "n":
			print()
			break
		else:
			print("\nPlease select either yes [y] or no [n].")
	return fav_list


def menu_option_3(fav_list):
	"""
	Prints the user's favorite zip codes.
	:param fav_list: A list of favorite zip codes. Datatype: List of Int
	"""
	print("\nHere is a list of your favorite zip codes: \n")
	print(fav_list)

"""
Problems to solve:

(1) some zip codes start with a zero and now I have to
	  change this to a string instead of an integer. The
	  zip codes also have to be 5 digits long.
 
(2) Option two has to be run before option 3 or the
    program crashes. Two creates the fav_list variable
    and three references it. I am not sure how to fix
    this.

   (-) Maybe tell python to check to see if the list is
       empty, and then if it is empty output a message
       directing the user to first create a list of
       favorites
       
(3) I use a break in menu_option_2, is there another
    way to exit the loop?
    
"""


main()
