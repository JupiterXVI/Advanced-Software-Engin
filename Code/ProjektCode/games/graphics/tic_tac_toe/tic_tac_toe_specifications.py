"""
imports
"""

class ChooseGraphicTTT(): # muss ggf keine klasse ein
    """
    global variables
    """
    positions = [ [[75,75],[370,75],[645,75]],
                  [[75,360],[370,360],[645,360]],
                  [[75,645],[370,645],[645,645]] ]


    tic_tac_toe_window = {
        "width": 900,
        "height": 900,
        "titel": "Tic Tac Toe",
        "position":[
            200,  # pos_x
            200 # pos_y
        ],
        "color": (0, 0, 0)
    }


    tic_tac_toe_board = {
        "name": "tic_tac_toe_board",
        "graphic": "./ProjektCode/games/graphics/tic_tac_toe/images/Board.png",
        "position":[
            -390,  # pos_x
            -390 # pos_y 
        ],
        "dimensions": [
            900, # width
            900  # heigth
        ],
        "who_offten_needed": 1
    }


    tic_tac_toe_o = {
        "name": "tic_tac_toe_o",
        "graphic": "./ProjektCode/games/graphics/tic_tac_toe/images/O.png",
        "position":"not set",
        "dimensions": [
            30, # width
            30  # heigth
        ],
        "who_offten_needed": 5
    }


    tic_tac_toe_x = {
        "name": "tic_tac_toe_x",
        "graphic": "./ProjektCode/games/graphics/tic_tac_toe/images/X.png",
        "position":"not set",
        "dimensions": [
            30, # width
            30  # heigth
        ],
        "who_offten_needed": 5
        
    }


    tic_tac_toe_o_winning = {
        "name": "tic_tac_toe_o_winning",
        "graphic": "./ProjektCode/games/graphics/tic_tac_toe/images/WinningO.png",
        "position":"not set",
        "dimensions": [
            30, # width
            30  # heigth
        ]
    }


    tic_tac_toe_x_winning = {
        "name": "tic_tac_toe_x_winning",
        "graphic": "./ProjektCode/games/graphics/tic_tac_toe/images/WinningX.png",
        "position":"not set",
        "dimensions": [
            30, # width
            30  # heigth
        ]
    }


    """
    functions
    """


if __name__ == "__main__":
    print("This file contains the description elements for the game graphics.")