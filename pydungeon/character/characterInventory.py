

class CharacterInventory:
    _characterInventoryList = {}

    # Feature Getter
    @property
    def characterInventory(self):
        #for key in self._characterInventoryList:
        #    print(key + ":", self._characterInventoryList[key])
        return self._characterInventoryList

    def getItem(self, itemName):
        return self._characterInventoryList[itemName]

    def addItem(self, itemName, about):
        self._characterInventoryList[itemName] =  about

    def removeItem(itemName):
        self._characterInventoryList.pop(self, itemName, None)