"""
imports
"""
from os import path as os_path
from sys import path as sys_path
sys_path.append(os_path.join(sys_path[0], '..'))
from adapter import AllowToBuldMenu
import pygame

class MenuBuilder(AllowToBuldMenu):
    """
    global variables
    """
    def __init__(self, window_info, window_elements):
        self.window_width = window_info["width"]
        self.window_height = window_info["height"]
        self.window_titel = window_info["titel"]
        self.window_elements = window_elements

    """
    functions
    """
    def create_window(self):
        window = pygame.display.set_mode((self.window_width, self.window_height))
        pygame.display.set_caption(self.window_titel)
        return window
        
        
    def create_window_elements(self):
        for element in self.window_elements:
            if element["form"] == "rectangle":
                print("rect")

    def set_styles(self):
        pass


class Button():
    """
    global variables
    """
    def __init__(self, pos_x, pos_y, width, height):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height
        self.aktive = True

    """
    functions
    """
    def click(self):
        if self.aktive:
            pass
        else:
            pass        


    
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