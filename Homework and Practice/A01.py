#******************************************************************************
# Author:           Elliott Parker
# Assignment:       Assignment #01
# Date:             July 10, 2023
# Description:      This program takes the user’s first name, location, and a
#                   guess/estimate of the temperature as inputs. An API then
#                   pulls the temperature and humidity for their location, in
#                   latitude and longitude coordinates. The program then
#                   calculates the heat index if the temperature is above 80
#                   degrees Fahrenheit. If the temperature is below 50 degrees,
#                   the program will also pull the wind speed. The wind speed
#                   will be used to calculate the wind chill.
# Revisions:        n/a
#******************************************************************************

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
EstimateTemp = 0
Temperature = 0
username = ""
Location = ""
HeatIndex = 0
WindChill = 0
RelativeHumidity = 0
WindVelocity = 0
latitude = 0.0000    # Beaverton Oregon = 45.4869   (−90; 90)
longitude = 0.0000   # Beaverton Oregon = 122.8040  (-180; 180)
Part = "minutely,hourly,daily,alerts"
AmericanUnits = "imperial"

# Welcome Message
print("Welcome to the weather App")

# Inputs
username = input("\nPlease enter your name: ")
latitude = input("\nPlease enter your Latitude: ")
longitude = input("\nPlease enter your Longitude: ")
EstimateTemp = input("\nCould you estimate the outside temperature: ")

# API
API_KEY = "9e3f1ef0cc4f44e4089db52f4de0cf0c"
API_ENDPOINT = "https://api.openweathermap.org/data/3.0/onecall?"
Parameters = {"lat": latitude,
              "lon": longitude,
              "exclude": Part,
              "units": AmericanUnits,  # default units are in kelvin
              "appid": API_KEY}
response = requests.get(API_ENDPOINT, params=Parameters)

"""Previously needed to verify that the API was formatting properly
and making the correct call to the website."""
# print(Parameters)
# print(response)
# print(response.url)
# print(response.status_code)
# print(response.content)

# Reading the API Response
data = response.json()

# Storing API Response Results
Temperature =       data["current"]["temp"]
RelativeHumidity =  data["current"]["humidity"]
WindVelocity =      data["current"]["wind_speed"]

"""Previously needed to verify that the API response was successful"""
# print(Temperature, RelativeHumidity, WindVelocity)


# Calculations

HeatIndex = -c_1 + \
            c_2 * Temperature + \
            c_3 * RelativeHumidity - \
            c_4 * Temperature*RelativeHumidity - \
            c_5*Temperature*Temperature - \
            c_6*RelativeHumidity*RelativeHumidity + \
            c_7*Temperature*Temperature*RelativeHumidity + \
            c_8*Temperature*RelativeHumidity*RelativeHumidity - \
            c_9*Temperature*Temperature*RelativeHumidity*RelativeHumidity


WindChill = d_1 + \
            (d_2 * Temperature) - \
            (d_3 * (WindVelocity ** d_4)) + \
            (d_5 * Temperature * (WindVelocity ** d_4))

# Outputs

if Temperature < 51:
  print(f"\nHello {username}. The current temperature is {Temperature:.1f} "
        f"and with the wind chill it feels like {WindChill:.1f}")
elif Temperature > 79:
  print(f"\nHello {username}. The current temperature is {Temperature:.1f} "
        f"and with the heat index it feels like {HeatIndex:.1f}")
else:
  print(f"\nHello {username}. The current temperature is {Temperature:.1f}."
        f" You should wear a sweater")
