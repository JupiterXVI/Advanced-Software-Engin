"""
imports
"""
from sys import path as sys_path

# This class discribes the struckture of the main menu
# which can be accessed form outside
class MainMenu(): # muss ggf keine klasse ein
    """
    global variables
    """
    window = {
        "width": 600,
        "height": 600,
        "titel": "Spielebibliothek",
        "color": (30, 30, 30)
    }

    start_button = {
        "name": "start_button",
        "form": "rectangle",
        "dimensions": [
            50,  # pos_x
            50,  # pos_y
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

    exit_button = {
        "name": "exit_button",
        "form": "rectangle",
        "dimensions": [
            50,  # pos_x
            200, # pos_y
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

    option_button = {
        "name": "option_button",
        "form": "rectangle",
        "dimensions": [
            50,  # pos_x
            350, # pos_y
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

    image_paths = {
        "start_button": sys_path[0] + "\image\start_btn.png",
        "exit_button": sys_path[0] + "\image\exit_btn.png"
    }

    # list which contains all element directories
    window_elements = [
        start_button,
        exit_button,
        option_button
    ]

if __name__ == "__main__":
    print("This file contains the description elements for the main menu.")