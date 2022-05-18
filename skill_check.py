import storage
from random import randint
import combat


def skill_check():
    storage.clear()
    print("""
        A giant rock falls from the ceiling, roll a die to see
        if you can dodge it...or you will be crashed by it!
        """)
    roll = randint(1, 6)
    print("  You rolled: " + str(roll))
    if roll + storage.character_dexterity > 7:
        print("""
        You dodge the stone and survive! Danger is not over though..
        The strange noise in the darkness continues, and it feels a lot closer now.. 
        """)
        input("  Press Enter to continue...")
        combat.combat()
    else:
        print("  You are smashed by the rock.. You die. Tha game is over.")
        input("  Press Enter to exit the game.")
