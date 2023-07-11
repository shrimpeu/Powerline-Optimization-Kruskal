import pygame


class MyNode(object):
    def __init__(self, xpos, ypos, radius, color):
        self.xpos = xpos
        self.ypos = ypos
        self.radius = radius
        self.color = color
        # pygame.draw.circle()
    pass


class MyEntry(object):
    def __init__(self, string, fontstyle, fontsize, bool, color_text, color_bg, x, y, width, height, entry_color_active,
                 entry_color_inactive, borderwidth, borderradius):
        self.string = string
        self.fontstyle = fontstyle
        self.fontsize = fontsize
        self.bool = bool
        self.color_Text = color_text
        self.color_bg = color_bg
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.entry_color_active = entry_color_active
        self.entry_color_inactive = entry_color_inactive
        self.borderwidth = borderwidth
        self.borderradius = borderradius
        self.active_state = False
        self.stringsize = 0

    def events(self, event):
        if self.x <= mousepos[0] <= self.x + self.width and self.y <= mousepos[1] <= self.y + self.height:
            # Change the button's color when clicking the button
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_IBEAM)
            if event.type == pygame.MOUSEBUTTONDOWN and self.active_state is False:
                self.active_state = True
                self.stringsize = 0
                self.string = ""
                print(self.active_state)
        else:
            if event.type == pygame.MOUSEBUTTONDOWN and self.active_state is True:
                self.active_state = False
                print(self.active_state)
            # Reset the button's color when the mouse is not hovering over it and becomes inactive
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        # pressing keyboard down
        if event.type == pygame.KEYDOWN and self.active_state is True:
            if self.stringsize == 1:  # limit of entry
                if event.key == pygame.K_BACKSPACE:
                    self.string = self.string[:-1]
                    self.stringsize -= 1
            elif self.stringsize < 0:
                self.stringsize = 0
            else:
                if event.unicode.isnumeric():  # numerical inputs only
                    self.string += event.unicode
                    self.stringsize += 1
            print(self.stringsize)

    def draw(self, screen):
        font = pygame.font.SysFont(self.fontstyle, self.fontsize)
        text = font.render(str(self.string), self.bool, self.color_Text, self.color_bg)
        textrect = text.get_rect()
        textrect.center = (self.x + self.width // 2, self.y + self.height // 2)
        if self.active_state is True:
            entry_color = self.entry_color_active
            self.color_Text = (0, 0, 0)
        else:
            entry_color = self.entry_color_inactive
            self.color_Text = (255, 255, 255)
        # background
        pygame.draw.rect(screen, entry_color, (self.x, self.y, self.width, self.height), 0, self.borderradius)
        # outline
        pygame.draw.rect(screen, (0, 0, 0), (self.x, self.y, self.width, self.height), self.borderwidth,
                         self.borderradius)
        screen.blit(text, textrect)


mousemovementpos = ()
mouseclickpos = ()
active_state = False
stringsize = 0

# classes needed to be called once, and it's properties to be drawn in a loop
sourceentry = MyEntry('source', 'monospace', 30, True, (255, 255, 255), None, 930, 20, 125, 35, (175, 175, 175),
                      (100, 100, 100), 2, 0)
endentry = MyEntry('end', 'monospace', 30, True, (255, 255, 255), None, 930, 75, 125, 35, (175, 175, 175),
                   (100, 100, 100), 2, 0)
weightentry = MyEntry('weight', 'monospace', 30, True, (255, 255, 255), None, 930, 75+55, 125, 35, (175, 175, 175),
                      (100, 100, 100), 2, 0)


pygame.init()  # root = Tk() root.mainloop
screen = pygame.display.set_mode((1250, 750))
running = True
while running:
    screen.fill((255, 255, 255))
    mousepos = pygame.mouse.get_pos()

    for event in pygame.event.get():  # event handling
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEMOTION:
            mousemovementpos = pygame.mouse.get_pos()
            # print("motion detected")
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseclickpos = pygame.mouse.get_pos()
            # print(mouseclickpos)
            # print("click detected")
        sourceentry.events(event)
        endentry.events(event)
        weightentry.events(event)

    sourceentry.draw(screen)
    endentry.draw(screen)
    weightentry.draw(screen)

    pygame.draw.line(screen, (50, 50, 50), (0, 0), mousemovementpos)
    pygame.display.update()
