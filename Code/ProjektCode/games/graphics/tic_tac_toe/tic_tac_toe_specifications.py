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
        "graphic": "./ProjektCode/games/graphics/tic_tac_toe/images/Board.png",
        "position":[
            200,  # pos_x
            200 # pos_y
        ],
        "color": (0, 0, 0)
    }

    tic_tac_toe_o = {
        "name": "tic_tac_toe_o",
        "graphic": "./ProjektCode/games/graphics/tic_tac_toe/images/O.png",
        "position":[
            100,  # pos_x
            200 # pos_y 
        ],
        "dimensions": [
            20, # width
            20  # heigth
        ],
        "who_offten_needed": 5
    }

    tic_tac_toe_x = {
        "name": "tic_tac_toe_x",
        "graphic": "./ProjektCode/games/graphics/tic_tac_toe/images/X.png",
        "position":[
            200,  # pos_x
            200 # pos_y
        ],
        "dimensions": [
            20, # width
            20  # heigth
        ],
        "who_offten_needed": 5
        
    }

    tic_tac_toe_o_winning = {
        "name": "tic_tac_toe_o_winning",
        "graphic": "./ProjektCode/games/graphics/tic_tac_toe/images/WinningO.png",
        "position":[
            200,  # pos_x
            200 # pos_y
        ],
    }

    tic_tac_toe_x_winning = {
        "name": "tic_tac_toe_x_winning",
        "graphic": "./ProjektCode/games/graphics/tic_tac_toe/images/WinningX.png",
        "position":[
            200,  # pos_x
            200 # pos_y
        ],
    }


        # list which contains all element directories
    game_elements = [
        tic_tac_toe_o,
        tic_tac_toe_x,
        #tic_tac_toe_o_winning,
        #tic_tac_toe_x_winning
    ]

if __name__ == "__main__":
    print("This file contains the description elements for the game graphics.")