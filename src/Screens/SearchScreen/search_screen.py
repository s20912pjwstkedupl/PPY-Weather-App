from kivymd.uix.button import MDButton, MDButtonText
from kivymd.uix.screen import MDScreen

from api.openstreetmap import get_geocode_by_query
from load_kv import load_kv

load_kv(__name__)

class SearchScreenView(MDScreen):
    search_result = []
    def goto_weather_for_geo(self, lat, lon, name):
        self.parent.get_screen("weather_screen").update_weather(lat, lon, name)
        self.parent.current = "weather_screen"
        print(lat, lon)

    def on_search_pressed(self):
        result = get_geocode_by_query(self.ids.search_text_city_name.text)
        self.search_result = result
        self.ids.search_results.clear_widgets()
        for item in result:
            btn = MDButton(
                MDButtonText(
                    text=item['name'],
                ),
                radius=0,
            )
            btn.bind(on_press=lambda x, bound_car=item: self.goto_weather_for_geo(item['lat'], item['lon'], item['name']))
            self.ids.search_results.add_widget(btn)
