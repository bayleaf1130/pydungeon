

class CharacterSavingThrows:
    _savingThrows = {}

    # Feature Getter
    @property
    def savingThrows(self):
        return self._savingThrows

    def getSavingThrow(self, attribute):
        return self._savingThrows[attribute]

    def addSavingThrow(self, attribute, saveValue):
        self._savingThrows[attribute] = saveValue

    def removeSavingThrow(attribute):
        self._savingThrows.pop(self, attribute, None)
