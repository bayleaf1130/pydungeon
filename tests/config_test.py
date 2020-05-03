import pytest
import os
import random
import string
import json

from pydungeon.utils.config import Config
from pydungeon.character.character import create_fifth_edition_character


# Lists to choose data from
names = ['', 'Vordic', 'Farran', 'Rorick', 'Van', 'Zed', 'Fleet', 'Willow']
races = ['', 'Dwarf', 'Elf', 'Halfling', 'Tiefling', 'Kenku']
classes = ['', 'Rouge', 'Wizard', 'Warlock', 'Warrior', 'Druid', 'Ranger']

# Create a character with random stats to save and load from
def create_random_character():
    character = create_fifth_edition_character()
    character.name = random.choice(names)
    character.race = random.choice(races)
    character.character_class = random.choice(classes)
    character.level = random.randint(1, 100)

    def gen_random_background():
        words = []

        def gen_word(len):
            return ''.join([random.choice(string.ascii_letters) for i in range(len)])

        for i in range(500):
            words.append(gen_word(random.randint(1, 12)))


        return ((' '.join(words)) + '.')


    character.background = gen_random_background()
    character.experience = random.randint(1, 10000)
    character.armor_class = random.randint(1, 20)
    character.hitdice = random.randint(1, 12)
    character.inspiration = random.randint(1, 5)
    character.alignment = random.choice(['Chaotic Neutral', 'Lawful Evil', 'Angelic', 'Lawful Good'])
    character.speed = random.randint(1,35)
    character.passive_wisdom = random.randint(1,20)
    character.proficiency = random.randint(1, 6)

    character.money = random.randint(1,1000)
    character.death_saves = random.randint(1,3)
    character.death_failures = random.randint(1,3)
    character.inventory = 'item 1'
    character.inventory = 'item 2'
    character.inventory = 'item 3'

    character.spells = 'fireball'
    character.spells = 'icebeam'
    character.spell_slots = 'icebeam'

    # Add the weird stuff

    return character


# The actual test
@pytest.mark.character
def test_character_configuration():
    character = create_random_character()
    data_dict = character.asdict()
    filename = character.name + '_config' + '.yaml'
    configuration = Config(filename)
    configuration.save(data_dict)

    # Assert that the file exists
    current_path = os.getcwd()
    file_string = os.path.join(current_path, filename)

    assert os.path.exists(file_string) == True

    # Now reload the data
    reloaded_dict = configuration.load()

    # Now remove the file for good measure
    os.remove(file_string)

    first_string = json.dumps(data_dict, sort_keys=True)
    second_string = json.dumps(reloaded_dict, sort_keys=True)

    # Test that the dict strings are the same
    assert first_string == second_string

