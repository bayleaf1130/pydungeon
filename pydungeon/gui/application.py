from kivy.app import App
from kivy.uix.button import Button

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
        return Button(text='Hello World')

#GuiApplication().run()