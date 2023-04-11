"""
imports
"""
from adapter import GuiBuilder
import pygame
from communication import Sender, Reseiver


# class used to build visualize menus and games
# - gui/menu builder using the pygame library
# - takes information about the window and its contence and creates it using those specifications
class PygameBuilder(GuiBuilder):
    """
    global variables
    """
    def __init__(self):
        pygame.init()
        # communication between objects
        self.sender = Sender()
        self.reseiver = Reseiver()
        self.run_forever = True
        self.funktion_with_parameters = [
            'set_window_info','set_window_elements',
            'set_game_elements','load_image_on_screen','set_font']
        # information for the gui-window
        self.window_info = "not set"
        # list of elements which make up the contence
        self.window_elements = "list of elements in menu"
        # font for text written on the menu
        self.fonts = [pygame.font.Font('freesansbold.ttf', 35), pygame.font.Font('freesansbold.ttf', 60), pygame.font.Font('freesansbold.ttf', 20)]
        self.window = "pygame_window_object"


    """
    functions
    """
    # this funktion runs untill stoped and reakts to messages send with category gui
    # - it checks for interaktion with gui and sends a message
    def run(self):
        while self.run_forever:
            while self.reseiver.event_reseved:
                message = self.reseiver.get_message()
                if message['category'] == 'gui':
                    self.react_to_request(request=message['info'])
                if message['category'] == 'exit':
                    print("closing gui thread")
                    return
            window_event = self.check_events()
            if window_event != "no action":
                self.sender.send(category= "input", name="window_event", info=window_event)
            if self.window != "pygame_window_object":
                self.update_window()
        print("closing gui thread")
        

    # this funktion takes the information from message and starts the requested funktion with the given parameters
    # - takes dictionary with funktion and parameter
    def react_to_request(self, request):
        if request["function"] in self.funktion_with_parameters:
            eval(f"self.{request['function']}")(request['parameter'])
        else:
            eval(f"self.{request['function']}")()


    # this funktion sets the window deskribing elements with the given parameter
    # - takes list of description elements
    def set_window_info(self, window_info):
        self.window_info = window_info


    # this funktion sets the content deskribing elements with the given parameter
    # - takes list of description elements
    def set_window_elements(self, window_elements):
        self.window_elements = window_elements


    # this funktion creates a window with set infromation and saves the objekt
    def create_window(self):
        window = pygame.display.set_mode(size=(self.window_info['width'], self.window_info['height']))
        pygame.display.set_caption(self.window_info['titel'])
        self.window = window
        self.clear_window()

    # this funktion fills the window with set color thereby removing the window content
    def clear_window(self):
        try:
            self.window.fill(self.window_info['color'])
        except:
            "window is still string"


    # this funktion closes th pygame game instanze and therefor the gui window
    def terminate_window(self):
        pygame.quit()


    # this funktion draws the set content elements on the cleard window
    def set_element_styles(self):
        self.clear_window()
        for element in self.window_elements:
            try:
                if element['form'] == "rectangle":
                    pygame.draw.rect(self.window, element['color'],[element['position'] ,element['dimensions']], element['line_thickness'])
                    text = self.fonts[element['text']['font']].render(element['text']['content'], True, element['text']['color'])
                    text_box = text.get_rect()
                    text_box.center = (element['position'][0] + (element['dimensions'][0]/2) , element['position'][1] + (element['dimensions'][1]/2))
                    self.window.blit(text, text_box)
                if element['form'] == "circle":
                    pygame.draw.circle(self.window, element['color'],
                                    (element['position'][0]+element['radius'], element['position'][1]+element['radius']), 
                                    element['radius'], element['line_thickness'])
            except:
                "window ist still string"


    # this funktion draws a given image on the window
    # - takes description element wirth additional path to graphic
    def load_image_on_screen(self, game_element):
            image = pygame.image.load(game_element['graphic'] )
            intercaton_surface = pygame.Rect(game_element['position'], game_element['dimensions'])
            image = pygame.image.load(game_element['graphic'] )
            self.window.blit(image, intercaton_surface.center)


    # this funktion refresches the gui, so newly drawn objekts can be seen 
    def update_window(self):
        pygame.display.update()


    # this funktion converts pygame interaction event into unicode
    # - takes pygqme events
    def check_key_tap(self, event):
        if event.key == pygame.K_BACKSPACE:
            return "backspace"
        else:
            return str(event.unicode)


    # this funktion checks if there was any interaction with the gui window and returns the event information
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.sender.send(category="exit", name="exit_event", info="window_closed")
                self.run_forever = False
            if event.type == pygame.KEYDOWN:
                return self.check_key_tap(event)
            if event.type == pygame.MOUSEBUTTONDOWN:
                return pygame.mouse.get_pos()
        return "no action"
        

if __name__ == "__main__":
    print("The PygameBuilder is a class used to visualize menus and games")

    