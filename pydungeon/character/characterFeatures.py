

class CharacterFeatures:
    _characterFeaturesList = {}

    # Feature Getter
    @property
    def characterFeatures(self):
        return self._characterFeaturesList

    def addFeatures(self, featureName, about):
        self._characterFeaturesList[featureName] =  about

    def removeFeatures(featureName):
        self._characterFeaturesList.pop(self, featureName, None)

