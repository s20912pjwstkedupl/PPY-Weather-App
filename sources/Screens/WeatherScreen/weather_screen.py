import json

from kivymd.app import MDApp
from kivymd.uix.button import MDButton, MDButtonText
from kivymd.uix.screen import MDScreen

from Components.weather_tile import WeatherTile
from api.openmeteo import get_weather_by_geocode
from load_kv import load_kv

load_kv(__name__)


class WeatherScreenView(MDScreen):
    weather = []
    lat = 0
    lon = 0
    city_name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pictures = json.load(open('dist/static/weather.json'))

    def update_weather(self, lat, lon, city_name):
        self.lat = lat
        self.lon = lon
        self.weather = get_weather_by_geocode(self.lat, self.lon)
        self.ids.city_name.text = city_name[:50]

        self.ids.weather_tiles_list.clear_widgets()
        for day in self.weather:
            img = self.pictures[str(day[2])]['day']['image']
            date = day[0]
            temp = day[1]
            w = WeatherTile(img, date, f"{temp} \N{DEGREE SIGN}C")
            w.update_vars()
            self.ids.weather_tiles_list.add_widget(w)

    def go_back(self):
        self.parent.current = "search_screen"
