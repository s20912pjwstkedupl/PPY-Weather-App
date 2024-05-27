import json

from kivy.metrics import dp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDButton, MDButtonText
from kivymd.uix.imagelist import MDSmartTileImage, MDSmartTile
from kivymd.uix.screen import MDScreen
from kivymd.uix.widget import MDWidget

from load_kv import load_kv

load_kv(__name__)


class WeatherTile(MDSmartTile):
    img = None
    date = ""
    temp = ""

    def __init__(self, _img, _date, _temp):
        super().__init__()
        self.img = _img
        self.date = _date
        self.temp = _temp

    def update_vars(self):
        self.ids.weather_img.source = self.img
        self.ids.label_date.text = self.date
        self.ids.label_temp.text = str(self.temp)
