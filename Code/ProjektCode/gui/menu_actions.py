"""
imports
"""
from adapter import GuiBuilder
from communication import Sender

class MenuActions():
    """
    global variables
    """


    """
    functions
    """
    def get_window_elements_on_screen(elements, sender:Sender):
        sender.send(category='gui', name='send element_info', info={'function':GuiBuilder.set_window_elements.__name__, 'parameter':elements})
        sender.send(category='gui', name='set element style', info={'function':GuiBuilder.set_element_styles.__name__, 'parameter':''})

    def clear_window(sender:Sender):
        sender.send(category="gui",name="clear window", info={'function':GuiBuilder.clear_window.__name__, 'parameter': ''})

    def get_button_from_position(button_list, position):
        x, y = position
        for button in button_list:
            if (x > button['position'][0] and 
                x < (button['position'][0] + button['dimensions'][0]) and
                y > button['position'][1] and 
                y < (button['position'][1] + button['dimensions'][1])):
                return button['name']
        return "no button"
