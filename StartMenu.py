
import pygame
import pygame_menu
import sys 
  
#basic structure of this code draws from
#https://pygame-menu.readthedocs.io/en/4.2.5/

# initializing the constructor 
pygame.init()
surface = pygame.display.set_mode((1920,1080))

def set_difficulty(value,difficulty):
    #do things here
    pass

def start_the_game():
    pass

mainMenu = pygame_menu.Menu('Welcome to Intro to Computing!', 1920,1080, theme = pygame_menu.themes.THEME_DARK)
settings = pygame_menu.Menu('Settings', 1920,1080, theme = pygame_menu.themes.THEME_DARK)
codeInput = pygame_menu.Menu('Secret Codes', 1920,1080, theme = pygame_menu.themes.THEME_DARK)

mainMenu.add.text_input('Name :', default='Al E. Gator')
#mainMenu.add.selector('Lesson :', [('Hard', 1), ('Easy', 2)], onchange=set_difficulty)
mainMenu.add.button('Play', start_the_game)
mainMenu.add.button('Secret Codes', codeInput)
mainMenu.add.button('Settings', settings)
mainMenu.add.button('Quit', pygame_menu.events.EXIT)

settings.add.text_input('test', default = 'success!')
codeInput.add.text_input('test', default = 'success!')

#This can be changed out for more flexible menu control
mainMenu.mainloop(surface)

