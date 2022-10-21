import pygame
from pygame.locals import *
import time
from PIL import Image, ImageDraw, ImageEnhance, ImageFont
from urllib import request
import os
import fontTools
import sys

# comment: pathstring (pathstr) in out case was D:\Testna_mapa\jagoda.jpg. For your case
# you should change it

# inicializacija
pygame.init()

# parametri pygame display:
len_x = 750
len_y = 900
canvas = pygame.display.set_mode((len_x, len_y))

# končni parametri slik hrane:
# razlika med slikami z okvirji ter pravokotniki
delta = len_x // 16
# velikosti slik
size_x = len_x // 4
size_y = len_y // 4

# FPS for pygame
FPS = 600
FramePerSec = pygame.time.Clock()

# define custom user events:
# this one will increase the size of the image box if cursor on image
ON_BOX = pygame.USEREVENT + 1

#########################################################################
# CLASES


class Canvas:
    def __init__(self, canvas):
        """Defines the canvas display and app name"""
        self.canvas = canvas
        self.canvasfill = canvas.fill((255, 255, 255))
        pygame.display.set_caption(r"App_Name")
        print("Display init good")


class Background:
    def __init__(self):
        """Defines background on canvas from URL request"""
        # background request
        self.request_bg = request.urlopen(r"https://thumbs.dreamstime.com/b/fresh-fruits-"
                                         r"assorted-colorful-clean-eating-fruit-background-138466607.jpg")
        # open background request
        self.background_image = Image.open(self.request_bg)
        # resize background
        self.background_image = self.background_image.resize((len_x, len_y))
        # get mode, size and data of background image
        self.mode = self.background_image.mode
        #print(self.mode) <-- testing
        self.size = self.background_image.size
        #print(self.size) <-- testing
        self.data = self.background_image.tobytes()
        # transform background image to surface
        self.background_image_py = pygame.image.fromstring(self.data, self.size, self.mode)
        # paste background surface to canvas (display)
        canvas.blit(self.background_image_py, (0, 0))


class PicWithFrame(Background):
    def __init__(self, pos_x, pos_y, pathstr):
        """Defines and modifies the input picture to desired format and blits it on the screen"""
        # with super we take the __init__ function parameters from Background class to here
        super().__init__()
        # opens pathstring to image:
        self.image_new = Image.open(pathstr)
        # resizes the image
        self.image_new = self.image_new.resize((size_x, size_y))
        # returns to us filename with extension, which we delete with splitext:
        self.name_jpg = os.path.split(pathstr)[1]
        # first element has the name of picture
        self.name = os.path.splitext(self.name_jpg)[0]
        #print(self.name) <-- testing
        ############################################################################
        # initialization of blank_canvas-a such that the picture gets a black border of size delta
        # This will create a new picture to be used later for blitting on canvas (surface)
        # size of blank canvas is the size of the original picture + 2*delta//5 for both left, right, top and bottom
        # borders
        self.blank_canvas = Image.new("RGB", (size_x + 2 * delta // 5, size_y + 2 * delta // 5), color=(0, 0, 0))
        self.blank_canvas.paste(self.image_new, (delta // 5, delta // 5, size_x + delta // 5, size_y + delta // 5))
        #self.blank_canvas.show()  <-- testing
        # now we turn our newly created picture to a pygame surface, so we can blit it on the canvas (display)
        self.mode_new = self.blank_canvas.mode
        #print(self.mode) <-- testing
        self.size_new = self.blank_canvas.size
        #print(self.size) <-- testing
        self.data_new = self.blank_canvas.tobytes()
        # transform new image to surface
        self.new_image_py = pygame.image.fromstring(self.data_new, self.size_new, self.mode_new)
        # get the rectangle of the new image, to be used in picture_expansion function
        self.new_image_py_rect = self.new_image_py.get_rect(topleft=(pos_x, pos_y)) # <---!!!! here the rectangle gets
        # new position, otherwise it is stuck at (0,0)
        # blit the new image to the canvas (display)
        canvas.blit(self.new_image_py, (pos_x, pos_y))
        #print("Background init good")

    def picture_on_box(self):
        """If mouse is over the picture add ON_BOX to queue"""
        mouse = pygame.mouse.get_pos()
        if self.new_image_py_rect.collidepoint(mouse):
            pygame.event.post(pygame.event.Event(ON_BOX))

    def text_on_box(self):
        """Text for ON_BOX event. Text will be displayed at mouse location if the mouse
        is over the picture"""
        # this will bre written if ON_BOX event from picture_on_box is true
        # defining font for text
        font = pygame.font.SysFont('Corbel', 50)
        # what will the text say -- in the final release this should come from some string data for time saving
        text = font.render(f'placeholder', True, (0, 0, 0))
        # get rectangle for text
        text_rect = text.get_rect()
        # define mouse again for this function
        mouse_text = pygame.mouse.get_pos()
        # with this rectangle we can create a colored one at mouse position:
        pygame.draw.rect(canvas, (255, 255, 0), (mouse_text[0], mouse_text[1], text_rect.width, text_rect.height))
        # blitting text on screen
        canvas.blit(text, (mouse_text[0], mouse_text[1]))
        # with this rectangle we can create a colored one:


class Exit:
    """creating an X button in the top right corner for closing the app.
    The coordinates are (len_x - button_exit_size, 0, len_x, button_exit_size)
     (button_exit_size x button_exit_size rectangle)"""
    def __init__(self, button_exit_size):
        # draw rectangle button
        self.button = pygame.draw.rect(canvas, color=(128, 128, 128),
                                       rect=pygame.Rect(len_x - button_exit_size, 0, len_x, button_exit_size))
        # create text "Placeholder"
        self.font = pygame.font.SysFont("Corbel", button_exit_size)
        # render font if not mouse hovered over button
        self.text = self.font.render(f"X", True, (0, 0, 0))
        # render font if mouse hovered over button
        self.text_mouse_hover = self.font.render(f"X", True, (255, 255, 0))
        # blit text on canvas
        canvas.blit(self.text, (len_x - 3/4*button_exit_size, button_exit_size / 12))

    def button_exit(self, button_exit_size):
        """Checking first whether the mose is on the buttom
        and later if the mouse button is down"""
        # get mouse position
        mouse = pygame.mouse.get_pos()
        # if mouse on button change color
        if self.button.collidepoint(mouse):
            self.button = pygame.draw.rect(canvas, color=(255, 0, 0),
                                           rect=pygame.Rect(len_x - button_exit_size, 0, len_x,
                                                            button_exit_size))
            canvas.blit(self.text_mouse_hover, (len_x - 3/4*button_exit_size, button_exit_size / 12))
            for event in pygame.event.get():
                # criteria for mouse clicked
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print("Enjoy your meals!")
                    pygame.quit()
                    sys.exit()


class RunAnalytics:
    def __init__(self, button_anal_size_x, button_anal_size_y):
        # draw rectangle button
        self.anal_box = pygame.draw.rect(canvas, color=(128, 128, 128),
                                    rect=pygame.Rect(0, 0, button_anal_size_x, button_anal_size_y))
        # create text "Run Analytics"
        self.font = pygame.font.SysFont("Corbel", button_anal_size_y)
        # render font if not mouse hovered over button
        self.text = self.font.render(f"Run Analytics", True, (0, 0, 0))
        # render font if mouse hovered over button
        self.text_hover = self.font.render(f"Run Analytics", True, (255, 255, 0))
        # blit text on canvas
        canvas.blit(self.text, (0, 0))

    def run(self, button_anal_size_x, button_anal_size_y):
        """Checking first whether the mose is on the buttom
                and later if the mouse button is down"""
        # get mouse position
        mouse = pygame.mouse.get_pos()
        # if mouse on button change color
        if self.anal_box.collidepoint(mouse):
            self.anal_box = pygame.draw.rect(canvas, color=(255, 0, 0),
                                           rect=pygame.Rect(0, 0, button_anal_size_x, button_anal_size_y))
            canvas.blit(self.text_hover, (0, 0))
            for event in pygame.event.get():
                #criteria for mouse clicked
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print("Bye")



# names for classes to be used in while loop
display = Canvas
bg = Background
pic = PicWithFrame
button = Exit
anal = RunAnalytics

def app():
    """Main function. This app compiles all class functions and outputs
    the final result"""

    ##################################################################
    # Start of executable

    # displays canvas
    display(canvas)
    # displays background
    bg()
    # add pictures to canvas display
    pic(110, 110, r"D:\Testna_mapa\jagoda.jpg")
    while True:
        pic(110, 110, r"D:\Testna_mapa\jagoda.jpg").picture_on_box()
        # conditions of program
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == ON_BOX:
                pic(110, 110, r"D:\Testna_mapa\jagoda.jpg").text_on_box()
        pygame.event.clear()
        # Exit of program
        # Makes button for X
        button(50)
        # Makes button for run Analysis
        anal(270, 50)
        # checks whether X button is pressed
        button(50).button_exit(50)
        # checks whehter Run Analytics is pressed
        anal(270, 50).run(270, 50)
        # update display for all changes
        pygame.display.update()
        # Frame ticks
        FramePerSec.tick(FPS)
if __name___ == "__main__":
    app()
