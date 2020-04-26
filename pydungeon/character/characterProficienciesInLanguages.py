

class CharacterProficienciesInLanguages: 
    _languages = {}

    # Feature Getter
    @property
    def languageProficiencies(self):
        return self._languages

    def getLanguageProficiency(self, languageName):
        return self._languages[languageName]

    def addLanguageProficiencies(self, languageName, familiarity):
        self._languages[languageName] = familiarity

    def removeLanguageProficiencies(languageName):
        self._languages.pop(self, languageName, None)