"""
imports
"""
#from sys import path as sys_path

# This class discribes the struckture of the main menu
# which can be accessed form outside
class ChooseGame(): # muss ggf keine klasse ein
    """
    global variables
    """
    window = {
        "width": 900,
        "height": 900,
        "titel": "Spielebibliothek",
        "color": (30, 30, 30)
    }

    space_invaders = {
        "name": "space_invaders_button",
        "form": "rectangle",
        "text": {
            "content": "Space Invaders",
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
            150, # red
            150, # green
            220  # blue
        ],
        "line_thickness": 0  # 0 -> filled; 1 -> thin, 2 -> thicker
    }

    
    tic_tac_toe = {
        "name": "tic_tac_toe_button",
        "form": "rectangle",
        "text": {
            "content": "Tic Tac Toe",
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
            100, # red
            100, # green
            100  # blue
        ],
        "line_thickness": 0  # 0 -> filled; 1 -> thin, 2 -> thicker
    }

    back_button = {
        "name": "back_button",
        "form": "rectangle",
        "text": {
            "content": "Zurück",
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
            220, # red
            150, # green
            150  # blue
        ],
        "line_thickness": 0  # 0 -> filled; 1 -> thin, 2 -> thicker
    }

    #image_paths = {
    #}

    # list which contains all element directories
    window_elements = [
        space_invaders,
        tic_tac_toe,
        back_button
    ]

if __name__ == "__main__":
    print("This file contains the description elements for the game choice menu.")