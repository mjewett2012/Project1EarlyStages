import os
from GamePackages.Models.CharacterModel import playerCharacter
from GamePackages.Menu import display_main_menu, display_class_select
from GamePackages.Data import save_characters
from GamePackages.Utility import dice_roller, exit_program
from datetime import date


WIDTH = 60  # Menu width

def class_choice():
    while True:        
        classChoice = input("What is your choice? ")
        if classChoice.lower() == "warrior":
            myClass = "Warrior"
        elif classChoice.lower() == "rogue":
            myClass = "Rogue"
        elif classChoice.lower() == "priest":
            myClass = "Priest"
        elif classChoice.lower() == "wielder":
            myClass = "Wielder"
        else:
            print("Not a valid class. Please try again.\n You can do it!\n")
            continue    
        
        print(f"You have chosen {myClass}.\n Is this correct? (y/n)")
        classChoice = input("Selection: ")
        if classChoice.lower() == "y":
            os.system('cls')
            return myClass
        elif classChoice.lower() == "n":
            os.system('cls')
            display_class_select()
            continue
        else:
            print("Not a valid selection. Please try again.\n")
            return        

def name_choice(characters):
    while True:    
        name = input("Enter you Character's Name (8 Characters Max): ")
        if len(name) > 8:
            print("Name is too long. Please try again.\n")
            return
        for character in characters:
            if name == character[0]:
                print("That name is already taken. Please try again.\n")
                return  
        print(f"You have chosen {name}.\n Is this correct? (y/n)")
        nameChoice = input("Selection: ")
        if nameChoice.lower() == "y":
            os.system('cls')
            return name
        elif nameChoice.lower() == "n":
            os.system('cls')
            continue

def stat_roller(myClass):
    while True:
        try:
            if myClass == "Warrior":
                strRoll = dice_roller(1, 6) + dice_roller(1, 6) + dice_roller(1, 6) + 3
                dexRoll = dice_roller(1, 6) + dice_roller(1, 6) + dice_roller(1, 6)
                intRoll = dice_roller(1, 6) + dice_roller(1, 6) + dice_roller(1, 6) - 3
                wisRoll = dice_roller(1, 6) + dice_roller(1, 6) + dice_roller(1, 6) - 3
                conRoll = dice_roller(1, 6) + dice_roller(1, 6) + dice_roller(1, 6) + 5
            elif myClass == "Rogue":
                strRoll = dice_roller(1, 6) + dice_roller(1, 6) + dice_roller(1, 6) + 1
                dexRoll = dice_roller(1, 6) + dice_roller(1, 6) + dice_roller(1, 6) + 3
                intRoll = dice_roller(1, 6) + dice_roller(1, 6) + dice_roller(1, 6) - 1
                wisRoll = dice_roller(1, 6) + dice_roller(1, 6) + dice_roller(1, 6) - 3
                conRoll = dice_roller(1, 6) + dice_roller(1, 6) + dice_roller(1, 6) + 1
            elif myClass == "Priest":
                strRoll = dice_roller(1, 6) + dice_roller(1, 6) + dice_roller(1, 6)
                dexRoll = dice_roller(1, 6) + dice_roller(1, 6) + dice_roller(1, 6) 
                intRoll = dice_roller(1, 6) + dice_roller(1, 6) + dice_roller(1, 6) + 3
                wisRoll = dice_roller(1, 6) + dice_roller(1, 6) + dice_roller(1, 6) + 3
                conRoll = dice_roller(1, 6) + dice_roller(1, 6) + dice_roller(1, 6) 
            elif myClass == "Wielder":
                strRoll = dice_roller(1, 6) + dice_roller(1, 6) + dice_roller(1, 6) - 1
                dexRoll = dice_roller(1, 6) + dice_roller(1, 6) + dice_roller(1, 6) - 1
                intRoll = dice_roller(1, 6) + dice_roller(1, 6) + dice_roller(1, 6) + 5
                wisRoll = dice_roller(1, 6) + dice_roller(1, 6) + dice_roller(1, 6) + 3
                conRoll = dice_roller(1, 6) + dice_roller(1, 6) + dice_roller(1, 6) - 1
            print(f"Your stats are:\nStrength: {strRoll}\nDexterity: {dexRoll}\nIntelligence: {intRoll}\nWisdom: {wisRoll}\nConstitution: {conRoll}\n")
            print("Are you happy with these stats? (y/n)")
            statChoice = input("Selection: ")
            if statChoice.lower() == "y":
                os.system('cls')
                break
            elif statChoice.lower() == "n":
                os.system('cls')
                continue
            else:
                print("Not a valid selection. Please try again.\n")
                return
        except Exception as e:
            print(f"Something went wrong in the stat roller\n myClass = {myClass}\n strRoll = {strRoll}\n dexRoll = {dexRoll}\n intRoll = {intRoll}\n wisRoll = {wisRoll}\n conRoll = {conRoll}\n")
            log_file = open("error_log.txt", "a")
            log_file.write(f"{date.today()} Something went wrong in the stat roller\n myClass = {myClass}\n strRoll = {strRoll}\n dexRoll = {dexRoll}\n intRoll = {intRoll}\n wisRoll = {wisRoll}\n conRoll = {conRoll}\n")
            log_file.close()
            exit_program()
            
    return strRoll, dexRoll, intRoll, wisRoll, conRoll

def stat_calculator(myClass, strength, dexterity, intelligence, wisdom, constitution):
    if myClass == "Warrior":
        defense = 10 + dexterity/10
        attack = 10 + strength/10
        hitPoints = 10 + constitution/10
        magicPoints = 10 + intelligence/10
    elif myClass == "Rogue":
        defense = 10 + dexterity/10
        attack = 10 + strength/10
        hitPoints = 10 + constitution/10
        magicPoints = 10 + intelligence/10
    elif myClass == "Priest":
        defense = 10 + dexterity/10
        attack = 10 + strength/10
        hitPoints = 10 + constitution/12
        magicPoints = 10 + intelligence/7
    elif myClass == "Wielder":
        defense = 10 + dexterity/12
        attack = 10 + strength/12
        hitPoints = 10 + constitution/10
        magicPoints = 10 + intelligence/6
    return defense, attack, hitPoints, magicPoints

def weapon_choice(myClass):
    if myClass == "Warrior":
        weapon = "Wooden Sword"
    elif myClass == "Rogue":
        weapon = "Wooden Dagger"
    elif myClass == "Priest":
        weapon = "Wooden Staff"
    elif myClass == "Wielder":
        weapon = "Wooden Wand"
    return weapon

def armor_choice(myClass):
    if myClass == "Warrior":
        armor = "Leather Armor"
    elif myClass == "Rogue":
        armor = "Leather Armor"
    elif myClass == "Priest":
        armor = "Acolyte Robes"
    elif myClass == "Wielder":
        armor = "Simple Robes"
    return armor

def get_password():
    while True:
        password = input("Enter a password for your character: ")
        password2 = input("Re-enter your password: ")
        if password == password2:
            os.system('cls')
            return password
        else:
            os.system('cls')
            print("Passwords do not match. Please try again.\n")

def delete_character(characters):
    while True:
        if len(characters) == 0:
            print("There are no characters to delete.\n")
            display_main_menu()
            return
        else:
            list_characters(characters)
            print("Which character would you like to delete?")
            try:
                number = int(input("Number: "))
            except ValueError:
                print("Invalid character numberlist. Please try again.")
                continue
            if number < 1 or number > len(characters):
                print("There is no character with that number. Please try again.")
            else:
                break
    character = characters.pop(number - 1)
    save_characters(characters)
    list_characters(characters)
    print(f"{character[0]} was deleted.\n")
    input("Press Enter to continue...")
    display_main_menu()

def ordinal_suffix_of(i):
    j = i % 10
    k = i % 100
    if (j == 1 and k != 11):
        return str(i) + "st"
    if (j == 2 and k != 12):
        return str(i) + "nd"
    if (j == 3 and k != 13):
        return str(i) + "rd"
    return str(i) + "th"

def format_character_line(index, name, ordinal, type_name):
    # Create the string
    content_str = f"{index}. {name} the {ordinal} Level {type_name}"
    # Center the string within the WIDTH, between the bars
    return f"|{content_str.center(WIDTH - 2)}|"

def list_characters(characters):
    # Display a numbered list of characters in the following format:
    # name, level, class
    # Example: 1. Bob the 1st Level Warrior or 1. Bob the 2nd Level Warrior
    # oridinal_suffix_of(i) accounts for 1st, 2nd, 3rd, 4th, etc.
    # format_character_line(index, name, ordinal, type_name) formats the character line
    # for the list
    
    if len(characters) == 0:
        print("There are no characters to display.\n")
        input("Press Enter to continue...")
        display_main_menu()
        return
    else:
        os.system('cls')

    # Print title and top line
    title = "CHARACTER LIST".center(WIDTH - 2, ' ')  # -2 for the pipes
    print(f"{'='*WIDTH}")
    print(f"|{title}|")
    print(f"{'='*WIDTH}")

    # Print characters
    for i in range(len(characters)):
        char_name = characters[i][0]
        char_level = ordinal_suffix_of(int(characters[i][13]))
        char_type = characters[i][1]
        print(format_character_line(i+1, char_name, char_level, char_type))

    # Print bottom line
    print(f"{'='*WIDTH}")
    print()
    input("Press Enter to continue...")
    display_main_menu()
    
def create_character(characters):
    display_class_select()
    myClass = class_choice()
    myName = name_choice(characters)
    strength, dexterity, intelligence, wisdom, constitution = stat_roller(myClass)
    weapon = weapon_choice(myClass)
    armor = armor_choice(myClass)
    defense, attack, hitPoints, magicPoints = stat_calculator(myClass, strength, dexterity, intelligence, wisdom, constitution)
    level = 1
    experience = 0
    gold = 0
    pWord = get_password()
    character = [myName, myClass, strength, dexterity, intelligence, wisdom, constitution, weapon, armor, defense, attack, hitPoints, magicPoints, level, experience, gold, pWord]
    characters.append(character)
    save_characters(characters)
    print(f"{myName} the {myClass} has been created.\n")
    print()
    input("Press Enter to continue...")
    display_main_menu()

def select_character(characters):
    list_characters(characters)
    print()
    print("Enter the number of the character you wish to play as.")
    print("Or enter 0 to return to the main menu.")
    while True:
        try:
            selection = int(input("Selection: "))
            if selection == 0:
                display_main_menu()
                return
            elif selection < 0 or selection > len(characters):
                print("Not a valid selection. Please try again.\n")
            else:
                break
        except ValueError:
            print("Not a valid selection. Please try again.\n")
    character = characters[selection - 1]
    print("You have selected {} the {}.".format(character[0], character[1]))
    print("Enter the password for this character.")
    while True:
        password = input("Password: ")
        if password == str(character[16]):
            print(f"Welcome back, {character[0]}!\nYour adventure continues...")
            selectedCharacter = playerCharacter.from_list(character)
            return selectedCharacter
        else:
            print("Incorrect password. Please try again.")
            continue



