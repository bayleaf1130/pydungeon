import pytest
import os
import random
import string
import json

from pydungeon.utils.config import Config
from pydungeon.character.character import Character


# Lists to choose data from
names = ['', 'Vordic', 'Farran', 'Rorick', 'Van', 'Zed', 'Fleet', 'Willow']
races = ['', 'Dwarf', 'Elf', 'Halfling', 'Tiefling', 'Kenku']
classes = ['', 'Rouge', 'Wizard', 'Warlock', 'Warrior', 'Druid', 'Ranger']

# Create a character with random stats to save and load from
def create_random_character():
    character = Character()
    character.name = random.choice(names)
    character.race = random.choice(races)
    character.charClass = random.choice(classes)
    character.level = random.randint(1, 100)

    def gen_random_background():
        words = []

        def gen_word(len):
            return ''.join([random.choice(string.ascii_letters) for i in range(len)])

        for i in range(500):
            words.append(gen_word(random.randint(1, 12)))
            

        return ((' '.join(words)) + '.')

    
    character.background = gen_random_background()
    character.experiencePoints = random.randint(1, 10000)
    character.armorClass = random.randint(1, 20)
    character.hitDice = random.randint(1, 12)
    character.inspiration = random.randint(1, 5)
    character.allignment = random.choice(['Chaotic Neutral', 'Lawful Evil', 'Angelic', 'Lawful Good'])
    character.speed = random.randint(1,35)
    character.passiveWisdom = random.randint(1,20)
    character.proficiencyBonus = random.randint(1, 6)

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

