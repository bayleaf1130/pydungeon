
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window

'''
Kivy:
https://kivy.org/doc/stable/installation/installation-windows.html#install-win-dist

python -m pip install --upgrade pip wheel setuptools virtualenv
python -m virtualenv kivy_venv
kivy_venv\Scripts\activate
python -m pip install docutils pygments pypiwin32 kivy_deps.sdl2==0.1.* kivy_deps.glew==0.1.*
python -m pip install kivy_deps.gstreamer==0.1.*
python -m pip install kivy==1.11.1

python kivy_venv\share\kivy-examples\demo\showcase\main.py
'''


class GuiApplication(App):

    def build(self):
        self.window_settings()
        return LoginScreen()

    def window_settings(self):
        Window.maximize()


class LoginScreen(GridLayout):

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2
        self.add_widgets()
    
        with self.canvas.before:
            Color(0, 0, 1, 1) # green; colors range from 0-1 instead of 0-255
            self.rect = Rectangle(size=self.size,
                                pos=self.pos)
        
        self.bind(pos=self.update_rect, size=self.update_rect)

    
    def add_widgets(self):
        self.add_widget(Label(text='Character Name'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)
        self.add_widget(Label(text='Race'))
        self.race = TextInput(multiline=False)
        self.add_widget(self.race)
        self.add_widget(Label(text='Class'))
        self.characterClass = TextInput(multiline=False)
        self.add_widget(self.characterClass)

    
    def update_rect(self, instance, value):
        instance.rect.pos = instance.pos
        instance.rect.size = instance.size
