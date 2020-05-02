''' Character Class for D and D Character Types '''

# Standard Imports
# None

# Third Party Imports
# None

# Local Imports
from pydungeon import logger
from pydungeon.utils.config import dictionary_transform
from pydungeon.character.characterDeathSaves import CharacterDeathSaves
from pydungeon.character.characterFeatures import CharacterFeatures
from pydungeon.character.characterInformation import CharacterInformation
from pydungeon.character.characterInventory import CharacterInventory
from pydungeon.character.characterProficienciesInLanguages import CharacterProficienciesInLanguages
from pydungeon.character.characterProficienciesInTools import CharacterProficienciesInTools
from pydungeon.character.characterProficienciesInWeapons import CharacterProficienciesInWeapons
from pydungeon.character.characterSavingThrows import CharacterSavingThrows
from pydungeon.character.characterSkills import CharacterSkills
from pydungeon.character.characterSpellAttacks import CharacterSpellAttacks
from pydungeon.character.characterSpells import CharacterSpells
from pydungeon.character.characterTraits import CharacterTraits
from pydungeon.character.characterWeaponAttacks import CharacterWeaponAttacks

'''
CharacterDeathSaves
CharacterFeatures
CharacterInformation
CharacterInventory
CharacterProficienciesInLanguages
CharacterProficienciesInTools
CharacterProficienciesInWeapons
CharacterSavingThrows
CharacterSkills
CharacterSpellAttacks
CharacterSpells
CharacterTraits
CharacterWeaponAttacks
'''

@dictionary_transform
class Character(
    CharacterDeathSaves, CharacterFeatures, CharacterInformation, CharacterInventory, CharacterProficienciesInLanguages, 
CharacterProficienciesInTools, CharacterProficienciesInWeapons, CharacterSavingThrows, CharacterSkills, CharacterSpellAttacks, 
CharacterSpells, CharacterTraits, CharacterWeaponAttacks):


    def getBasicInformation(self):
        return str("Name: " + self.name + "\n" + 
                    "Race: " + self.race + "\n" + 
                    "Class: " + self.charClass + "\n" + 
                    "Level: " + str(self.level) + "\n" +
                    "Background: " + self.background + "\n")

    def getTotalInformation(self):
        #("Physical Traits: ", self.physicalTraits)
        return str("Name: " + self.name + "\n" + 
                    "Race: " + self.race + "\n" + 
                    "Class: " + self.charClass + "\n" + 
                    "Background: " + self.background + "\n" +
                    "Level: " + str(self.level) + "\n" + 
                    "Experience Points: " + str(self.experiencePoints) + "\n" + 
                    "Armor Class: " + str(self.armorClass) + "\n" + 
                    "Initiative: " + str(self.initiative) + "\n" + 
                    "Hit Dice: " + str(self.hitDice) + "\n" + 
                    "Inspiration: " + str(self.inspiration) + "\n" + 
                    "Proficiency Bonus: " + str(self.proficiencyBonus) + "\n" + 
                    "Passive Wisdom: " + str(self.passiveWisdom) + "\n" +  
                    "Saving Throws: " + str(self.savingThrows) + "\n" + 
                    "Allignment: " + str(self.allignment) + "\n" + 
                    "Speed: " + str(self.speed) + "\n" + 
                    "Physical Traits: " + self.getTraitList() + "\n" +
                    "Abilities: " + self.getAbilities() + "\n")

    def getProficiencies(self):
        languageProficiency = self.languageProficiencies
        languageList = ""
        for language in languageList:
            languageList += ("\n\t" + language + ": " + languageList[language])
        
        
        toolProficiency = self.toolProficiencies
        toolsList = ""
        for tool in toolsList:
            toolsList += ("\n\t" + tool + ": " + toolsList[tool])

        
        weaponProficiency = self.weaponProficiencies
        weaponsList = ""
        for weapon in weaponsList:
            weaponsList += ("\n\t" + weapon + ": " + weaponsList[weapon])

        return ("Language Proficiency: \n\t" + languageList + "\n" + "Weapon Proficiency: \n\t" + weaponsList + "\n" + "Tool Proficiency: \n\t" + toolsList + "\n")

    def getTraitList(self):
        physicalTraits = self.physicalTraits
        traitList = ""
        for trait in physicalTraits:
            traitList += ("\n\t" + trait + ": " + physicalTraits[trait])
        return traitList
    
    def getAbilities(self):
        abilities = self.abilities
        abilityList = ""
        for ability in abilityList:
            abilityList += ("\n\t" + ability + ": " + abilityList[ability])
        return abilityList

