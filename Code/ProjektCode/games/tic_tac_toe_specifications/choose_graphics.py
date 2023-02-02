"""
imports
"""

class ChooseGraphicTTT(): # muss ggf keine klasse ein
    """
    global variables
    """
    tic_tac_toe_window = {
        "width": 900,
        "height": 900,
        "titel": "Tic Tac Toe",
        "graphic": "../graphics/tic_tac_toe/Board.png",
        "position":[
            200,  # pos_x
            200 # pos_y
        ],
        "color": (255, 255, 255)
    }

    tic_tac_toe_o = {
        "name": "tic_tac_toe_o",
        "graphic": "../graphics/tic_tac_toe/O.png",
        "position":[
            200,  # pos_x
            200 # pos_y
        ],
    }

    tic_tac_toe_x = {
        "name": "tic_tac_toe_x",
        "graphic": "../graphics/tic_tac_toe/X.png",
        "position":[
            200,  # pos_x
            200 # pos_y
        ],
    }

    tic_tac_toe_o_winning = {
        "name": "tic_tac_toe_o_winning",
        "graphic": "../graphics/tic_tac_toe/WinningO.png",
        "position":[
            200,  # pos_x
            200 # pos_y
        ],
    }

    tic_tac_toe_x_winning = {
        "name": "tic_tac_toe_x_winning",
        "graphic": "../graphics/tic_tac_toe/WinningX.png",
        "position":[
            200,  # pos_x
            200 # pos_y
        ],
    }


        # list which contains all element directories
    game_elements = [
        tic_tac_toe_o,
        tic_tac_toe_x,
        tic_tac_toe_o_winning,
        tic_tac_toe_x_winning
    ]

if __name__ == "__main__":
    print("This file contains the description elements for the game graphics.")