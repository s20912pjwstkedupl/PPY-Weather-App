import requests
import urllib.parse

def get_geocode_by_query(query: str):
    loc = requests.get(f"https://nominatim.openstreetmap.org/search.php?q={urllib.parse.quote_plus(query)}&format=jsonv2&limit=10", headers={
        "Accept": "application/json",
        "User-Agent": "PPY Weather App"
    })
    data = loc.json()
    return list(map(lambda item: {
        'lat': item['lat'],
        'lon': item['lon'],
        'name': item['display_name']
    }, data))

# print(get_geocode_by_query("Kraków"))