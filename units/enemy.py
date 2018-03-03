from unit import Unit
import controller
import pygame as pg
class Enemy(Unit):

    def __init__(self,hp,speed,x,y):
        super(Enemy,self).__init__(hp,speed,x,y)
        # self.pos = pg.math.Vector2(x,y)
