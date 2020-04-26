from pydungeon.character.character import Character

dwarf_character = Character()

dwarf_character.name = "Dhunmic"
dwarf_character.race = "Dwarf"
dwarf_character.addFeatures("Dwarf", "Can dig really really big holes.")
dwarf_character.addItem("Sword", "Big sword")

print("All Information\n")
print(dwarf_character.getTotalInformation())

print("Vital Information\n")
print(dwarf_character.getBasicInformation())

print("Proficiencies\n")
print(dwarf_character.getProficiencies())