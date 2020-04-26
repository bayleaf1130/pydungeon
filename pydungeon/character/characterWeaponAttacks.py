

class CharacterWeaponAttacks:
    _weaponAttacks = {}

    # Feature Getter
    @property
    def weaponAttacks(self):
        return self._weaponAttacks

    def getWeaponAttack(self, itemName):
        return self._weaponAttacks[itemName]

    def addWeaponAttack(self, attackName, about, damage):
        self._weaponAttacks[attackName] = {"Description": about, "Damage": damage}

    def removeWeaponAttack(attackName):
        self._weaponAttacks.pop(self, attackName, None)