
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window


class test_screen(FloatLayout):
    def mostrar(self, text):
        pass

    def borrar(self, text):
        pass


class TestApp(App):
    def build(self):
        Window.clearcolor = 1, 1, 1, 1
        return test_screen()