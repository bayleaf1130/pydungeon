

class CharacterSpells:
    _spells = {}

    # Feature Getter
    @property
    def spells(self):
        return self._spells

    def getSpells(self, spellName):
        return self._spells[spellName]

    def addSpell(self, spellName, about, damage, uses):
        self._spells[spellName] = {"Description": about, "Damage": damage, "Uses": uses}

    def removeSpell(spellName):
        self._spells.pop(self, spellName, None)