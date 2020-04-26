

class CharacterSkills:
    _skills = {}

    # Feature Getter
    @property
    def skills(self):
        return self._skills

    def getskills(self, skillName):
        return self._skills[skillName]

    def addskill(self, skillName, about):
        self._skills[skillName] = about

    def removeskill(skillName):
        self._skills.pop(self, skillName, None)