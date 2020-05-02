

class CharacterProficienciesInTools: 
    _tools = {}

    # Feature Getter
    @property
    def toolProficiencies(self):
        return self._tools

    def getToolProficiency(self, toolName):
        return self._tools[toolName]

    def addToolProficiency(self, toolName, familiarity):
        self._tools[toolName] = familiarity

    def removeToolProficiency(toolName):
        self._tools.pop(self, toolName, None)