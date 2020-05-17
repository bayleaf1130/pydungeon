# regular imports
from functools import partial
# kivy imports
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
# layout imports
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
# widget imports
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.tabbedpanel import TabbedPanelItem
from kivy.uix.checkbox import CheckBox
from kivy.uix.dropdown import DropDown


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


class StatsPanel(TabbedPanelItem):
    pass


class BonusesPanel(TabbedPanelItem):
    pass


class InventoryPanel(TabbedPanelItem):  

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.drop_down = InventoryDropDown()  
    
    def add_inventory_item(self, instance, item_name, item_description, scroll_gridlayout):
        app=App.get_running_app()

        layout = BoxLayout(orientation='horizontal')
        inventory_description_label = Label(font_size='14sp', size_hint_x=0.7, text=item_description, halign="left", valign="top")
        inventory_name_button = Button(font_size='18sp', size_hint_x=0.3, text=item_name.title())
        inventory_name_button.pressed = 0
        inventory_name_button.bind(on_press=lambda item_name: self.show_description(inventory_name_button, inventory_description_label, layout))

        layout.add_widget(inventory_name_button)

        scroll_gridlayout.add_widget(layout)

    def show_description(self, name_button, description_label, layout):
        name_button.pressed = (name_button.pressed + 1) % 2
        if(name_button.pressed == 1):
            layout.add_widget(description_label)
        else:
            layout.remove_widget(description_label)
        pass


class AttackPanel(TabbedPanelItem):  

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.drop_down = AttackDropDown()    
    
    def add_attack(self, instance, attack_name, attack_description, scroll_gridlayout):
        app=App.get_running_app()

        layout = BoxLayout(orientation='horizontal')
        attack_description_label = Label(font_size='14sp', size_hint_x=0.7, text=attack_description, halign="left", valign="top")
        attack_name_button = Button(font_size='18sp', size_hint_x=0.3, text=attack_name.title())
        attack_name_button.pressed = 0
        attack_name_button.bind(on_press=lambda item_name: self.show_description(attack_name_button, attack_description_label, layout))

        layout.add_widget(attack_name_button)

        scroll_gridlayout.add_widget(layout)

    def show_description(self, name_button, description_label, layout):
        name_button.pressed = (name_button.pressed + 1) % 2
        if(name_button.pressed == 1):
            layout.add_widget(description_label)
        else:
            layout.remove_widget(description_label)
        pass


class ProficienciesPanel(TabbedPanelItem):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.drop_down = ProficienciesDropDown()    
    
    def add_proficiency(self, instance, proficiency_name, proficiency_description, scroll_gridlayout):
        app=App.get_running_app()

        layout = BoxLayout(orientation='horizontal')
        proficiency_description_label = Label(font_size='14sp', size_hint_x=0.7, text=proficiency_description, halign="left", valign="top")
        proficiency_name_button = Button(font_size='18sp', size_hint_x=0.3, text=proficiency_name.title())
        proficiency_name_button.pressed = 0
        proficiency_name_button.bind(on_press=lambda item_name: self.show_description(proficiency_name_button, proficiency_description_label, layout))

        layout.add_widget(proficiency_name_button)

        scroll_gridlayout.add_widget(layout)

    def show_description(self, name_button, description_label, layout):
        name_button.pressed = (name_button.pressed + 1) % 2
        if(name_button.pressed == 1):
            layout.add_widget(description_label)
        else:
            layout.remove_widget(description_label)
        pass



class SkillsPanel(TabbedPanelItem):
    pass


class AbilitiesPanel(TabbedPanelItem):
    pass


class InventoryDropDown(DropDown):

    def drop_down_control(self, name):
        #App.get_running_app().root.ids.creation_tab.ids.inventory_panel.drop_down.close(self)
        App.get_running_app().root.ids.creation_tab.ids.inventory_panel.ids.item_dropdown_type.text = name


class AttackDropDown(DropDown):

    def drop_down_control(self, name):
        #App.get_running_app().root.ids.creation_tab.ids.inventory_panel.drop_down.close(self)
        App.get_running_app().root.ids.creation_tab.ids.attack_panel.ids.attack_dropdown_type.text = name


class ProficienciesDropDown(DropDown):

    def drop_down_control(self, name):
        #App.get_running_app().root.ids.creation_tab.ids.inventory_panel.drop_down.close(self)
        App.get_running_app().root.ids.creation_tab.ids.proficiencies_panel.ids.proficiency_dropdown_type.text = name


class InputField(AnchorLayout):
    pass


class GuiApplication(App):

    def window_settings(self):
        Window.maximize()
        Window.clearcolor = (.15, .15, .15, 1)

    def build(self):
        self.window_settings()
        return CharacterCreator()
