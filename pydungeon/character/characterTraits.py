

class CharacterTraits:
    _traits = {}

    # Feature Getter
    @property
    def traits(self):
        return self._traits

    def getTraits(self, traitName):
        return self._traits[traitName]

    def addTrait(self, traitName, about):
        self._traits[traitName] = about

    def removeTrait(traitName):
        self._traits.pop(self, traitName, None)