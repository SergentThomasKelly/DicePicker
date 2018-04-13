##Coded by SergentThomasKelly
#Project started the 18th of January 2018 at 7:15 PM
#First version finished the 19th of January 2018 at 9:27 AM

# ============================== INITIALISATION ============================== #
import pygame as pg
import sys
from os import path
from random import randint

# ============================== MAIN CLASS ================================== #
class DicePicker():
    # >>> Initialisation >>>
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((640, 480))
        self.clock = pg.time.Clock()
        pg.display.set_caption("DicePicker")
        self.loadEverything()
        self.run()

    # >>> Function for selecting the proper image for the good number >>>
    def facePicker(self):
        global facesFolder
        return path.join(facesFolder, str(self.pickedNumber)+str('c.gif'))

    # >>> Loading everything we need for executing code >>>
    def loadEverything(self):
        global facesFolder
        mainFolder = path.dirname(__file__)
        assetsFolder = path.join(mainFolder, 'assets')
        facesFolder = path.join(assetsFolder, 'faces')
        fontFolder = path.join(assetsFolder, 'fonts')
        self.guiFont = pg.font.Font(path.join(fontFolder, 'main.ttf'), 65)
        self.fond = pg.Surface(self.screen.get_size()).convert_alpha()
        self.fond.fill((0, 0, 0))
        self.colorGrey = (128,128,128)
        self.colorWhite = (255,255,255)
        self.colorText1 = self.colorText2 = self.colorText3 = self.colorText4 = self.colorText5 = self.colorText6 = self.colorText7 = self.colorText8 = self.colorText9 = self.colorGrey
        self.pickedNumber = 0

    # >>> Pick a number randomly >>>
    def randomPicker(self, number):
        self.pickedNumber = randint(1, int(number))

    # >>> Key Listener for keyboard and mouse input >>>
    def KeyListener(self):
        for event in pg.event.get():
            if self.button1.collidepoint(pg.mouse.get_pos()) == True:
                self.colorText1 = self.colorWhite
                if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                    self.randomPicker(1)
                    break
            else:
                self.colorText1= self.colorGrey
            if self.button2.collidepoint(pg.mouse.get_pos()) == True:
                self.colorText2 = self.colorWhite
                if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                    self.randomPicker(2)
                    break
            else:
                self.colorText2= self.colorGrey
            if self.button3.collidepoint(pg.mouse.get_pos()) == True:
                self.colorText3 = self.colorWhite
                if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                    self.randomPicker(3)
                    break
            else:
                self.colorText3= self.colorGrey
            if self.button4.collidepoint(pg.mouse.get_pos()) == True:
                self.colorText4 = self.colorWhite
                if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                    self.randomPicker(4)
                    break
            else:
                self.colorText4= self.colorGrey
            if self.button5.collidepoint(pg.mouse.get_pos()) == True:
                self.colorText5 = self.colorWhite
                if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                    self.randomPicker(5)
                    break
            else:
                self.colorText5= self.colorGrey
            if self.button6.collidepoint(pg.mouse.get_pos()) == True:
                self.colorText6 = self.colorWhite
                if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                    self.randomPicker(6)
                    break
            else:
                self.colorText6= self.colorGrey
            if self.button7.collidepoint(pg.mouse.get_pos()) == True:
                self.colorText7 = self.colorWhite
                if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                    self.randomPicker(7)
                    break
            else:
                self.colorText7= self.colorGrey
            if self.button8.collidepoint(pg.mouse.get_pos()) == True:
                self.colorText8= self.colorWhite
                if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                    self.randomPicker(8)
                    break
            else:
                self.colorText8= self.colorGrey
            if self.button9.collidepoint(pg.mouse.get_pos()) == True:
                self.colorText9 = self.colorWhite
                if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                    self.randomPicker(9)
                    break
            else:
                self.colorText9= self.colorGrey
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_1:
                    self.randomPicker(1)
                if event.key == pg.K_2:
                    self.randomPicker(2)
                if event.key == pg.K_3:
                    self.randomPicker(3)
                if event.key == pg.K_4:
                    self.randomPicker(4)
                if event.key == pg.K_5:
                    self.randomPicker(5)
                if event.key == pg.K_6:
                    self.randomPicker(6)
                if event.key == pg.K_7:
                    self.randomPicker(7)
                if event.key == pg.K_8:
                    self.randomPicker(8)
                if event.key == pg.K_9:
                    self.randomPicker(9)
                if event.key == pg.K_ESCAPE:
                    self.quit()
            if event.type == pg.QUIT:
                self.quit()

    # >>> The program is forever active unless we quit it >>>
    def run(self):
        while True:
            self.renderScreen()
            self.KeyListener()

    # >>> Render and actualize the screen >>>
    def renderScreen(self):
        self.diceFaceSurface = pg.image.load(self.facePicker())
        self.screen.blit(self.fond,(0,0))
        self.titleBlit = self.screen.blit(self.guiFont.render("Faces :", 4, (255,255,255)), (15,10))
        self.button1 = self.screen.blit(self.guiFont.render("(1)", 4, self.colorText1), (35,50))
        self.button2 = self.screen.blit(self.guiFont.render("(2)", 4, self.colorText2), (30,90))
        self.button3 = self.screen.blit(self.guiFont.render("(3)", 4, self.colorText3), (30,130))
        self.button4 = self.screen.blit(self.guiFont.render("(4)", 4, self.colorText4), (30,170))
        self.button5 = self.screen.blit(self.guiFont.render("(5)", 4, self.colorText5), (30,210))
        self.button6 = self.screen.blit(self.guiFont.render("(6)", 4, self.colorText6), (30,250))
        self.button7 = self.screen.blit(self.guiFont.render("(7)", 4, self.colorText7), (30,290))
        self.button8 = self.screen.blit(self.guiFont.render("(8)", 4, self.colorText8), (30,330))
        self.button9 = self.screen.blit(self.guiFont.render("(9)", 4, self.colorText9), (30,370))
        self.scoreTitleBlit = self.screen.blit(self.guiFont.render("Score :", 4, self.colorWhite), (10,415))
        self.scoreNumber = self.screen.blit(self.guiFont.render(str(self.pickedNumber), 4, self.colorWhite), (170, 415))
        self.diceFace = self.screen.blit(self.diceFaceSurface, (350, 100))
        pg.display.update()

    # >>> Quit pygame and python >>>
    def quit(self):
        pg.quit()
        sys.exit()


# ============================== START ======================================= #
DicePicker()

#END
