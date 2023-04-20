"""
imports
"""
HEADLINE_WIDTH = 500
HEADLINE_HEIGHT = 100
HEADLINE_X_OFFSET = 200
HEADLINE_Y_OFFSET = 150
NAME_WIDTH = 200
NAME_HEIGHT = 50
POINT_WIDTH = 100
NAME_X_OFFSET = 210
NAME_Y_OFFSET = 250
POINT_X_OFFSET = 550
ROW_OFFSET = -10
BUTTON_WIDTH = 400
BUTTON_HEIGHT = 100
BUTTON_X_OFFSET = 250
BUTTON_Y_OFFSET = 580


# This class discribes the struckture of the main menu
# which can be accessed form outside
class WinScreen(): # muss ggf keine klasse ein
    """
    global variables
    """
    congretulation = {
        "name": "congretulation",
        "form": "rectangle",
        "text": {
            "content": "Glückwunsch",
            "font": 1,
            "color": [
                230, # red
                180, # green
                10  # blue
            ],
        },
        "position":[
            HEADLINE_X_OFFSET,  # pos_x
            HEADLINE_Y_OFFSET # pos_y
        ],
        "dimensions": [
            HEADLINE_WIDTH, # width
            HEADLINE_HEIGHT  # heigth
        ],
        "color": [
            0, # red
            0, # green
            0  # blue
        ],
        "line_thickness": 0  # 0 -> filled; 1 -> thin, 2 -> thicker
    }

    player0 = {
        "name": "player",
        "form": "rectangle",
        "text": {
            "content": "Player",
            "font": 2,
            "color": [
                255, # red
                255, # green
                255  # blue
            ],
        },
        "position":[
            NAME_X_OFFSET,  # pos_x
            NAME_Y_OFFSET # pos_y
        ],
        "dimensions": [
            NAME_WIDTH, # width
            NAME_HEIGHT  # heigth
        ],
        "color": [
            0, # red
            0, # green
            0  # blue
        ],
        "line_thickness": 0  # 0 -> filled; 1 -> thin, 2 -> thicker
    }

    points0 = {
        "name": "points",
        "form": "rectangle",
        "text": {
            "content": "Points",
            "font": 2,
            "color": [
                255, # red
                255, # green
                255  # blue
            ],
        },
        "position":[
            POINT_X_OFFSET,  # pos_x
            NAME_Y_OFFSET # pos_y
        ],
        "dimensions": [
            POINT_WIDTH, # width
            NAME_HEIGHT  # heigth
        ],
        "color": [
            0, # red
            0, # green
            0  # blue
        ],
        "line_thickness": 0  # 0 -> filled; 1 -> thin, 2 -> thicker
    }

    player1 = {
        "name": "player",
        "form": "rectangle",
        "text": {
            "content": "Player",
            "font": 2,
            "color": [
                255, # red
                255, # green
                255  # blue
            ],
        },
        "position":[
            NAME_X_OFFSET,  # pos_x
            NAME_Y_OFFSET + (1*(NAME_HEIGHT+ROW_OFFSET)) # pos_y
        ],
        "dimensions": [
            NAME_WIDTH, # width
            NAME_HEIGHT  # heigth
        ],
        "color": [
            0, # red
            0, # green
            0  # blue
        ],
        "line_thickness": 0  # 0 -> filled; 1 -> thin, 2 -> thicker
    }

    points1 = {
        "name": "points",
        "form": "rectangle",
        "text": {
            "content": "Points",
            "font": 2,
            "color": [
                255, # red
                255, # green
                255  # blue
            ],
        },
        "position":[
            POINT_X_OFFSET,  # pos_x
            NAME_Y_OFFSET + (1*(NAME_HEIGHT+ROW_OFFSET)) # pos_y
        ],
        "dimensions": [
            POINT_WIDTH, # width
            NAME_HEIGHT  # heigth
        ],
        "color": [
            0, # red
            0, # green
            0  # blue
        ],
        "line_thickness": 0  # 0 -> filled; 1 -> thin, 2 -> thicker
    }

    player2 = {
        "name": "player",
        "form": "rectangle",
        "text": {
            "content": "Player",
            "font": 2,
            "color": [
                255, # red
                255, # green
                255  # blue
            ],
        },
        "position":[
            NAME_X_OFFSET,  # pos_x
            NAME_Y_OFFSET + (2*(NAME_HEIGHT+ROW_OFFSET)) # pos_y
        ],
        "dimensions": [
            NAME_WIDTH, # width
            NAME_HEIGHT  # heigth
        ],
        "color": [
            0, # red
            0, # green
            0  # blue
        ],
        "line_thickness": 0  # 0 -> filled; 1 -> thin, 2 -> thicker
    }

    points2 = {
        "name": "points",
        "form": "rectangle",
        "text": {
            "content": "Points",
            "font": 2,
            "color": [
                255, # red
                255, # green
                255  # blue
            ],
        },
        "position":[
            POINT_X_OFFSET,  # pos_x
            NAME_Y_OFFSET + (2*(NAME_HEIGHT+ROW_OFFSET)) # pos_y
        ],
        "dimensions": [
            POINT_WIDTH, # width
            NAME_HEIGHT  # heigth
        ],
        "color": [
            0, # red
            0, # green
            0  # blue
        ],
        "line_thickness": 0  # 0 -> filled; 1 -> thin, 2 -> thicker
    }

    player3 = {
        "name": "player",
        "form": "rectangle",
        "text": {
            "content": "Player",
            "font": 2,
            "color": [
                255, # red
                255, # green
                255  # blue
            ],
        },
        "position":[
            NAME_X_OFFSET,  # pos_x
            NAME_Y_OFFSET + (3*(NAME_HEIGHT+ROW_OFFSET)) # pos_y
        ],
        "dimensions": [
            NAME_WIDTH, # width
            NAME_HEIGHT  # heigth
        ],
        "color": [
            0, # red
            0, # green
            0  # blue
        ],
        "line_thickness": 0  # 0 -> filled; 1 -> thin, 2 -> thicker
    }

    points3 = {
        "name": "points",
        "form": "rectangle",
        "text": {
            "content": "Points",
            "font": 2,
            "color": [
                255, # red
                255, # green
                255  # blue
            ],
        },
        "position":[
            POINT_X_OFFSET,  # pos_x
            NAME_Y_OFFSET + (3*(NAME_HEIGHT+ROW_OFFSET)) # pos_y
        ],
        "dimensions": [
            POINT_WIDTH, # width
            NAME_HEIGHT  # heigth
        ],
        "color": [
            0, # red
            0, # green
            0  # blue
        ],
        "line_thickness": 0  # 0 -> filled; 1 -> thin, 2 -> thicker
    }

    player4 = {
        "name": "player",
        "form": "rectangle",
        "text": {
            "content": "Player",
            "font": 2,
            "color": [
                255, # red
                255, # green
                255  # blue
            ],
        },
        "position":[
            NAME_X_OFFSET,  # pos_x
            NAME_Y_OFFSET + (4*(NAME_HEIGHT+ROW_OFFSET)) # pos_y
        ],
        "dimensions": [
            NAME_WIDTH, # width
            NAME_HEIGHT  # heigth
        ],
        "color": [
            0, # red
            0, # green
            0  # blue
        ],
        "line_thickness": 0  # 0 -> filled; 1 -> thin, 2 -> thicker
    }

    points4 = {
        "name": "points",
        "form": "rectangle",
        "text": {
            "content": "Points",
            "font": 2,
            "color": [
                255, # red
                255, # green
                255  # blue
            ],
        },
        "position":[
            POINT_X_OFFSET,  # pos_x
            NAME_Y_OFFSET + (4*(NAME_HEIGHT+ROW_OFFSET)) # pos_y
        ],
        "dimensions": [
            POINT_WIDTH, # width
            NAME_HEIGHT  # heigth
        ],
        "color": [
            0, # red
            0, # green
            0  # blue
        ],
        "line_thickness": 0  # 0 -> filled; 1 -> thin, 2 -> thicker
    }

    back_button = {
        "name": "start_menu",
        "form": "rectangle",
        "text": {
            "content": "Weiter",
            "font": 0,
            "color": [
                0, # red
                0, # green
                0  # blue
            ],
        },
        "position":[
            BUTTON_X_OFFSET,  # pos_x
            BUTTON_Y_OFFSET # pos_y
        ],
        "dimensions": [
            BUTTON_WIDTH, # width
            BUTTON_HEIGHT  # heigth
        ],
        "color": [
            150, # red
            120, # green
            100  # blue
        ],
        "line_thickness": 0  # 0 -> filled; 1 -> thin, 2 -> thicker
    }

    player_list = [
        player0,
        player1,
        player2,
        player3,
        player4
        ]
    
    points_list = [
        points0,
        points1,
        points2,
        points3,
        points4
    ]

    # list which contains all element directories
    window_elements = [
        congretulation,
        back_button
    ]


    """
    functions
    """
    

if __name__ == "__main__":
    print("This file contains the description elements for the game choice menu.")
    