#Very simple character selection game
characterforgame = input("Choose one as a character for the game: Barbarian, Bard, Cleric, Druid, Fighter, Monk, Paladin, Ranger, Rogue, Sorcerer, Warlock, Wizard: ").lower()

if characterforgame == "barbarian":
    print("You picked Barbarian 🪓. Barbarians are fierce warriors fueled by primal rage!")
elif characterforgame == "bard":
    print("You picked Bard 🎶. Bards weave magic through music and storytelling to inspire and confuse.")
elif characterforgame == "cleric":
    print("You picked Cleric ✝️. Clerics are divine spellcasters who serve the gods and heal the wounded.")
elif characterforgame == "druid":
    print("You picked Druid 🌿. Druids are nature’s guardians, with shapeshifting powers and earth magic.")
elif characterforgame == "fighter":
    print("You picked Fighter ⚔️. Fighters are versatile champions, excelling in physical combat and strategy.")
elif characterforgame == "monk":
    print("You picked Monk 🥋. Monks are martial artists who channel inner energy for swift and powerful strikes.")
elif characterforgame == "paladin":
    print("You picked Paladin 🛡️. Paladins are holy warriors who smite evil and protect the innocent.")
elif characterforgame == "ranger":
    print("You picked Ranger 🏹. Rangers are skilled hunters who master wilderness survival and archery.")
elif characterforgame == "rogue":
    print("You picked Rogue 🗡️. Rogues are stealthy and cunning, striking from the shadows.")
elif characterforgame == "sorcerer":
    print("You picked Sorcerer 🔥. Sorcerers wield raw, untamed magic drawn from their bloodline.")
elif characterforgame == "warlock":
    print("You picked Warlock 🧙. Warlocks are pact-makers who draw power from mysterious patrons.")
elif characterforgame == "wizard":
    print("You picked Wizard 🧙‍♂️. Wizards are masters of arcane magic, studying ancient tomes to control reality itself.")
else:
    print("Invalid character")