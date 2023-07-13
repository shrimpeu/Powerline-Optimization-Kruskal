# if pygame module does not exist currently
# go to command prompt and type
# pip install pygame
# to convert to .exe file, go to command prompt and type (method 1)
# pip install pyinstaller
# go to the directory where this .py file is located
# type cmd at the address bar, press enter, then type
# pyinstaller --onefile -w main.py
# after conversion the .exe file will be located at the folder named 'dist' and get it out of that folder
# additional folder named 'build' will be there as well and it can be deleted along with 'dist'
# try running the exe file
# using auto py to exe (method 2)
# pip install auto-py-to-exe
# CMD, type "auto-py-to-exe", hit enter
# then just browse the .py file you want converted and icon, if there is any
import pygame


class MyEntry(object):
    def __init__(self, string, fontstyle, fontsize, boolean, color_text, color_bg, x, y, width, height, active_color,
                 inactive_color, borderwidth, borderradius):
        self.string = string
        self.fontstyle = fontstyle
        self.fontsize = fontsize
        self.bool = boolean
        self.color_text = color_text
        self.color_bg = color_bg
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.active_color = active_color
        self.inactive_color = inactive_color
        self.borderwidth = borderwidth
        self.borderradius = borderradius
        self.active_state = False
        self.stringsize = 0

    def events(self, event):
        if self.x <= mousepos[0] <= self.x + self.width and self.y <= mousepos[1] <= self.y + self.height:
            if event.type == pygame.MOUSEBUTTONDOWN and self.active_state is False:
                self.active_state = True  # active object
                self.stringsize = 0
                self.string = ""
                # print(self.active_state)
        else:
            # Reset the entry's color when the mouse is not hovering over it
            if event.type == pygame.MOUSEBUTTONDOWN and self.active_state is True:
                self.active_state = False  # inactive object
                # print(self.active_state)

        # pressing keyboard down
        if event.type == pygame.KEYDOWN and self.active_state is True:
            if event.key == pygame.K_BACKSPACE and self.stringsize > 0:
                self.string = self.string[:-1]
                self.stringsize -= 1
            if event.unicode.isnumeric() and self.stringsize < 5:  # numerical inputs only
                self.string += event.unicode
                self.stringsize += 1
            # print(self.string)

    def draw(self, screen):
        font = pygame.font.SysFont(self.fontstyle, self.fontsize)
        text = font.render(str(self.string), self.bool, self.color_text, self.color_bg)
        textrect = text.get_rect()
        textrect.center = (self.x + self.width // 2, self.y + self.height // 2)
        if self.active_state is True:
            entry_color = self.active_color
            self.color_text = (0, 0, 0)
        else:
            entry_color = self.inactive_color
            self.color_text = (255, 255, 255)
        # background
        pygame.draw.rect(screen, entry_color, (self.x, self.y, self.width, self.height), 0, self.borderradius)
        # outline
        pygame.draw.rect(screen, (0, 0, 0), (self.x, self.y, self.width, self.height), self.borderwidth,
                         self.borderradius)
        screen.blit(text, textrect)


class MyButton(object):
    def __init__(self, string, fontstyle, fontsize, boolean, color_text, color_bg, x, y, width, height, active_color,
                 inactive_color, command):
        self.string = string
        self.fontstyle = fontstyle
        self.fontsize = fontsize
        self.bool = boolean
        self.color_text = color_text
        self.color_bg = color_bg
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.active_color = active_color
        self.inactive_color = inactive_color
        self.active_state = False
        self.command = command

    def events(self, event):
        if self.x <= mousepos[0] <= self.x + self.width and self.y <= mousepos[1] <= self.y + self.height:
            if event.type == pygame.MOUSEBUTTONDOWN and self.active_state is False:
                # Change the button's color when clicking the button
                self.active_state = True
                # print("buttondown")
        if event.type == pygame.MOUSEBUTTONUP and self.active_state is True:
            # returning the button's color when releasing the mouseclick
            self.command()
            sourceentry.string = "source"
            endentry.string = "end"
            weightentry.string = "weight"
            self.active_state = False

    def draw(self, screen):
        font = pygame.font.SysFont(self.fontstyle, self.fontsize)
        text = font.render(self.string, self.bool, self.color_text, self.color_bg)
        textrect = text.get_rect()
        textrect.center = (self.x + self.width // 2, self.y + self.height // 2)
        if self.active_state is True:
            button_color = self.active_color
        else:
            button_color = self.inactive_color
        pygame.draw.rect(screen, button_color, (self.x, self.y, self.width, self.height))
        screen.blit(text, textrect)


class MyNode(object):
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def draw(self, win):
        pygame.draw.circle(win, (0, 0, 0), (self.x, self.y), self.radius)  # black outline of the ball
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius - 1)  # bg of ball


def eventhandler(event):  # event handling, this is needed for objects to detect certain events happening in the UI
    sourceentry.events(event)
    endentry.events(event)
    weightentry.events(event)
    addedgebutton.events(event)


def addedge():
    if sourceentry.string.isnumeric() and endentry.string.isnumeric() and weightentry.string.isnumeric():
        print(sourceentry.string)
        print(endentry.string)
        print(weightentry.string)
        graph.append([sourceentry.string, endentry.string, weightentry.string])
        print(graph)
    # print("Button press")


mousemovementpos = ()
mouseclickpos = ()

# classes needed to be called once and its properties to be drawn in a loop
# this is important so that we can change the value of attributes of a class
# because if these objects are inside the loop it will be harder to change the value of the attributes
sourceentry = MyEntry('source', 'monospace', 30, True, (255, 255, 255), None, 1100, 20, 125, 35, (175, 175, 175),
                      (100, 100, 100), 2, 0)
endentry = MyEntry('end', 'monospace', 30, True, (255, 255, 255), None, 1100, 75, 125, 35, (175, 175, 175),
                   (100, 100, 100), 2, 0)
weightentry = MyEntry('weight', 'monospace', 30, True, (255, 255, 255), None, 1100, 130, 125, 35, (175, 175, 175),
                      (100, 100, 100), 2, 0)
addedgebutton = MyButton('Add Edge', 'monospace', 20, True, (255, 255, 255), None, 1100, 185, 125, 35, (175, 175, 175),
                         (100, 100, 100), addedge)

graph = []

pygame.init()
screen = pygame.display.set_mode((1250, 750))
running = True
while running:
    screen.fill((255, 255, 255))
    mousepos = pygame.mouse.get_pos()

    # properties being drawn in a loop
    sourceentry.draw(screen)
    endentry.draw(screen)
    weightentry.draw(screen)
    addedgebutton.draw(screen)

    for event in pygame.event.get():
        eventhandler(event)
        if event.type == pygame.QUIT:
            exit()
        '''
        if event.type == pygame.MOUSEMOTION:
            mousemovementpos = pygame.mouse.get_pos()
            # print("motion detected")
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseclickpos = pygame.mouse.get_pos()
            # print(mouseclickpos)
            # print("click detected")
        '''

    # pygame.draw.line(screen, (50, 50, 50), (0, 0), mousemovementpos)
    pygame.display.update()
