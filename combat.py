import storage
from random import randint


def combat():
    storage.clear()
    print("A horrible orc attacks you!")
    input("Press Enter to combat...")
    orc = [14, 15]
    while orc[1] > 0 and storage.character_life > 0:
        char_roll = randint(1, 6)
        print("You rolled: " + str(char_roll))
        monst_roll = randint(1, 6)
        print("The monster rolled: " + str(monst_roll))
        if char_roll + storage.character_strength >= monst_roll + orc[0]:
            print("You hit the monster!")
            orc[1] = orc[1] - randint(1, 6)
            input("Press Enter to continue the combat...")
        else:
            print("The monster hits you!")
            storage.character_life = storage.character_life - randint(1, 6)
            print(storage.character_life)
            input("Press Enter to continue the combat...")
    if storage.character_life > 0:
        print("You defeated the orc, congratulations!")
        input("Press Enter to exit the game")
    else:
        print("You lost.. your friends will never be freed..and you dead.")
        input("Press Enter to exit the game")
