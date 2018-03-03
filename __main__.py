
import controller
import pygame as pg


print "db activeGame set"


while controller.activeGame.running:
    controller.activeGame.new()
    controller.activeGame.run()

pg.quit()