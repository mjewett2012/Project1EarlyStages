from GamePackages.Menu import display_main_menu, display_title_graphics
from GamePackages.CharacterManagement import list_characters, create_character, delete_character, exit_program, select_character
from GamePackages.Data import load_characters
from GamePackages.GameLoop import game_loop

def main():
    display_title_graphics()
    input("Press Enter to continue...")
    display_main_menu()
    characters = load_characters()
    while True:        
        command = input("Selection: ")
        if command.lower() == "list":
            list_characters(characters)
        elif command.lower() == "add":
            create_character(characters)
        elif command.lower() == "del":
            delete_character(characters)
        elif command.lower() == "start":
            list_characters(characters)
            selection = input("Select a character to begin your adventure: ")
            selected = select_character(characters)
            game_loop(selected)
                            
        elif command.lower() == "quit":
            exit_program()
            break
        else:
            print("Not a valid selection. Please try again.\n")
    print("Fare thee well!")

if __name__ == "__main__":
    main()