
class CharacterDeathSaves:
    _deathSaves = {}

    # Feature Getter
    @property
    def deathSaves(self):
        return self._deathSaves

    def getDeathSave(self, attribute):
        return self._deathSaves[attribute]

    def addDeathSave(self, attribute, saveValue):
        self._deathSaves[attribute] = saveValue

    def removeDeathSave(attribute):
        self._deathSaves.pop(self, attribute, None)

