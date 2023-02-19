"""
imports
"""

class ChooseGraphicSI(): # muss ggf keine klasse ein
    """
    global variables
    """
    space_invadors_window = {
        "width": 900,
        "height": 900,
        "titel": "Space Invadors",
        "graphic": "/images/tv.png",
        "position":[
            200,  # pos_x
            200 # pos_y
        ],
        "color": (255, 255, 255)
    }

    space_invaders_player = {
        "name": "space_invaders_player",
        "graphic": "/images/player.png",
        "position":[
            200,  # pos_x
            200 # pos_y
        ],
        "speed": 3,
        "laser_cooldown": 600,
    }

    space_invaders_extra = {
        "name": "space_invaders_player",
        "graphic": "/images/extra.png",
        "position":[
            200,  # pos_x
            200 # pos_y
        ],
        "value": 500,
        "speed": 3,
    }

    space_invaders_green = {
        "name": "space_invaders_player",
        "graphic": "/images/green.png",
        "position":[
            200,  # pos_x
            200 # pos_y
        ],
        "value": 200,
        "speed": 1,
    }

    space_invaders_red = {
        "name": "space_invaders_player",
        "graphic": "/images/red.png",
        "position":[
            200,  # pos_x
            200 # pos_y
        ],
        "value": 100,
        "speed": 1,
    }

    space_invaders_yellow = {
        "name": "space_invaders_player",
        "graphic": "/images/yellow.png",
        "position":[
            200,  # pos_x
            200 # pos_y
        ],
        "value": 300,
        "speed": 1,
    }

    space_invaders_obstacles = {
        "name": "space_invaders_obstacles",
        "shape": [
                '  xxxxxxx',
                ' xxxxxxxxx',
                'xxxxxxxxxxx',
                'xxxxxxxxxxx',
                'xxxxxxxxxxx',
                'xxx     xxx',
                'xx       xx'],
        "position":[
            200,  # pos_x
            200 # pos_y
        ],
    }

    space_invaders_laser ={
        "name": "space_invadors_laser",
        "position":[
            200,  # pos_x
            200 # pos_y
        ],
        "style": "pygame.Surface((4,20))",
        "color": (255, 255, 255),
        "speed": 3,
    }

        # list which contains all element directories
    game_elements = [
        space_invaders_player,
        space_invaders_extra,
        space_invaders_green,
        space_invaders_red,
        space_invaders_yellow,
        space_invaders_obstacles,
        space_invaders_laser
    ]

if __name__ == "__main__":
    print("This file contains the description elements for the game graphics.")