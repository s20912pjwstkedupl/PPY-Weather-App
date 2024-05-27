import requests

def get_weather_by_geocode(latitude, longitude):
    res = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=weather_code,temperature_2m_max&timezone=Europe%2FBerlin", headers={
        "Accept": "application/json",
    })
    data = res.json()['daily']
    return list(zip(data['time'], data['temperature_2m_max'], data['weather_code']))


# print(get_weather_by_geocode(52.2298, 21.0118))