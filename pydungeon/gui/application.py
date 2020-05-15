
from kivy.uix.gridlayout import GridLayout
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.checkbox import CheckBox
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

Builder.load_file('pydungeon/gui/kv_application_files/application.kv')

class CharacterCreator(BoxLayout):
    pass


class CategoryTabs(GridLayout):

    def checkbox_click(self, instance, value, skinName, image_widget): 
        if value is True:
            skinName = skinName.lower().replace(" ", "_").replace("-", "_")
            image_widget.source = 'gui/character_images/fantasy_' + skinName + '.png'
    
    def add_custom_class(self, instance, new_race, scroll_gridlayout):
        app=App.get_running_app()

        new_race_checkbox = CheckBox(size_hint_x= None, group= '1')
        # on_active=app.root.checkbox_click(self, self.active, new_race.title(), app.character_image_widget)
        new_race_label = Label(font_size='18sp', size_hint_x=None, text=new_race.title())

        scroll_gridlayout.add_widget(new_race_checkbox)
        scroll_gridlayout.add_widget(new_race_label)
        pass


class GuiApplication(App):

    def window_settings(self):
        Window.maximize()

    def build(self):
        self.window_settings()
        return CharacterCreator()
