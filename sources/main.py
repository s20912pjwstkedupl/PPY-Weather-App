from kivy.uix.screenmanager import ScreenManager

from kivymd.tools.hotreload.app import MDApp
class SM(ScreenManager):
    def get_classes(self):
        return {screen.__class__.__name__: screen.__class__.__module__ for screen in self.screens}

class WeatherApp(MDApp):
    DEBUG = True
    sm = None
    state = {}

    def build_app(self, first=False):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "White"
        if self.sm is None:
            self.state = {'current': 'search_screen'}

        KV_FILES = []
        self.sm = SM()
        CLASSES = self.sm.get_classes()
        return self.sm

    def apply_state(self, state):
        self.sm.current = state['current']


if __name__ == '__main__':
    app = WeatherApp()
    app.run()
