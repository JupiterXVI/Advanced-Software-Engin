"""
imports
"""
from .interfaces import AllowToBuldMenu
import pygame

# class used to build menu objekts
# - gui/menu builder using the pygame library
# - takes information about the window and its contence and creates it using those specifications
class MenuBuilder(AllowToBuldMenu):
    """
    global variables
    """
    def __init__(self):
        pygame.init()
        # information for the gui-window
        self.window_width = "width"
        self.window_height = "height"
        self.window_titel = "titel"
        self.window_color = "color"
        # list of elements which make up the contence
        self.window_elements = "list of elements in menu"
        self.game_elements = "list of elements in game"
        # font for text written on the menu
        self.font = pygame.font.Font('freesansbold.ttf', 35)
        self.window = "pygame_window_object"

    """
    functions
    """
    def set_window_info(self, window_info):
        self.window_width = window_info["width"]
        self.window_height = window_info["height"]
        self.window_titel = window_info["titel"]
        self.window_color = window_info["color"]

    def set_window_elements(self, window_elements):
        self.window_elements = window_elements

    def set_game_elements(self, game_elements):
        self.game_elements = game_elements

    # this funktion creates a window with a given sice and setz its title
    def create_window(self):
        window = pygame.display.set_mode((self.window_width, self.window_height))
        pygame.display.set_caption(self.window_titel)
        self.window = window

    def clear_window(self):
        self.window.fill(self.window_color)

    # this funktion closes the the game and therefor all windows
    def terminate_window(self):
        pygame.quit()

    # this funktion uses the element list given at initilization, checks the form of the element,
    # draws them on the given window and returns a list of interactable surfaces aproximate to the drawn elemnets
    def create_window_interaction_elements(self):
        elements_added_to_window = {"item_name": [], "item": []}
        for element in reversed(self.window_elements):
            intercaton_surface = pygame.Rect([0, 0, 0, 0])
            if element["form"] == "rectangle":
                intercaton_surface = pygame.Rect( element["position"], element["dimensions"])
            if element["form"] == "circle":
                rect_size = 2*element["radius"]
                pos_x = element["position"][0] - element["radius"]
                pos_y =element["position"][1] - element["radius"]
                intercaton_surface = pygame.Rect([pos_x, pos_y, rect_size, rect_size])
            elements_added_to_window["item_name"].append(element["name"])
            elements_added_to_window["item"].append(intercaton_surface)
        return elements_added_to_window

    # this funktion takes the given elements and their styles specifications and changes them acordingly
    def set_element_styles(self):
        self.window.fill(self.window_color)
        for element in self.window_elements:
            if element["form"] == "rectangle":
                pygame.draw.rect(self.window, element["color"],[element["position"] ,element["dimensions"]], element["line_thickness"])
                text = self.font.render(element["text"]["content"], True, element["text"]["color"])
                text_box = text.get_rect()
                text_box.center = (element["position"][0] + (element["dimensions"][0] / 2) , element["position"][1] + (element["dimensions"][1] / 2))
                self.window.blit(text, text_box)
            if element["form"] == "circle":
                pygame.draw.circle(self.window, element["color"], element["position"], element["radius"], element["line_thickness"])

    def create_game_elements(self):
        elements_added_to_game = {"item_name": [], "item": []}
        for element in reversed(self.game_elements):
            for pice in range(element["who_offten_needed"]):
                image = pygame.image.load(element["graphic"] )
                intercaton_surface = pygame.Rect(element["position"], element["dimensions"])
                #points = element["value"]
                #speed = element["speed"]
                #cooldown = element["laser_cooldown"]
                #form = element["shape"]
                #style = element["style"]
                #properties = []
                elements_added_to_game["item_name"].append(f"{element['name']}_{pice}")
                elements_added_to_game["item"].append([intercaton_surface, image])
        return elements_added_to_game
        
    def set_game_element_styles(self, added_elemets):
        self.window.fill(self.window_color)
        index = 0
        for element in added_elemets["item"]:
            self.window.blit(element[1], element[0].center)
            index += 1

    # this funktion refresches the gui, so newly drawn objekts can be seen 
    def update_window(self):
        pygame.display.update()

    # this funktion checks if the right mous button was cklicked
    def check_click(self):
        if pygame.mouse.get_pressed()[0] == 1:
            return True
        return False

    # this funktion checks if the menubar was used or one of the interactable surfaces was ckicked
    # and returns the name of the interaction
    def check_events(self, interaction_surfaces):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
        for index, item in enumerate(interaction_surfaces["item"]):
            if item.collidepoint(pygame.mouse.get_pos()):
                if self.check_click():
                    return interaction_surfaces["item_name"][index]
        return "no action"



if __name__ == "__main__":
    print("This file contains the class to build and run menus")

    