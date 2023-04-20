"""
imports
"""
X_OFFSET = 200
Y_OFFSET = 200
GAME_BUTTON_WIDTH = 500
GAME_BUTTON_HEIGHT = 100
GAME_BUTTON_OFFSET = 50

# This class discribes the struckture of the main menu
# which can be accessed form outside
class ChooseGame(): # muss ggf keine klasse ein
    """
    global variables
    """
    space_invaders = {
        "name": "space_invaders",
        "form": "rectangle",
        "text": {
            "content": "Space Invaders",
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
            GAME_BUTTON_WIDTH, # width
            GAME_BUTTON_HEIGHT  # heigth
        ],
        "color": [
            150, # red
            150, # green
            220  # blue
        ],
        "line_thickness": 0  # 0 -> filled; 1 -> thin, 2 -> thicker
    }


    tic_tac_toe = {
        "name": "tic_tac_toe",
        "form": "rectangle",
        "text": {
            "content": "Tic Tac Toe",
            "font": 0,
            "color": [
                0, # red
                0, # green
                0  # blue
            ],
        },
        "position":[
            X_OFFSET,  # pos_x
            Y_OFFSET + (1*(GAME_BUTTON_HEIGHT+GAME_BUTTON_OFFSET)) # pos_y
        ],
        "dimensions": [
            GAME_BUTTON_WIDTH, # width
            GAME_BUTTON_HEIGHT  # heigth
        ],
        "color": [
            100, # red
            100, # green
            100  # blue
        ],
        "line_thickness": 0  # 0 -> filled; 1 -> thin, 2 -> thicker
    }


    back_button = {
        "name": "start_menu",
        "form": "rectangle",
        "text": {
            "content": "Zurück",
            "font": 0,
            "color": [
                0, # red
                0, # green
                0  # blue
            ],
        },
        "position":[
            X_OFFSET,  # pos_x
            Y_OFFSET + (2*(GAME_BUTTON_HEIGHT+GAME_BUTTON_OFFSET)) # pos_y
        ],
        "dimensions": [
            GAME_BUTTON_WIDTH, # width
            GAME_BUTTON_HEIGHT  # heigth
        ],
        "color": [
            220, # red
            150, # green
            150  # blue
        ],
        "line_thickness": 0  # 0 -> filled; 1 -> thin, 2 -> thicker
    }


    # list which contains all element directories
    window_elements = [
        space_invaders,
        tic_tac_toe,
        back_button
    ]


    """
    functions
    """


if __name__ == "__main__":
    print("This file contains the description elements for the game choice menu.")
    