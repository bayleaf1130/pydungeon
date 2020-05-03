''' character edit '''

from collections import UserDict
import abc


class CharacterProperty(abc.ABC):
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @property
    @abc.abstractmethod
    def getter(self):
        pass

    @property
    @abc.abstractmethod
    def setter(self):
        pass

    @property
    @abc.abstractmethod
    def deleter(self):
        pass


# Just stored in a dict with name/value pairing
class SimpleProperty(CharacterProperty):
    def __init__(self, name):
        super().__init__(name)

    @property
    def getter(self):
        def g(that):
            if self.name in that:
                return that[self.name]

        return g

    @property
    def setter(self):
        def s(that, value):
            that[self.name] = value

        return s

    @property
    def deleter(self):
        def d(that):
            if self.name in that:
                del that[self.name]

        return d

# Name is stored in the dict as key but setting this adds data to a list, deleting gets rid of the list and property
class ListProperty(CharacterProperty):
    def __init__(self, name):
        super().__init__(name)

    @property
    def getter(self):
        def g(that):
            if self.name in that:
                return that[self.name]

        return g

    @property
    def setter(self):
        def s(that, value):
            if self.name in that:
                that[self.name].append(value)
            else:
                that[self.name] = []
                that[self.name].append(value)

        return s

    @property
    def deleter(self):
        def d(that):
            if self.name in that:
                del that[self.name]

        return d


# A property that is a dict itself and can be accessed like one, items should be iterable pairs
class DictionaryProperty(CharacterProperty):
    def __init__(self, name):
        super().__init__(name)

    @property
    def getter(self):
        def g(that):
            if self.name in that:
                return that[self.name]

        return g

    @property
    def setter(self):
        # Value should be a tuple here
        def s(that, value):
            try:
                if self.name in that:
                    for key,val in value:
                        that[self.name][key] = val
                else:
                    that[self.name] = {}
                    for key,val in value:
                        that[self.name][key] = val
            except IndexError:
                pass

        return s

    @property
    def deleter(self):
        def d(that):
            if self.name in that:
                del that[self.name]

        return d


class Item(object):
    __slots__ = ['_name', '_value', '_info']

    def __init__(self, name, value=0, info=''):
        self._name = name
        self._value = value
        self._info = info

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def value(self):
        return self.value

    @value.setter
    def value(self, value):
        self._value = value

    @property
    def info(self):
        return self._info

    @info.setter
    def info(self, value):
        self._info = value

    def __str__(self):
        return '\n'.join([f'name: {self._name}', f'value: {self._value}', f'info: {self._info}'])


class Weapon(object):
    __slots__ = ['_name', '_value', '_info', '_hitdice', '_weapon_type']

    def __init__(self, name, value=0, info='', hitdice=8, weapon_type='strength'):
        self._name = name
        self._value = value
        self._info = info
        self._hitdice = 0
        self._weapon_type = weapon_type

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, value):
        self._name = value


    @property
    def value(self):
        return self.value

    @value.setter
    def value(self, value):
        self._value = value

    @property
    def info(self):
        return self._info

    @info.setter
    def info(self, value):
        self._info = value

    @property
    def hitdice(self):
        return self._hitdice

    @hitdice.setter
    def info(self, value):
        self._hitdice = value

    @property
    def weapon_type(self):
        return self._weapon_type

    @weapon_type.setter
    def weapon_type(self):
        return self._weapon_type

    def __str__(self):
        return '\n'.join([f'name: {self._name}',
                          f'value: {self._value}',
                          f'info: {self._info}',
                          f'hitdice:{self._hitdice}',
                          f'weapon_type: {self._weapon_type}'])


class Spell(object):
    __slots__ = ['_name', '_value', '_info', '_hitdice', '_spell_type']

    def __init__(self, name, value=0, info='', hitdice=8, spell_type='wisdom'):
        self._name = name
        self._value = value
        self._info = info
        self._hitdice = 0
        self._spell_type = spell_type

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, value):
        self._name = value


    @property
    def value(self):
        return self.value

    @value.setter
    def value(self, value):
        self._value = value

    @property
    def info(self):
        return self._info

    @info.setter
    def info(self, value):
        self._info = value

    @property
    def hitdice(self):
        return self._hitdice

    @hitdice.setter
    def info(self, value):
        self._hitdice = value

    @property
    def spell_type(self):
        return self._spell_type

    @spell_type.setter
    def spell_type(self, value):
        self._spell_type = value

    def __str__(self):
        return '\n'.join([f'name: {self._name}',
                          f'value: {self._value}',
                          f'info: {self._info}',
                          f'hitdice: {self._hitdice}',
                          f'spell_type: {self._spell_type}'])

# Create the character class with certain properties
def character_class_factory(name, properties_list):
    # Create the base character with said properties

    dictionary = {}

    for item in properties_list:
        dictionary[item.name] = property(item.getter, item.setter, item.deleter)

    def asdict(self):
        return self.data

    dictionary['asdict'] = asdict

    def fromdict(self, datadict):
        self.data.update(datadict)

    dictionary['fromdict'] = fromdict

    bases = (UserDict,)

    return type(name, bases, dictionary)


# Add more properties here in the future
# More characters can be added the same way!
FifthEditionCharacter = character_class_factory('FifthEditionCharacter',
                                    [SimpleProperty('name'),
                                     SimpleProperty('race'),
                                     SimpleProperty('character_class'),
                                     SimpleProperty('experience'),
                                     SimpleProperty('level'),
                                     SimpleProperty('armor_class'),
                                     SimpleProperty('initiative'),
                                     SimpleProperty('proficiency_bonus'),
                                     SimpleProperty('inspiration'),
                                     SimpleProperty('hitpoints'),
                                     SimpleProperty('hitdice'),
                                     SimpleProperty('speed'),
                                     SimpleProperty('passive_wisdom'),
                                     SimpleProperty('alignment'),
                                     SimpleProperty('background'),
                                     SimpleProperty('player_name'),
                                     DictionaryProperty('ability_scores'),
                                     DictionaryProperty('saving_throws'),
                                     DictionaryProperty('skills'),
                                     ListProperty('inventory'),
                                     ListProperty('features'),
                                     ListProperty('traits'),
                                     ListProperty('proficient_tools'),
                                     ListProperty('proficient_languages'),
                                     ListProperty('proficient_weapons'),
                                     ListProperty('spell_slots'),
                                     ListProperty('spells'),
                                     SimpleProperty('death_saves'),
                                     SimpleProperty('money'),
                                     SimpleProperty('death_failures')])


def create_fifth_edition_character(**kwargs):
    # Create a character and bind the properties to the class itself
    obj = FifthEditionCharacter()
    obj.name = ''
    obj.player_name = ''
    obj.character_class = ''
    obj.race = ''
    obj.experience = 0
    obj.level = 1
    obj.armor_class = 10
    obj.initiative = 0
    obj.proficiency_bonus = 2
    obj.inspiration = 1
    obj.hitpoints = 1
    obj.hitdice = 8
    obj.speed = 30
    obj.passive_wisdom = 10
    obj.alignment = ''
    obj.background = ''
    obj.death_saves = 0
    obj.death_failures = 0
    obj.money = 0
    obj.ability_scores = [('strength', 10),
                          ('charisma', 10),
                          ('intelligence', 10),
                          ('wisdom', 10),
                          ('constitution',10),
                          ('dexterity', 10)]

    obj.saving_throws = [('strength', 2),
                         ('charisma', 2),
                         ('intelligence', 2),
                         ('wisdom', 2),
                         ('constitution',2),
                         ('dexterity', 2)]

    obj.skills = [('athletics', 2),
                  ('acrobatics', 2),
                  ('arcane', 2),
                  ('nature', 2),
                  ('performance', 2),
                  ('deception', 2),
                  ('persuasion', 2),
                  ('investigation', 2),
                  ('insight', 2),
                  ('religion', 2),
                  ('history', 2),
                  ('survival', 2),
                  ('stealth', 2),
                  ('medicine', 2),
                  ('intimidation', 2),
                  ('perception', 2),
                  ('animal_handling', 2),
                  ('sleight_of_hand', 2)]

    obj.inventory = Item('lockpick', 2, 'open doors')
    obj.spells = ''
    obj.spell_slots = ''
    obj.proficient_tools = ''
    obj.proficient_langauges = ''
    obj.proficient_weapons = ''
    obj.features = ''
    obj.traits = ''



    # Add defaults then overwrite them

    for key,value in kwargs.items():
        obj[key] = value

    return obj



if __name__ == '__main__':
    character = create_fifth_edition_character()
    print(character.inventory)
    character.inventory = Item('bottle', 2, 'store liquids')
    character.inventory = 13
    print(character.inventory)
