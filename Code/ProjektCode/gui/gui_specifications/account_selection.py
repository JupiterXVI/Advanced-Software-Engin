"""
imports
"""
#from sys import path as sys_path

# This class discribes the struckture of the main menu
# which can be accessed form outside
class AccountSelection(): # muss ggf keine klasse ein
    """
    global variables
    """


    """
    global variables
    """
    account_0 = {
        "name": "account_0",
        "form": "rectangle",
        "text": {
            "content": "account_0",
            "font": 0,
            "color": [
                0, # red
                0, # green
                0  # blue
            ],
        },
        "position":[
            200,  # pos_x
            100   # pos_y
        ],
        "dimensions": [
            500, # width
            80  # heigth
        ],
        "color": [
            175, # red
            201, # green
            147  # blue
        ],
        "line_thickness": 0  # 0 -> filled; 1 -> thin, 2 -> thicker
    }
   
    account_1 = {
        "name": "account_1",
        "form": "rectangle",
        "text": {
            "content": "account_1",
            "font": 0,
            "color": [
                0, # red
                0, # green
                0  # blue
            ],
        },
        "position":[
            200,  # pos_x
            200   # pos_y
        ],
        "dimensions": [
            500, # width
            80  # heigth
        ],
        "color": [
            54, # red
            76, # green
            139  # blue
        ],
        "line_thickness": 0  # 0 -> filled; 1 -> thin, 2 -> thicker
    }

    
    account_2 = {
        "name": "account_2",
        "form": "rectangle",
        "text": {
            "content": "account_2",
            "font": 0,
            "color": [
                0, # red
                0, # green
                0  # blue
            ],
        },
        "position":[
            200,  # pos_x
            300   # pos_y
        ],
        "dimensions": [
            500, # width
            80  # heigth
        ],
        "color": [
            110, # red
            80, # green
            95  # blue
        ],
        "line_thickness": 0  # 0 -> filled; 1 -> thin, 2 -> thicker
    }

    account_3 = {
        "name": "account_3",
        "form": "rectangle",
        "text": {
            "content": "account_3",
            "font": 0,
            "color": [
                0, # red
                0, # green
                0  # blue
            ],
        },
        "position":[
            200,  # pos_x
            400   # pos_y
        ],
        "dimensions": [
            500, # width
            80  # heigth
        ],
        "color": [
            251, # red
            201, # green
            144  # blue
        ],
        "line_thickness": 0  # 0 -> filled; 1 -> thin, 2 -> thicker
    }

    account_4 = {
        "name": "account_4",
        "form": "rectangle",
        "text": {
            "content": "account_4",
            "font": 0,
            "color": [
                0, # red
                0, # green
                0  # blue
            ],
        },
        "position":[
            200,  # pos_x
            500   # pos_y
        ],
        "dimensions": [
            500, # width
            80  # heigth
        ],
        "color": [
            232, # red
            140, # green
            183  # blue
        ],
        "line_thickness": 0  # 0 -> filled; 1 -> thin, 2 -> thicker
    }

    account_5 = {
        "name": "account_5",
        "form": "rectangle",
        "text": {
            "content": "account_5",
            "font": 0,
            "color": [
                0, # red
                0, # green
                0  # blue
            ],
        },
        "position":[
            200,  # pos_x
            600   # pos_y
        ],
        "dimensions": [
            500, # width
            80  # heigth
        ],
        "color": [
            29, # red
            229, # green
            214  # blue
        ],
        "line_thickness": 0  # 0 -> filled; 1 -> thin, 2 -> thicker
    }

    account_6 = {
        "name": "account_6",
        "form": "rectangle",
        "text": {
            "content": "account_6",
            "font": 0,
            "color": [
                0, # red
                0, # green
                0  # blue
            ],
        },
        "position":[
            200,  # pos_x
            700   # pos_y
        ],
        "dimensions": [
            500, # width
            80  # heigth
        ],
        "color": [
            216, # red
            80, # green
            113  # blue
        ],
        "line_thickness": 0  # 0 -> filled; 1 -> thin, 2 -> thicker
    }
    account_list = [
        account_0,
        account_1,
        account_2,
        account_3,
        account_4,
        account_5,
        account_6
    ]

    # list which contains all element directories
    window_elements = [
    ]


    """
    functions
    """

    
if __name__ == "__main__":
    print("This file contains the description elements for the game choice menu.")
    