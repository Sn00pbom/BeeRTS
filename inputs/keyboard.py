#guy.jump
import controller
import pygame as pg

def readKeyboard(event):


    if event.type == pg.KEYDOWN:
        if event.key == pg.K_d:
            print "db d clear selected"
            controller.clearSelected()
    # print "db hello"

    # events = pg.event.get()
    # for event in events:
    #     print "db for loop"
    # if event.type == pg.KEYDOWN:
    #
    #     if event.key == pg.K_LEFT:
    #         player.jump(player.LEFT)
    #     elif event.key == pg.K_RIGHT:
    #         # print "db 1"
    #         player.jump(player.RIGHT)
    #     elif event.key == pg.K_UP:
    #         player.jump(player.CENTER)

