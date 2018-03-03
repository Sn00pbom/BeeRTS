import pygame as pg
import controller
from effects.indicateclick import ClickIndicator
from units import Unit
import math

LEFT = 1
MIDDLE = 2
RIGHT = 3
SCROLL_UP = 4
SCROLL_DOWN = 5

def selection(mousepos):
    rect = pg.Rect()
    rect.x = mousepos[0]
    rect.y = mousepos[1]
    deltax = rect.x - controller.mleftdownpos.x
    deltay = rect.y - controller.mleftdownpos.y
    rect.w = math.fabs(deltax)
    rect.h = math.fabs(deltay)


def drawSelection():
    # if pg.mouse.get_pressed()[LEFT] == 1:
    #     print "db"
    # if len(controller.squad.)==0: return
    for unit in controller.squad.units:
        blue = (0,0,255)
        pg.draw.rect(controller.activeGame.DISPLAY,blue,unit.rect,3)
    mousepos = pg.mouse.get_pos()



def readMouse(event):
    game = controller.activeGame
    mousepos = pg.mouse.get_pos()

    # drawSelection()

    if event.type == pg.MOUSEBUTTONDOWN:
        um = getUnderMouse(mousepos) ##underneath mouse position sprite array
        if event.button == RIGHT:
            print "db right click"
            # print "db " + pg.mouse.get_pos()

            # moveToMouse = controller.activeGame.unit.setVelTowards(mousepos)
            moveToMouse = controller.squad.setVelTowards(mousepos)
            if len(um) == 0:
                moveToMouse
            else:
                for sprite in um:
                    if type(sprite) == Unit:
                        print "db myunit"
                    else:
                        moveToMouse

            doClickIndication(mousepos)
        elif event.button == LEFT:
            controller.mleftdownpos = mousepos
            #selecting something
            if len(um) != 0:
                for sprite in um:
                    if type(sprite) == Unit:
                        #sprite is a unit, and inherits methods
                        controller.squad.addUnit(sprite)
    elif event.type == pg.MOUSEBUTTONUP:

        if event.button == LEFT:
            # selection(mousepos)
            pass


        
def getUnderMouse(mousepos):
    sprites = []
    for sprite in controller.activeGame.all_sprites:
        if sprite.rect.collidepoint(mousepos):
            sprites.append(sprite)

    return sprites



def doClickIndication(mousepos):
    indicator = ClickIndicator()
    indicator.rect.center = mousepos
    controller.activeGame.all_sprites.add(indicator)
