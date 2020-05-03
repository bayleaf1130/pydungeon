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

    obj.inventory = '2 Gold'
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
    character.inventory = 13
    print(character.inventory)
