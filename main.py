import requests
import json

data_dict = {
    "lat" : "32.830310",
    "lon": "35.078900",
    "exclude": "daily,current,minutely",
    "appid" : "021f4394e9dcd52e9716ebab2648fa86",

}

api_data = requests.get("https://api.openweathermap.org/data/2.5/onecall?", params=data_dict)
print(api_data.status_code)

weather_data = api_data.json()

# print(weather_data)
id_list = []
# print(weather_data['hourly'][5]['weather'][0]['description'])
will_rain = False
for i in range(0,13):
    id = weather_data['hourly'][i]['weather'][0]['id']

if id < 800:
    will_rain = True
else:
    pass
