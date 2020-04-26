from dataclasses import dataclass


''' Character Class for D and D Character Types '''
@dataclass
class CharacterInformation:
    ###  Character Abilities ###
    _name: str = ""
    _race: str = ""
    _charClass: str = ""
    _level: int = 1
    _experiencePoints: int = 0
    _armorClass: int = 0
    _initiative: int = 0
    _health: int = 0
    _hitDice: int = 0
    _inspiration: int = 0
    _proficiencyBonus: int = 0
    _passiveWisdom: int = 0
    _savingThrows: int = 0
    _background: str = ""
    _allignment: str = ""
    _speed: int = 0
    #character Physical Traits

    #lists
    #_inventory: dict
    #_weaponAttacks: dict
    #_spellAttacks: dict
    #_deathSaves: dict
    #_features: dict 
    #_traits: dict #name, about
    #_skills: dict #name, value
    #_spells: dict #name, about, damage, uses
    #_proficienciesInLanguages: list
    #_proficienciesInTools: list
    #_proficienciesInWeapons: list
    #_savingThrows: dict #attributes, number

    #_physicalTraits - Gender, Hair, Eyes, Size, Height, Weight
    _Gender: str = ""
    _Hair: str = ""
    _Eyes: str = ""
    _Size: str = ""
    _Height: str = ""
    _Weight: str = ""

    #character Abilities
    _Strength: int = 0
    _Dexterity: int = 0
    _Constitution: int = 0
    _Intelligence: int = 0
    _Wisdom: int = 0
    _Charisma: int = 0

    ### Getters and Setters ###
    # Name
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, newName):
        self._name = newName

    # Race
    @property
    def race(self):
        return self._race

    @race.setter
    def race(self, newRace):
        self._race = newRace
    
    # Character Class
    @property
    def charClass(self):
        return self._charClass

    @charClass.setter
    def charClass(self, newClass):
        self._charClass = newClass
    
    # Level
    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, newLvl):
        self._level = newLvl
    
    # Experience Points
    @property
    def experiencePoints(self):
        return self._experiencePoints

    @experiencePoints.setter
    def experiencePoints(self, newExp):
        self._experiencePoints = newExp

    # Armor Class
    @property
    def armorClass(self):
        return self._armorClass

    @armorClass.setter
    def armorClass(self, newArmorClass):
        self._armorClass = newArmorClass

    # Initiative
    @property
    def initiative(self):
        return self._initiative

    @initiative.setter
    def initiative(self, newInitiative):
        self._initiative = newInitiative

    # Health
    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, newHealth):
        self._health = newHealth

    # Hit Dice
    @property
    def hitDice(self):
        return self._hitDice

    @hitDice.setter
    def hitDice(self, newHitDice):
        self._hitDice = newHitDice

    # Inspiration: 
    @property
    def inspiration(self):
        return self._inspiration

    @inspiration.setter
    def inspiration(self, newInspiration):
        self._heal_inspiration = newInspiration

    # Proficiency Bonus
    @property
    def proficiencyBonus(self):
        return self._proficiencyBonus

    @proficiencyBonus.setter
    def proficiencyBonus(self, newProficiencyBonus):
        self._proficiencyBonus = newProficiencyBonus

    # Passive Wisdom
    @property
    def passiveWisdom(self):
        return self._passiveWisdom

    @passiveWisdom.setter
    def passiveWisdom(self, newPassiveWisdom):
        self._passiveWisdom = newPassiveWisdom

    # Saving Throws
    @property
    def savingThrows(self):
        return self._savingThrows

    @savingThrows.setter
    def savingThrows(self, newSavingThrows):
        self._savingThrows = newSavingThrows

    # Background
    @property
    def background(self):
        return self._background

    @background.setter
    def background(self, newBackground):
        self._background = newBackground

    # Allignment
    @property
    def allignment(self):
        return self._allignment

    @allignment.setter
    def allignment(self, newAllignment):
        self._allignment = newAllignment

    # Speed
    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, newSpeed):
        self._speed = newSpeed

    # Abilites
    @property
    def abilities(self):
        return {"Strength": self._Strength, "Dexterity": self._Dexterity, "Constitution": self._Constitution, "Intelligence": self._Intelligence, "Wisdom": self._Wisdom, "Charisma": self._Charisma}
    
    # Strength
    @property
    def Strength(self):
        return self._Strength

    @Strength.setter
    def Strength(self, newStr):
        self._Strength = newStr
    
    # Dexterity
    @property
    def Dexterity(self):
        return self._Dexterity

    @Dexterity.setter
    def Dexterity(self, newDex):
        self._Dexterity = newDex
    
    # Constitution
    @property
    def Constitution(self):
        return self._Constitution

    @Constitution.setter
    def Constitution(self, newCon):
        self._Constitution = newCon
          
    # Intelligence 
    @property
    def Intelligence(self):
        return self._Intelligence

    @Intelligence.setter
    def Intelligence(self, newInt):
        self._Intelligence = newInt
    
    # Wisdom
    @property
    def Wisdom(self):
        return self._Wisdom

    @Wisdom.setter
    def Wisdom(self, newWis):
        self._Wisdom = newWis
    
    # Charisma
    @property
    def Charisma(self):
        return self._Charisma

    @Charisma.setter
    def Charisma(self, newCha):
        self._Charisma = newCha
         
    # Physical Traits
    @property
    def physicalTraits(self):
        return {"Gender": self._Gender, "Hair": self._Hair, "Eyes": self._Eyes, "Size": self._Size, "Height": self._Height, "Weight": self._Weight}
    
        
    # Gender
    @property
    def Gender(self):
        return self._Gender

    @Gender.setter
    def Gender(self, newGender):
        self._Gender = newGender
    
    # Hair
    @property
    def Hair(self):
        return self._Hair

    @Hair.setter
    def Hair(self, newHair):
        self._Hair = newHair
    
    # Eyes
    @property
    def Eyes(self):
        return self._Eyes

    @Eyes.setter
    def Eyes(self, newEyes):
        self._Eyes = newEyes
          
    # Size
    @property
    def Size(self):
        return self._Size
 
    @Size.setter
    def Size(self, newSize):
        self._Size = newSize
    
    # Height
    @property
    def Height(self):
        return self._Height

    @Height.setter
    def Height(self, newHeight):
        self._Height = newHeight
    
    # Weight
    @property
    def Weight(self):
        return self._Weight

    @Weight.setter
    def Weight(self, newWeight):
        self._Weight = newWeight
         