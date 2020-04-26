

class CharacterProficienciesInWeapons: 
    _weapons = {}

    # Feature Getter
    @property
    def weaponProficiencies(self):
        return self._weapons

    def getWeaponProficiency(self, weaponName):
        return self._weapons[weaponName]

    def addWeaponProficiency(self, weaponName, familiarity):
        self._weapons[weaponName] = familiarity

    def removeWeaponProficiency(weaponName):
        self._weapons.pop(self, weaponName, None)