from random import randint
import storage


def modify_skills():
    storage.clear()
    print("To modify your skills, roll a six face die for each of your skills, "
          "and the game will add your score to the relevant skill ")
    input("\nPress Enter to roll for Strength")
    roll = randint(1, 6)
    print("You rolled: " + str(roll))
    storage.character_strength = storage.character_strength + roll
    input("\nPress Enter to roll for Dexterity")
    roll = randint(1, 6)
    print("You rolled: " + str(roll))
    storage.character_dexterity = storage.character_dexterity + roll
    input("\nPress Enter to roll for Life")
    roll = randint(1, 6)
    storage.character_life = storage.character_life + roll
    print("You rolled: " + str(roll))
    input("\nPress Enter to continue... ")
    # clear()
    print("""
    Congrats! You have completed your character creation!
    Your final character sheet is:""")

    # Name: """ + character_name +
    #       """
    #       Race: """ + character_race +
    #       """
    #       Class: """ + character_class +
    #       """ \n
    #       Strength :""" + str(character_strength) +
    #       """
    #       Dexterity: """ + str(character_dexterity) +
    #       """
    #       Magic: """ + str(character_magic) +
    #       """
    #       Life: """ + str(character_life))
    # input("\nPress Enter to begin your adventure, if you dare...")