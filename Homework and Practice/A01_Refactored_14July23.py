# ******************************************************************************
# Author:           Elliott Parker
# Assignment:       Assignment #01
# Date:             July 10, 2023
# Description:      This program takes the user’s first name, location, and a
#                   guess/estimate of the temperature as inputs. An API then
#                   pulls the temperature and humidity for their location, in
#                   as a zip code. I created an API to convert the ZIP to
#                   longitude and latitude coordinates. The program then
#                   calculates the heat index if the temperature is above 80
#                   degrees Fahrenheit. If the temperature is below 50 degrees,
#                   the program will also pull the wind speed. The wind speed
#                   will be used to calculate the wind chill.
# Revisions:        n/a
# ******************************************************************************

import requests

# Constants:
c_1 = 42.379
c_2 = 2.04901523
c_3 = 10.14333127
c_4 = 0.22475541
c_5 = 6.83783e-3
c_6 = 5.481717e-2
c_7 = 1.22874e-3
c_8 = 8.5282e-4
c_9 = 1.99e-6

d_1 = 35.74
d_2 = 0.6215
d_3 = 35.75
d_4 = 0.16
d_5 = 0.4275

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

# Welcome Message
print("Welcome to the weather App")

# Inputs
user_name = input("\nPlease enter your name: ")
zip_code = input("\nPlease enter your zip code: ")
#latitude = input("\nPlease enter your Latitude: ")
#longitude = input("\nPlease enter your Longitude: ")


# API for Direct GeoCoding data
API_KEY_zip = "9e3f1ef0cc4f44e4089db52f4de0cf0c"
API_ENDPOINT_zip = "http://api.openweathermap.org/geo/1.0/zip?"
part_2 = zip_code, country_code
Parameters_zip = {"zip": part_2,
                  "appid": API_KEY_zip}
response_zip = requests.get(API_ENDPOINT_zip, params=Parameters_zip)
data_zip = response_zip.json()

# Storing API Response Results (GeoCoding)
longitude = data_zip["lon"]
latitude = data_zip["lat"]
place = data_zip["name"]

# API For Weather Data
API_KEY = "9e3f1ef0cc4f44e4089db52f4de0cf0c"
API_ENDPOINT = "https://api.openweathermap.org/data/3.0/onecall?"
Parameters = {"lat": latitude,
              "lon": longitude,
              "exclude": part,
              "units": american_units,  # default units are in kelvin
              "appid": API_KEY}
response = requests.get(API_ENDPOINT, params=Parameters)
data = response.json()  # Reading the API Response (Weather)

# Storing API Response Results (Weather)
temperature = data["current"]["temp"]
relative_humidity = data["current"]["humidity"]
wind_velocity = data["current"]["wind_speed"]


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

# Calculations

heat_index = -c_1 + \
             c_2 * temperature + \
             c_3 * relative_humidity - \
             c_4 * temperature * relative_humidity - \
             c_5 * temperature * temperature - \
             c_6 * relative_humidity * relative_humidity + \
             c_7 * temperature * temperature * relative_humidity + \
             c_8 * temperature * relative_humidity * relative_humidity - \
             c_9 * temperature * temperature * \
             relative_humidity * relative_humidity

wind_chill = d_1 + \
             (d_2 * temperature) - \
             (d_3 * (wind_velocity ** d_4)) + \
             (d_5 * temperature * (wind_velocity ** d_4))

# Outputs

if temperature < 51:
  print(f"\nHello {user_name}. The current temperature in {place} is {temperature:.1f}")
  print(f"\nAnd with the wind chill, it feels like {wind_chill:.1f}")
  
elif temperature > 79:
  print(f"\nHello {user_name}. The current temperature in {place} is {temperature:.1f}")
  print(f"\nAnd with the heat index, it feels like {heat_index:.1f}")
  
else:
  print(f"\nHello {user_name}. The current temperature in {place} is {temperature:.1f}")
  print("You should wear a sweater")

print(f"Have a great day, {user_name}")
