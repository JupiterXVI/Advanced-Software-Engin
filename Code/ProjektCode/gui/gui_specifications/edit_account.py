"""
imports
"""
#from sys import path as sys_path

# This class discribes the struckture of the main menu
# which can be accessed form outside
class EditAccount(): # muss ggf keine klasse ein
    """
    global variables
    """
    window = {
        "width": 900,
        "height": 900,
        "titel": "Spielebibliothek",
        "color": (30, 30, 30)
    }

    title_username = {
        "name": "title_username",
        "form": "rectangle",
        "text": {
            "content": "Username:",
            "color": [
                250, # red
                250, # green
                250  # blue
            ],
        },
        "position":[
            200,  # pos_x
            100   # pos_y
        ],
        "dimensions": [
            1, # width
            100  # heigth
        ],
        "color": [
            30, # red
            30, # green
            30  # blue
        ],
        "line_thickness": 0  # 0 -> filled; 1 -> thin, 2 -> thicker
    }

    input_username = {
        "name": "input_username",
        "form": "rectangle",
        "text": {
            "content": "USERNAME",
            "color": [
                0, # red
                0, # green
                0  # blue
            ],
        },
        "position":[
            410,  # pos_x
            100   # pos_y
        ],
        "dimensions": [
            375, # width
            100  # heigth
        ],
        "color": [
            220, # red
            220, # green
            150  # blue
        ],
        "line_thickness": 0  # 0 -> filled; 1 -> thin, 2 -> thicker
    }

    title_password = {
        "name": "title_password",
        "form": "rectangle",
        "text": {
            "content": "Passwort:",
            "color": [
                250, # red
                250, # green
                250  # blue
            ],
        },
        "position":[
            190,  # pos_x
            225   # pos_y
        ],
        "dimensions": [
            1, # width
            100  # heigth
        ],
        "color": [
            30, # red
            30, # green
            30  # blue
        ],
        "line_thickness": 0  # 0 -> filled; 1 -> thin, 2 -> thicker
    }

    input_password = {
        "name": "input_password",
        "form": "rectangle",
        "text": {
            "content": "Passwort",
            "color": [
                0, # red
                0, # green
                0  # blue
            ],
        },
        "position":[
            410,  # pos_x
            225   # pos_y
        ],
        "dimensions": [
            375, # width
            100  # heigth
        ],
        "color": [
            220, # red
            220, # green
            150  # blue
        ],
        "line_thickness": 0  # 0 -> filled; 1 -> thin, 2 -> thicker
    }

    title_password_repeat = {
        "name": "title_password_repeat",
        "form": "rectangle",
        "text": {
            "content": "Wiederhole PW:",
            "color": [
                250, # red
                250, # green
                250  # blue
            ],
        },
        "position":[
            245,  # pos_x
            350   # pos_y
        ],
        "dimensions": [
            1, # width
            100  # heigth
        ],
        "color": [
            30, # red
            30, # green
            30  # blue
        ],
        "line_thickness": 0  # 0 -> filled; 1 -> thin, 2 -> thicker
    }

    input_password_repeat = {
        "name": "input_password_repeat",
        "form": "rectangle",
        "text": {
            "content": "Passwort",
            "color": [
                0, # red
                0, # green
                0  # blue
            ],
        },
        "position":[
            410,  # pos_x
            350   # pos_y
        ],
        "dimensions": [
            375, # width
            100  # heigth
        ],
        "color": [
            220, # red
            220, # green
            150  # blue
        ],
        "line_thickness": 0  # 0 -> filled; 1 -> thin, 2 -> thicker
    }

    title_age = {
        "name": "title_age",
        "form": "rectangle",
        "text": {
            "content": "Age:",
            "color": [
                250, # red
                250, # green
                250  # blue
            ],
        },
        "position":[
            150,  # pos_x
            475   # pos_y
        ],
        "dimensions": [
            1, # width
            100  # heigth
        ],
        "color": [
            30, # red
            30, # green
            30  # blue
        ],
        "line_thickness": 0  # 0 -> filled; 1 -> thin, 2 -> thicker
    }

    input_age = {
        "name": "input_age",
        "form": "rectangle",
        "text": {
            "content": "Age",
            "color": [
                0, # red
                0, # green
                0  # blue
            ],
        },
        "position":[
            410,  # pos_x
            475   # pos_y
        ],
        "dimensions": [
            375, # width
            100  # heigth
        ],
        "color": [
            220, # red
            220, # green
            150  # blue
        ],
        "line_thickness": 0  # 0 -> filled; 1 -> thin, 2 -> thicker
    }

    title_admin = {
        "name": "title_admin",
        "form": "rectangle",
        "text": {
            "content": "is Admin:",
            "color": [
                250, # red
                250, # green
                250  # blue
            ],
        },
        "position":[
            195,  # pos_x
            600   # pos_y
        ],
        "dimensions": [
            1, # width
            100  # heigth
        ],
        "color": [
            30, # red
            30, # green
            30  # blue
        ],
        "line_thickness": 0  # 0 -> filled; 1 -> thin, 2 -> thicker
    }

    input_admin = {
        "name": "input_admin",
        "form": "rectangle",
        "text": {
            "content": "Admin",
            "color": [
                0, # red
                0, # green
                0  # blue
            ],
        },
        "position":[
            410,  # pos_x
            600   # pos_y
        ],
        "dimensions": [
            375, # width
            100  # heigth
        ],
        "color": [
            220, # red
            220, # green
            150  # blue
        ],
        "line_thickness": 0  # 0 -> filled; 1 -> thin, 2 -> thicker
    }

    save_button = {
        "name": "save",
        "form": "rectangle",
        "text": {
            "content": "Speichern",
            "color": [
                0, # red
                0, # green
                0  # blue
            ],
        },
        "position":[
            195,  # pos_x
            725   # pos_y
        ],
        "dimensions": [
            250, # width
            100  # heigth
        ],
        "color": [
            180, # red
            220, # green
            180  # blue
        ],
        "line_thickness": 0  # 0 -> filled; 1 -> thin, 2 -> thicker
    }

    cancel_button = {
        "name": "cancel",
        "form": "rectangle",
        "text": {
            "content": "Abbrechen",
            "color": [
                0, # red
                0, # green
                0  # blue
            ],
        },
        "position":[
            455,  # pos_x
            725   # pos_y
        ],
        "dimensions": [
            250, # width
            100  # heigth
        ],
        "color": [
            220, # red
            180, # green
            180  # blue
        ],
        "line_thickness": 0  # 0 -> filled; 1 -> thin, 2 -> thicker
    }

    #image_paths = {
    #}
    input_fields = {
        "input_username" : input_username,
        "input_password" : input_password,
        "input_passwort_repeat" : input_password_repeat,
        "input_age" : input_age,
        "input_admin" : input_admin
    }

    # list which contains all element directories
    window_elements = [
        title_username,
        input_username,
        title_password,
        input_password,
        title_password_repeat,
        input_password_repeat,
        title_age,
        input_age,
        title_admin,
        input_admin,
        save_button,
        cancel_button
    ]

if __name__ == "__main__":
    print("This file contains the description elements for the game choice menu.")