"""
imports
"""
#from sys import path as sys_path

# This class discribes the struckture of the main menu
# which can be accessed form outside
class ManageAccount(): # muss ggf keine klasse ein
    """
    global variables
    """
    window = {
        "width": 900,
        "height": 900,
        "titel": "Spielebibliothek",
        "color": (30, 30, 30)
    }

    account_0_name = {
        "name": "account_0_name",
        "form": "rectangle",
        "text": {
            "content": "account_1",
            "color": [
                0, # red
                0, # green
                0  # blue
            ],
        },
        "position":[
            150,  # pos_x
            100   # pos_y
        ],
        "dimensions": [
            480, # width
            100  # heigth
        ],
        "color": [
            180, # red
            180, # green
            220  # blue
        ],
        "line_thickness": 0  # 0 -> filled; 1 -> thin, 2 -> thicker
    }

    account_0_delete = {
        "name": "account_0_delete",
        "form": "rectangle",
        "text": {
            "content": "X",
            "color": [
                0, # red
                0, # green
                0  # blue
            ],
        },
        "position":[
            650,  # pos_x
            100   # pos_y
        ],
        "dimensions": [
            100, # width
            100  # heigth
        ],
        "color": [
            180, # red
            180, # green
            220  # blue
        ],
        "line_thickness": 0  # 0 -> filled; 1 -> thin, 2 -> thicker
    }

    account_1_name = {
        "name": "account_1_name",
        "form": "rectangle",
        "text": {
            "content": "account_2",
            "color": [
                0, # red
                0, # green
                0  # blue
            ],
        },
        "position":[
            150,  # pos_x
            225   # pos_y
        ],
        "dimensions": [
            480, # width
            100  # heigth
        ],
        "color": [
            220, # red
            180, # green
            150  # blue
        ],
        "line_thickness": 0  # 0 -> filled; 1 -> thin, 2 -> thicker
    }

    account_1_delete = {
        "name": "account_1_delete",
        "form": "rectangle",
        "text": {
            "content": "X",
            "color": [
                0, # red
                0, # green
                0  # blue
            ],
        },
        "position":[
            650,  # pos_x
            225   # pos_y
        ],
        "dimensions": [
            100, # width
            100  # heigth
        ],
        "color": [
            220, # red
            180, # green
            150  # blue
        ],
        "line_thickness": 0  # 0 -> filled; 1 -> thin, 2 -> thicker
    }

    account_2_name = {
        "name": "account_2_name",
        "form": "rectangle",
        "text": {
            "content": "account_3",
            "color": [
                0, # red
                0, # green
                0  # blue
            ],
        },
        "position":[
            150,  # pos_x
            350   # pos_y
        ],
        "dimensions": [
            480, # width
            100  # heigth
        ],
        "color": [
            220, # red
            180, # green
            220  # blue
        ],
        "line_thickness": 0  # 0 -> filled; 1 -> thin, 2 -> thicker
    }

    account_2_delete = {
        "name": "account_2_delete",
        "form": "rectangle",
        "text": {
            "content": "X",
            "color": [
                0, # red
                0, # green
                0  # blue
            ],
        },
        "position":[
            650,  # pos_x
            350   # pos_y
        ],
        "dimensions": [
            100, # width
            100  # heigth
        ],
        "color": [
            220, # red
            180, # green
            220  # blue
        ],
        "line_thickness": 0  # 0 -> filled; 1 -> thin, 2 -> thicker
    }

    account_3_name = {
        "name": "account_3_name",
        "form": "rectangle",
        "text": {
            "content": "account_4",
            "color": [
                0, # red
                0, # green
                0  # blue
            ],
        },
        "position":[
            150,  # pos_x
            475   # pos_y
        ],
        "dimensions": [
            480, # width
            100  # heigth
        ],
        "color": [
            220, # red
            220, # green
            180  # blue
        ],
        "line_thickness": 0  # 0 -> filled; 1 -> thin, 2 -> thicker
    }

    account_3_delete = {
        "name": "account_3_delete",
        "form": "rectangle",
        "text": {
            "content": "X",
            "color": [
                0, # red
                0, # green
                0  # blue
            ],
        },
        "position":[
            650,  # pos_x
            475   # pos_y
        ],
        "dimensions": [
            100, # width
            100  # heigth
        ],
        "color": [
            220, # red
            220, # green
            180  # blue
        ],
        "line_thickness": 0  # 0 -> filled; 1 -> thin, 2 -> thicker
    }

    account_4_name = {
        "name": "account_4_name",
        "form": "rectangle",
        "text": {
            "content": "account_5",
            "color": [
                0, # red
                0, # green
                0  # blue
            ],
        },
        "position":[
            150,  # pos_x
            600   # pos_y
        ],
        "dimensions": [
            480, # width
            100  # heigth
        ],
        "color": [
            180, # red
            220, # green
            180  # blue
        ],
        "line_thickness": 0  # 0 -> filled; 1 -> thin, 2 -> thicker
    }

    account_4_delete = {
        "name": "account_4_delete",
        "form": "rectangle",
        "text": {
            "content": "X",
            "color": [
                0, # red
                0, # green
                0  # blue
            ],
        },
        "position":[
            650,  # pos_x
            600   # pos_y
        ],
        "dimensions": [
            100, # width
            100  # heigth
        ],
        "color": [
            180, # red
            220, # green
            180  # blue
        ],
        "line_thickness": 0  # 0 -> filled; 1 -> thin, 2 -> thicker
    }

    back_button = {
        "name": "main_menu",
        "form": "rectangle",
        "text": {
            "content": "Zurück",
            "color": [
                0, # red
                0, # green
                0  # blue
            ],
        },
        "position":[
            200,  # pos_x
            725   # pos_y
        ],
        "dimensions": [
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

    # list which contains all element directories
    account_button_list = [
        account_0_name,
        account_1_name,
        account_2_name,
        account_3_name,
        account_4_name
    ]


    window_elements = [
        account_0_name,
        account_0_delete,
        account_1_name,
        account_1_delete,
        account_2_name,
        account_2_delete,
        account_3_name,
        account_3_delete,
        account_4_name,
        account_4_delete,
        back_button
    ]

if __name__ == "__main__":
    print("This file contains the description elements for the account management menu.")