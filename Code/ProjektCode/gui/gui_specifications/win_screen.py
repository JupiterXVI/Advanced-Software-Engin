"""
imports
"""
#from sys import path as sys_path

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
            200,  # pos_x
            150 # pos_y
        ],
        "dimensions": [
            500, # width
            100  # heigth
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
            210,  # pos_x
            250 # pos_y
        ],
        "dimensions": [
            200, # width
            50  # heigth
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
            550,  # pos_x
            250 # pos_y
        ],
        "dimensions": [
            100, # width
            50  # heigth
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
            210,  # pos_x
            290 # pos_y
        ],
        "dimensions": [
            200, # width
            50  # heigth
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
            550,  # pos_x
            290 # pos_y
        ],
        "dimensions": [
            100, # width
            50  # heigth
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
            210,  # pos_x
            330 # pos_y
        ],
        "dimensions": [
            200, # width
            50  # heigth
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
            550,  # pos_x
            330 # pos_y
        ],
        "dimensions": [
            100, # width
            50  # heigth
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
            210,  # pos_x
            370 # pos_y
        ],
        "dimensions": [
            200, # width
            50  # heigth
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
            550,  # pos_x
            370 # pos_y
        ],
        "dimensions": [
            100, # width
            50  # heigth
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
            210,  # pos_x
            410 # pos_y
        ],
        "dimensions": [
            200, # width
            50  # heigth
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
            550,  # pos_x
            410 # pos_y
        ],
        "dimensions": [
            100, # width
            50  # heigth
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
            250,  # pos_x
            580 # pos_y
        ],
        "dimensions": [
            400, # width
            100  # heigth
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
    