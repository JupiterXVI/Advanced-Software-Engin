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
        "form": "rectangle",
        "pos_x": 50,
        "pos_y": 50,
        "width": 500,
        "heigth": 100
    }

    exit_button = {
        "form": "rectangle",
        "pos_x": 50,
        "pos_y": 200,
        "width": 500,
        "heigth": 100
    }

    image_paths = {
        "start_button": sys_path[0] + "\image\start_btn.png",
        "exit_button": sys_path[0] + "\image\exit_btn.png"
    }

    window_elements = [
        start_button,
        exit_button
    ]