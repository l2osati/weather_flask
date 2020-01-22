import requests
import sys

key = "d113c46fb9b524b20948131702128e3b"
default_lat = '38.5744896'
default_lon = '-121.43493120000001'

def get_current_weather(lat=default_lat, lon=default_lon):
    params = {
        'lat': lat,
        'lon': lon,
        'APPID': key,
        'units': 'imperial'
    }
    
    url = f"http://api.openweathermap.org/data/2.5/weather"
    r = requests.get(url, params=params)

    return r.json()

def get_five_day_forecast(lat=default_lat, lon=default_lon):
    params = {
        'lat': lat,
        'lon': lon,
        'APPID': key
    }

    url = f"http://api.openweathermap.org/data/2.5/forecast"
    r = requests.get(url, params=params)

    return r.json()

def flatten_dictionary(data, label=""):
    new_data = {}

    if label != "":
        label = f"{label}_"

    for key, value in data.items():
        if type(value) not in [dict, list]:
            new_data[f"{label}{key}"] = value                
        else:
            if type(value) is dict:
                new_data.update(flatten_dictionary(value, key))
            elif type(value) is list:
                new_data.update(flatten_dictionary(value[0], key))

    return new_data

if __name__ == "__main__":
    #print(flatten_dictionary(get_current_weather()))
    get_five_day_forecast()