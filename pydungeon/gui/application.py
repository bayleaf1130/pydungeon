
from kivy.uix.gridlayout import GridLayout
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.tabbedpanel import TabbedPanelItem
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


class CreationTab(GridLayout):
    pass


class ClassPanel(TabbedPanelItem):

    def class_change(self, instance, value, className): 
        if value is True:
            image_widget = App.get_running_app().root.ids.creation_tab.ids.class_icon_widget
            className = className.lower().replace(" ", "_").replace("-", "_")
            image_widget.source = 'gui/classes_icons/' + className + '_icon.png'
        
    def add_custom_class(self, instance, new_class, scroll_gridlayout):
        new_class_checkbox = CheckBox(size_hint_x= None, group= 'classes')
        # on_active=app.root.checkbox_click(self, self.active, new_class.title(), app.character_image_widget)
        new_class_label = Label(font_size='18sp', size_hint_x=None, text=new_class.title())

        scroll_gridlayout.add_widget(new_class_checkbox)
        scroll_gridlayout.add_widget(new_class_label)
        pass


class RacePanel(TabbedPanelItem):

    def race_change(self, instance, value, skinName): 
        if value is True:
            image_widget = App.get_running_app().root.ids.creation_tab.ids.character_image_widget
            skinName = skinName.lower().replace(" ", "_").replace("-", "_")
            image_widget.source = 'gui/character_images/fantasy_' + skinName + '.png'
    
    def add_custom_race(self, instance, new_race, scroll_gridlayout):
        app=App.get_running_app()

        new_race_checkbox = CheckBox(size_hint_x= None, group= 'races')
        # on_active=app.root.checkbox_click(self, self.active, new_race.title(), app.character_image_widget)
        new_race_label = Label(font_size='18sp', size_hint_x=None, text=new_race.title())

        scroll_gridlayout.add_widget(new_race_checkbox)
        scroll_gridlayout.add_widget(new_race_label)
        pass


class GuiApplication(App):

    def window_settings(self):
        Window.maximize()
        Window.clearcolor = (.15, .15, .15, 1)

    def build(self):
        self.window_settings()
        return CharacterCreator()
