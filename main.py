import sys
import create_character as test
import modify_skills as test1
import storage
import scene

sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=30, cols=110))
sys.stdout.write("\x1b]2;'Castle Dungeons - An interactive fiction game'\x07")
storage.clear()


class color:
    BOLD = '\033[1m'
    END = '\033[0m'


print(color.BOLD + '        Castle Dungeons - An interactive fiction game in Python' + color.END)


def intro():
    print("""
        In this adventure, you are the hero. \n
        Your choices, skills, and a bit of luck, will influence the outcome of the game.\n
        An evil sorcerer is holding your fellow adventurers prisoners.
        Will you succeed to free your friends from the castle dungeons, or peril trying?
        """)
    input("  Press Enter to start...")


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
input("\n  Press Enter to begin your adventure, if you dare...")

scene.scene_1()
