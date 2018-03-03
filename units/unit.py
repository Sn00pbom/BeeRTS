import pygame as pg
import math
import controller
vec = pg.math.Vector2

class Unit(pg.sprite.Sprite):

    def __init__(self,hp,speed,x,y):
        self.hp = hp
        self.pos = vec(x,y)
        self.goTo = vec(0, 0) ##initialize
        self.vel = vec(0, 0)
        self.speed = speed

        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load("./assets/units/unit_worker.png")
        self.rect = self.image.get_rect()

        self.rect.center = self.pos

        # self.width = width
        # self.height = height

    def setVelTowards(self,pos):
        pos = vec(pos[0],pos[1])
        if pos != self.pos:
            pass


        self.goTo = pos

        print self.goTo

        deltaX = self.goTo.x-self.pos.x
        deltaY = self.goTo.y-self.pos.y
        vb = vec(deltaX,deltaY)

        theta = math.atan(deltaY/deltaX)

        # vx = self.speed * math.sqrt(1-(math.sin(theta)**2))
        # vy = self.speed * math.sqrt(1 - (math.cos(theta) ** 2))
        vx = (self.speed*deltaX)/vb.length()
        vy = (self.speed*deltaY)/vb.length()
        self.vel = vec(vx,vy)
        print "db theta " + str(theta)


    def atDest(self):

        x1 = self.goTo.x
        y1 = self.goTo.y
        x2 = self.pos.x
        y2 = self.pos.y
        boundDelta = 2
        xbound = [x1-boundDelta,x1+boundDelta]
        ybound = [y1-boundDelta,y1+boundDelta]
        if (x2> xbound[0] and x2 < xbound[1]) and (y2> ybound[0] and y2 < ybound[1]):
            return True
        else:
            return False

    def checkMove(self):
        newpos = self.pos + self.vel
        for sprite in controller.activeGame.all_sprites:
            if sprite.rect.collidepoint(newpos) and sprite is not self:
                return False
        return True


    def update(self):
        # print self.pos
        # print self.goTo
        if self.atDest() == True:
            self.vel = vec(0,0)
        if self.checkMove():
            self.pos = self.pos + self.vel

        self.rect.center = self.pos