import create_character as test
import modify_skills as test1
import storage
import scene


storage.clear()
print('Castle Dungeons - An interactive fiction game in Python')


def intro():
    print("\nIn this adventure, you are the hero. \n")
    print('Your choices, skills, and a bit of luck, will influence the outcoume of the game.\n')
    print('An evil sorcerer is holding your fellow adventurers prisoners.')
    print('Will you succeed to free your friends from the castle dungeons, or peril trying? \n')
    input("Press Enter to start...")


intro()
test.create_character()
test.create_character_skill_sheet()



test1.modify_skills()
print("""
    Congrats! You have completed your character creation!
    Your final character sheet is:

    Name: """ + storage.character_name +
    """
    Race: """ + storage.character_race +
    """
    Class: """ + storage.character_class +
    """ \n
    Strength :""" + str(storage.character_strength) +
    """
    Dexiterity: """ + str(storage.character_dexterity) +
    """
    Magic: """ + str(storage.character_magic) +
    """
    Life: """ + str(storage.character_life) )
input("\nPress Enter to begin your adventure, if you dare...")

scene.scene_1()

