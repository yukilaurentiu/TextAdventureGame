import storage


def create_character():
    storage.clear()

    # storage.character_name = 'test 123'
    storage.character_name = input(""" 
        Let's begin by creating your character.
        What is your character name? \n
        >""")
    while storage.character_race is None:
        race_choice = input("""
        choose your character race from the list below by entering the number:
        1 - Elf
        2 - Dwarf \n
        >""")
        if race_choice == "1":
            storage.character_race = "Elf"
        elif race_choice == "2":
            storage.character_race = "Dwarf"
        else:
            print("Not a valid choice, try again")
    storage.clear()
    while storage.character_class is None:
        class_choice = input("""
        Choose your character class from the list below by entering the number:
        1 - Warrior
        2 - Wizard\n
        >""")
        if class_choice == "1":
            storage.character_class = "Warrior"
        elif class_choice == "2":
            storage.character_class = "Wizard"
        else:
            print("Not a valid choice, try again")


def create_character_skill_sheet():
    storage.clear()

    print("""
        Now let's determine your character's skills, which you will use throughout the game.
        In this game, your character has four skills:""")
    input("\n  Press to continue... ")
    print("""
        - Strength, which you will use in combat or any strength test
        - Dexterity, which you will use in any ability test
        - Magic, which you will use whenever you need to cast a spell or use/inspect 
          a magical item or place
        _ Life, which determines your life energy, points will be lost when hurt,
          and whenever life reaches 0, your character dies.
          Depending on your race and class, you will have a certain point-base already 
    calculated by the game.
    You will shortly be able to increase your skills by rolling a 6-face die.
    """)
    input("\n  Press to continue... ")
    print(""" 
        Here is your base Character Skills Sheet: """)

    # storage.character_strength = 5
    # storage.character_magic = 0
    # storage.character_dexterity = 3
    # storage.character_life = 10

    if storage.character_race == "Elf":
        storage.character_strength = storage.character_strength + 3
        storage.character_magic = storage.character_magic + 6
        storage.character_dexterity = storage.character_dexterity + 4
        storage.character_life = storage.character_life + 2
    elif storage.character_race == "Dwarf":
        storage.character_strength = storage.character_strength + 5
        storage.character_life = storage.character_life + 4
    if storage.character_class == "Warrior":
        storage.character_strength = storage.character_strength + 3
        storage.character_life = storage.character_life + 3
    elif storage.character_class == "Wizard":
        storage.character_magic = storage.character_magic + 4

    print("""
    Name: """ + storage.character_name +
    """
    Race: """ + storage.character_race +
    """
    Class: """ + storage.character_class +
    """ 
    Strength :""" + str(storage.character_strength) +
    """
    Dexterity: """ + str(storage.character_dexterity) +
    """
    Magic: """ + str(storage.character_magic) +
    """
    Life: """ + str(storage.character_life))
    input("\nPlease Enter to apply your skills modifiers...")