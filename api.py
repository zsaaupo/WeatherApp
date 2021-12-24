"""
Api
"""
print(__doc__)
import requests

def format_data(weather_data):
    # formating weather data

    try:
        city_name = weather_data['name']
        fahrenheit = weather_data['main']['temp']
        celsius = (fahrenheit-32)*5//9
        condition = weather_data['weather'][0]['description']
        humidity = weather_data['main']['humidity']
        icon = weather_data['weather'][0]['icon']

        formated_data = 'City: %s \nCondition: %s \nTemperature (°C): %s \nHumidity %s' % (city_name, condition, celsius, humidity) # string format

    except:
         formated_data = 'OOPS!, Failed to retrieving informations'
         icon = ''
    
    return (formated_data, icon)


def weather_info(city_name):
    # get weather information by calling openweathermap api

    api_key = '368dabb4d7459b30b5fe8f72a59fba60' # weather api key 
    server = 'https://api.openweathermap.org/data/2.5/weather?' # weather api url

    parameter = {'APPID' : api_key, 'q' : city_name, 'units' : 'imperial'} # api's recommended parameter

    output = requests.get(server, parameter) # get request to api
    weather_data = output.json() # api respons convert to json data (dictionary)
    weather_report = format_data(weather_data)
    return weather_report

# print(weather_info('dhaka'))