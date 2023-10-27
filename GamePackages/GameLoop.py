# This is the main game loop. It is responsible for running the game.
#
# Parameters: character - The character object that the player has selected to play the game with.
#
# Return: None
#
# Example:
# game_loop(character)

import os


def game_loop(character):
    print("You have started your adventure!\n")
    print("Your character is: ")
    print("Name: " + character.name)
    print("Class: " + character.character_class)
    print("Strength: " + str(character.strength))
    print("Dexterity: " + str(character.dexterity))
    print("Intelligence: " + str(character.intelligence))
    print("Wisdom: " + str(character.wisdom))
    print("Constitution: " + str(character.constitution))
    print("Weapon: " + character.weapon)
    print("Armor: " + character.armor)
    print("Defense: " + str(character.defense))
    print("Attack: " + str(character.attack))
    print("Hit Points: " + str(character.hitPoints))
    print("Magic Points: " + str(character.magicPoints))
    print("Level: " + str(character.level))
    print("Experience: " + str(character.experience))
    print("Gold: " + str(character.gold))
    
    input("Press Enter to continue...")

    # Clearing the Screen
    os.system('cls')


