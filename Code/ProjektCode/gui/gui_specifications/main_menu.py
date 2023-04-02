"""
imports
"""
#from sys import path as sys_path

# This class discribes the struckture of the main menu
# which can be accessed form outside
class MainMenu(): # muss ggf keine klasse ein
    """
    global variables
    """
    window = {
        "width": 900,
        "height": 900,
        "titel": "Spielebibliothek",
        "color": (30, 30, 30)
    }

    choose_game_button = {
        "name": "choose_game",
        "form": "rectangle",
        "text": {
            "content": "Spiel wählen",
            "color": [
                0, # red
                0, # green
                0  # blue
            ],
        },
        "position":[
            200,  # pos_x
            200 # pos_y
        ],
        "dimensions": [
            500, # width
            100  # heigth
        ],
        "color": [
            220, # red
            180, # green
            180  # blue
        ],
        "line_thickness": 0  # 0 -> filled; 1 -> thin, 2 -> thicker
    }

    
    account_button = {
        "name": "account",
        "form": "rectangle",
        "text": {
            "content": "Benutzerverwaltung",
            "color": [
                0, # red
                0, # green
                0  # blue
            ],
        },
        "position":[
            200,  # pos_x
            350 # pos_y
        ],
        "dimensions": [
            500, # width
            100  # heigth
        ],
        "color": [
            180, # red
            180, # green
            220  # blue
        ],
        "line_thickness": 0  # 0 -> filled; 1 -> thin, 2 -> thicker
    }

    exit_button = {
        "name": "exit",
        "form": "rectangle",
        "text": {
            "content": "Beenden",
            "color": [
                0, # red
                0, # green
                0  # blue
            ],
        },
        "position":[
            200,  # pos_x
            500 # pos_y
        ],
        "dimensions": [
            500, # width
            100  # heigth
        ],
        "color": [
            180, # red
            220, # green
            180  # blue
        ],
        "line_thickness": 0  # 0 -> filled; 1 -> thin, 2 -> thicker
    }


    circle_button = {
        "name": "circle",
        "form": "circle",
        "position": [
            430,  # pos_x
            630 # pos_y
        ],
        "dimensions": [
            40, # width
            40  # heigth
        ],
        "radius": 20,
        "color": [
            220, # red
            220, # green
            180  # blue
        ],
        "line_thickness": 0  # 0 -> filled; 1 -> thin, 2 -> thicker
    }

    #image_paths = {
    #    "start_button": sys_path[0] + "\image\start_btn.png",
    #    "exit_button": sys_path[0] + "\image\exit_btn.png"
    #}

    # list which contains all element directories
    window_elements = [
        choose_game_button,
        account_button,
        exit_button,
        circle_button
    ]

if __name__ == "__main__":
    print("This file contains the description elements for the main menu.")