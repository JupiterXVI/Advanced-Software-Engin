"""
imports
"""
X_OFFSET = 200
Y_OFFSET = 200
BUTTON_WIDTH = 500
BUTTON_HEIGHT = 100
BUTTON_OFFSET = 50
CIRCLE_RADIUS = 20
CIRCLE_X_OFFSET = 430
CIRCLE_Y_OFFSET = 630

# This class discribes the struckture of the main menu
# which can be accessed form outside
class Start(): # muss ggf keine klasse ein
    """
    global variables
    """
    choose_game_button = {
        "name": "choose_game",
        "form": "rectangle",
        "text": {
            "content": "Spiel wählen",
            "font": 0,
            "color": [
                0, # red
                0, # green
                0  # blue
            ],
        },
        "position":[
            X_OFFSET,  # pos_x
            Y_OFFSET # pos_y
        ],
        "dimensions": [
            BUTTON_WIDTH, # width
            BUTTON_HEIGHT  # heigth
        ],
        "color": [
            220, # red
            180, # green
            180  # blue
        ],
        "line_thickness": 0  # 0 -> filled; 1 -> thin, 2 -> thicker
    }

    
    account_button = {
        "name": "manage_account",
        "form": "rectangle",
        "text": {
            "content": "Benutzerverwaltung",
            "font": 0,
            "color": [
                0, # red
                0, # green
                0  # blue
            ],
        },
        "position":[
            X_OFFSET,  # pos_x
            Y_OFFSET + (1*(BUTTON_HEIGHT+BUTTON_OFFSET))  # pos_y
        ],
        "dimensions": [
            BUTTON_WIDTH, # width
            BUTTON_HEIGHT # heigth
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
            "font": 0,
            "color": [
                0, # red
                0, # green
                0  # blue
            ],
        },
        "position":[
            X_OFFSET,  # pos_x
            Y_OFFSET + (2*(BUTTON_HEIGHT+BUTTON_OFFSET))  # pos_y
        ],
        "dimensions": [
            BUTTON_WIDTH, # width
            BUTTON_HEIGHT # heigth
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
            CIRCLE_X_OFFSET,  # pos_x
            CIRCLE_Y_OFFSET # pos_y
        ],
        "dimensions": [
            2*CIRCLE_RADIUS, # width
            2*CIRCLE_RADIUS  # heigth
        ],
        "radius": CIRCLE_RADIUS,
        "color": [
            220, # red
            220, # green
            180  # blue
        ],
        "line_thickness": 0  # 0 -> filled; 1 -> thin, 2 -> thicker
    }

    # list which contains all element directories
    window_elements = [
        choose_game_button,
        account_button,
        exit_button,
        circle_button
    ]


    """
    functions
    """
    

if __name__ == "__main__":
    print("This file contains the description elements for the main menu.")
    