

class CharacterSpellAttacks:
    _spellAttacks = {}

    # Feature Getter
    @property
    def spellAttacks(self):
        return self._spellAttacks

    def getSpellAttack(self, spellName):
        return self._spellAttacks[spellName]

    def addSpellAttack(self, spellName, about, damage):
        self._spellAttacks[spellName] = {"Description": about, "Damage": damage}

    def removeSpellAttack(spellName):
        self._spellAttacks.pop(self, spellName, None)