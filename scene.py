import storage
import combat
import skill_check


def scene_1():
    storage.clear()
    choice = None
    while choice is None:
        user_input = input("""
        You have entered the Castle Dungeons..
        It is dark, however thankfully your torch is lit and 
        you can see up to 20 feet away from you.
        The stone walls are damp, the smell of rats and orcs is strong.
        You walk down a narrow corridor, until you reach a thick stone wall.

        The corridor continues on the left, and on the right.

        What do you do? Enter below the number. 

        1 - Turn left
        2 - Turn right
        > """)

        if user_input == "1":
            choice = "1"
            Scene_2()
        elif user_input == "2":
            choice = "2"
            Scene_3()
        else:
            print("""
            Not a valid choice, type a number """)


def scene_2():
    storage.clear()
    choice = None
    while choice is None:
        user_input = input("""
        From the darkness behind you.. you hear a strange noise.

        What do you do? Enter below the number.

        1 - Continue walking
        2 - Stop to listen 
        > """)
        if user_input == "1":
            choice = "1"
            combat.combat()
        elif user_input == "2":
            choice = "2"
            skill_check.skill_check()
        else:
            print("""
        Not a valid choice, type a number """)


def scene_3():
    storage.clear()
    choice = None
    while choice is None:
        user_input = input("""
    From the darkness ahead of you.. you hear a strange noise.

    What do you do?

    1 - Continue walking
    2 - Stop to listen

    > """)
        if user_input == "1" or user_input == "continue":
            choice = "1"
            combat.combat()
        elif user_input == "2" or user_input == "stop":
             choice = "2"
             skill_check.skill_check()
        else:
             print("""
             Not a valid choice, type a number """)

