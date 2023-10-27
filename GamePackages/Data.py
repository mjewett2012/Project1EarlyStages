import csv
import sys

FILENAME = "character_data.csv"

def load_characters():
    try:
        characters = []
        with open(FILENAME, newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                characters.append(row)
        return characters
    except FileNotFoundError as e:
        return characters
    except Exception as e:
        print(type(e), e)
        sys.exit()

def save_characters(characters):
    try:
        with open(FILENAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(characters)
    except OSError as e:
        print(type(e), e)
        sys.exit()
    except Exception as e:
        print(type(e), e)
        sys.exit()