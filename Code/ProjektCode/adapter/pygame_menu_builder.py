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
    def __init__(self, window_info, window_elements):
        # information for the gui-window
        self.window_width = window_info["width"]
        self.window_height = window_info["height"]
        self.window_titel = window_info["titel"]
        self.window_color = window_info["color"]
        # list of elements which make up the contence
        self.window_elements = window_elements

    """
    functions
    """
    # ths funktion creates a window with a given sice and setz its title
    def create_window(self):
        window = pygame.display.set_mode((self.window_width, self.window_height))
        pygame.display.set_caption(self.window_titel)
        return window

    # this funktion closes the the game and therefor all windows
    def terminate_window(self):
        pygame.quit()

    # this funktion uses the element list given at initilization, checks the form of the element,
    # draws them on the given window and returns a list of interactable surfaces aproximate to the drawn elemnets
    def create_window_interaction_elements(self):
        elements_added_to_window = {"item_name": [], "item": []}
        for element in self.window_elements:
            intercaton_surface = pygame.Rect([0, 0, 0, 0])
            if element["form"] == "rectangle":
                intercaton_surface = pygame.Rect(element["dimensions"])
            if element["form"] == "circle":
                rect_size = 2*element["radius"]
                pos_x = element["position"][0] - element["radius"]
                pos_y =element["position"][1] - element["radius"]
                intercaton_surface = pygame.Rect([pos_x, pos_y, rect_size, rect_size])
            elements_added_to_window["item_name"].append(element["name"])
            elements_added_to_window["item"].append(intercaton_surface)
        return elements_added_to_window
#element["position"], 2*element["radius"], 2*element["radius"]
    # this funktion takes the given elements and their styles specifications and changes them acordingly
    def set_element_styles(self, window):
        window.fill(self.window_color)
        for element in self.window_elements:
            if element["form"] == "rectangle":
                pygame.draw.rect(window, element["color"], element["dimensions"], element["line_thickness"])
            if element["form"] == "circle":
                pygame.draw.circle(window, element["color"], element["position"], element["radius"], element["line_thickness"])

        

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
    def check_events(self, intercaton_surfaces):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
        for index, item in enumerate(intercaton_surfaces["item"]):
            if item.collidepoint(pygame.mouse.get_pos()):
                if self.check_click():
                    return intercaton_surfaces["item_name"][index]



if __name__ == "__main__":
    print("This file contains the class to build and run menus")

    
"""
import pygame

SCREEN_HEIGHT = 500
SCREEN_WIDTH = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Spielebibliothek')

#load button images
start_img = pygame.image.load('image/start_btn.png').convert_alpha()
exit_img = pygame.image.load('image/exit_btn.png').convert_alpha()

#button class
class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect= self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
		
    def draw(self):
        action = False
        #get mouse position
        pos = pygame.mouse.get_pos()
        print(pos)
		
        #check mouseover and clicked conditions
        if self.rect.collidepoint(pos) == 0:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        if self.rect.collidepoint(pos):
            print('HOVER')
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:		#0 Linksklick, 1 Mausrad, 2 Rechtsklick
                print('CLICKED')
                self.clicked = True
                action = True
				
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

	
        #draw button on screen
        screen.blit(self.image, (self.rect.x, self.rect.y))

        return action
		
#create button instances
start_button = Button(100, 100, start_img, 0.5)
exit_button = Button(100, 200, exit_img, 0.5)

run = True
while run:

    screen.fill((202, 228, 241))
	
    if start_button.draw() ==True:
        print('START')
    if exit_button.draw() == True:
        print('EXIT')
        run = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
		
pygame.quit()
"""