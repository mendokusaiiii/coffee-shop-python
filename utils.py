import json

def save_menu(menu):
    with open('data.txt', 'w') as file:
        json.dump(menu, file)

def load_menu():
    try:
        with open('data.txt', 'r') as file:
            menu = json.load(file)
    except FileNotFoundError:
        menu = {}
    return menu
