import os

class DynamicMenu:
    def __init__(self, title, options):
        self.title = title
        self.options = options

    def display(self):
        os.system('cls')
        print(self.title)
        print("=" * len(self.title))
        for idx, option in enumerate(self.options, 1):
            print(f"{idx}. {option['text']}")
        print("\n")
    
    def get_choice(self):
        while True:
            try:
                choice = int(input("Enter your choice: "))
                if 1 <= choice <= len(self.options):
                    return choice
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Please enter a valid number.")

    def execute_choice(self):
        choice = self.get_choice()
        self.options[choice-1]['action']()

def town_actions():
    # Define all the functions that correspond to the choices in town
    def visit_tavern():
        print("You visited the tavern.")
        # Your code for visiting the tavern here

    def visit_blacksmith():
        print("You visited the blacksmith.")
        # Your code for visiting the blacksmith here

    # Add other functions as needed

    # Create a town menu instance and display it
    town_menu = DynamicMenu(
        title="You are in the town of Duskwood.",
        options=[
            {"text": "Visit the tavern", "action": visit_tavern},
            {"text": "Visit the blacksmith", "action": visit_blacksmith},
            # Add other menu options as needed
        ]
    )
    town_menu.display()
    town_menu.execute_choice()

town_actions()