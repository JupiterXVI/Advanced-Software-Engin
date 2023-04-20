"""
imports
"""
ACCOUNT_BUTTON_WIDTH = 480
ACCOUNT_BUTTON_HEIGHT = 100
ACCOUNT_X_OFFSET = 150
ACCOUNT_Y_OFFSET = 100
DELETE_BUTTON_WIDTH = 100
DELETE_BUTTON_HEIGHT = 100
DELETE_X_OFFSET = 650
DELETE_Y_OFFSET = 100
BUTTON_OFFSET = 25
BACK_BUTTON_WIDTH = 500
BACK_BUTTON_HEIGHT = 100
BACK_X_OFFSET = 200
BACK_Y_OFFSET = 725


# This class discribes the struckture of the main menu
# which can be accessed form outside
class ManageAccount(): # muss ggf keine klasse ein
    """
    global variables
    """
    account_0_name = {
        "name": "account_0_name",
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
            ACCOUNT_X_OFFSET,  # pos_x
            ACCOUNT_Y_OFFSET   # pos_y
        ],
        "dimensions": [
            ACCOUNT_BUTTON_WIDTH, # width
            ACCOUNT_BUTTON_HEIGHT  # heigth
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
            "font": 0,
            "color": [
                0, # red
                0, # green
                0  # blue
            ],
        },
        "position":[
            DELETE_X_OFFSET,  # pos_x
            DELETE_Y_OFFSET   # pos_y
        ],
        "dimensions": [
            DELETE_BUTTON_WIDTH, # width
            DELETE_BUTTON_HEIGHT  # heigth
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
            "font": 0,
            "color": [
                0, # red
                0, # green
                0  # blue
            ],
        },
        "position":[
            ACCOUNT_X_OFFSET,  # pos_x
            ACCOUNT_Y_OFFSET + (1*(ACCOUNT_BUTTON_HEIGHT+BUTTON_OFFSET)) # pos_y
        ],
        "dimensions": [
            ACCOUNT_BUTTON_WIDTH, # width
            ACCOUNT_BUTTON_HEIGHT  # heigth
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
            "font": 0,
            "color": [
                0, # red
                0, # green
                0  # blue
            ],
        },
        "position":[
            DELETE_X_OFFSET,  # pos_x
            DELETE_Y_OFFSET + (1*(DELETE_BUTTON_HEIGHT+BUTTON_OFFSET)) # pos_y
        ],
        "dimensions": [
            DELETE_BUTTON_WIDTH, # width
            DELETE_BUTTON_HEIGHT  # heigth
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
            "font": 0,
            "color": [
                0, # red
                0, # green
                0  # blue
            ],
        },
        "position":[
            ACCOUNT_X_OFFSET,  # pos_x
            ACCOUNT_Y_OFFSET + (2*(ACCOUNT_BUTTON_HEIGHT+BUTTON_OFFSET)) # pos_y
        ],
        "dimensions": [
            ACCOUNT_BUTTON_WIDTH, # width
            ACCOUNT_BUTTON_HEIGHT  # heigth
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
            "font": 0,
            "color": [
                0, # red
                0, # green
                0  # blue
            ],
        },
        "position":[
            DELETE_X_OFFSET,  # pos_x
            DELETE_Y_OFFSET + (2*(DELETE_BUTTON_HEIGHT+BUTTON_OFFSET)) # pos_y
        ],
        "dimensions": [
            DELETE_BUTTON_WIDTH, # width
            DELETE_BUTTON_HEIGHT  # heigth
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
            "font": 0,
            "color": [
                0, # red
                0, # green
                0  # blue
            ],
        },
        "position":[
            ACCOUNT_X_OFFSET,  # pos_x
            ACCOUNT_Y_OFFSET + (3*(ACCOUNT_BUTTON_HEIGHT+BUTTON_OFFSET)) # pos_y
        ],
        "dimensions": [
            ACCOUNT_BUTTON_WIDTH, # width
            ACCOUNT_BUTTON_HEIGHT  # heigth
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
            "font": 0,
            "color": [
                0, # red
                0, # green
                0  # blue
            ],
        },
        "position":[
            DELETE_X_OFFSET,  # pos_x
            DELETE_Y_OFFSET + (3*(DELETE_BUTTON_HEIGHT+BUTTON_OFFSET)) # pos_y
        ],
        "dimensions": [
            DELETE_BUTTON_WIDTH, # width
            DELETE_BUTTON_HEIGHT  # heigth
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
            "font": 0,
            "color": [
                0, # red
                0, # green
                0  # blue
            ],
        },
        "position":[
            ACCOUNT_X_OFFSET,  # pos_x
            ACCOUNT_Y_OFFSET + (4*(ACCOUNT_BUTTON_HEIGHT+BUTTON_OFFSET)) # pos_y
        ],
        "dimensions": [
            ACCOUNT_BUTTON_WIDTH, # width
            ACCOUNT_BUTTON_HEIGHT  # heigth
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
            "font": 0,
            "color": [
                0, # red
                0, # green
                0  # blue
            ],
        },
        "position":[
            DELETE_X_OFFSET,  # pos_x
            DELETE_Y_OFFSET + (4*(DELETE_BUTTON_HEIGHT+BUTTON_OFFSET)) # pos_y
        ],
        "dimensions": [
            DELETE_BUTTON_WIDTH, # width
            DELETE_BUTTON_HEIGHT  # heigth
        ],
        "color": [
            180, # red
            220, # green
            180  # blue
        ],
        "line_thickness": 0  # 0 -> filled; 1 -> thin, 2 -> thicker
    }

    
    back_button = {
        "name": "start_menu",
        "form": "rectangle",
        "text": {
            "content": "Zurück",
            "font": 0,
            "color": [
                0, # red
                0, # green
                0  # blue
            ],
        },
        "position":[
            BACK_X_OFFSET,  # pos_x
            BACK_Y_OFFSET   # pos_y
        ],
        "dimensions": [
            BACK_BUTTON_WIDTH, # width
            BACK_BUTTON_HEIGHT  # heigth
        ],
        "color": [
            220, # red
            180, # green
            180  # blue
        ],
        "line_thickness": 0  # 0 -> filled; 1 -> thin, 2 -> thicker
    }

    
    account_button_list = [
        account_0_name,
        account_1_name,
        account_2_name,
        account_3_name,
        account_4_name
    ]

    
    # list which contains all element directories
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


    """
    functions
    """
    

if __name__ == "__main__":
    print("This file contains the description elements for the account management menu.")
    