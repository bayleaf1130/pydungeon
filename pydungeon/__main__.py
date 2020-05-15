''' The main entry point '''

# Standard Imports
import sys

# Third Party Imports
# None

# Local Imports
from pydungeon import logger
from pydungeon.character.character import Character
from pydungeon.gui.application import GuiApplication
# from pydungeon.gui.application import GuiApplication

if __name__ == '__main__':
    GuiApplication().run()
    '''
    dwarf_character = Character()

    dwarf_character.name = "Dhunmic"
    dwarf_character.race = "Dwarf"
    dwarf_character.addFeatures("Dwarf", "Can dig really really big holes.")
    dwarf_character.addSavingThrow('strength', 15)
    dwarf_character.addItem("Sword", "Big sword")

    print("All Information\n")
    print(dwarf_character.getTotalInformation())

    print("Vital Information\n")
    print(dwarf_character.getBasicInformation())

    print("Proficiencies\n")
    print(dwarf_character.getProficiencies())

    print("Features\n")
    print(dwarf_character.characterFeatures)

    print("Saving Throws\n")
    print(dwarf_character.savingThrows)

    #GuiApplication().run()

    from pprint import pprint
    pprint(dwarf_character.asdict())
    
    another_character = Character()
    another_character.fromdict(dwarf_character.asdict())
    pprint(another_character.asdict())
    '''
