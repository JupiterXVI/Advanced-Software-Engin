"""
imports
"""
from sys import path as sys_path

class MainMenu():
    """
    global variables
    """
    window = {
        "width": 600,
        "height": 600,
        "titel": "Spielebibliothek"
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
            255, # red
            255, # green
            255  # blue
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
            255, # red
            255, # green
            255  # blue
        ],
        "line_thickness": 0  # 0 -> filled; 1 -> thin, 2 -> thicker
    }

    image_paths = {
        "start_button": sys_path[0] + "\image\start_btn.png",
        "exit_button": sys_path[0] + "\image\exit_btn.png"
    }

    window_elements = [
        start_button,
        exit_button,
    ]