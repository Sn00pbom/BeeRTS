import pygame as pg
import settings
from inputs import keyboard
from units.unit import Unit
from inputs import mouse
from units.enemy import Enemy
from units.squad import Squad

class Game():
    def __init__(self):

        pg.init()
        self.size = [settings.GAME_WIDTH, settings.GAME_HEIGHT]
        self.clock = pg.time.Clock()

        self.DISPLAY = pg.display.set_mode(self.size)
        self.running = True


    def new(self):
        self.all_sprites = pg.sprite.Group()

        self.unit1 = Unit(10,4,10,10)
        self.unit2 = Unit(10, 4, 10, 110)
        self.unit3 = Unit(10, 4, 10, 210)

        self.enemy = Enemy(20,4,200,200)
        self.all_sprites.add(self.unit1)
        self.all_sprites.add(self.unit2)
        self.all_sprites.add(self.unit3)
        self.all_sprites.add(self.enemy)



    def run(self):
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
            self.clock.tick(settings.FPS)


    def update(self):
        self.all_sprites.update()
        # hits = pg.sprite.spritecollide(self.player, self.platforms, False)
        #
        # if hits:
        #     # self.player.rect.midbottom[1] = hits[0].rect.top + 1
        #     # self.player.rect.midbottom[0] = hits[0].rect.top
        #     self.player.pos.y = hits[0].rect.top + 1
        #     self.player.vel.y = 0
        #     # print hits[0].rect.top
        #     # print hits[0].rect.top + 1
        #
        # if self.player.rect.top <= settings.GAME_HEIGHT / 2:
        #     self.player.pos.y += abs(self.player.vel.y)
        #     for plat in self.platforms:
        #         plat.rect.y += abs(self.player.vel.y)
        #
        #         if plat.rect.top >= settings.GAME_HEIGHT:
        #             plat.kill()
        #
        #             self.GateCount -= 1
        #
        #             print self.GateCount


    # def generateGate(self, offset):
    #
    #     randomGateStart = random.randrange(20, settings.GAME_WIDTH - 20 - settings.GATE_WIDTH)
    #     pa = Plat(0, offset, randomGateStart, 25)
    #     self.platforms.add(pa)
    #     self.all_sprites.add(pa)
    #
    #     pb = Plat(randomGateStart + settings.GATE_WIDTH, offset,
    #               settings.GAME_WIDTH - settings.GATE_WIDTH - randomGateStart, 25)
    #     self.platforms.add(pb)
    #     self.all_sprites.add(pb)
    #
    #     self.GateCount += 2
    #     print self.GateCount



    def events(self):
        events = pg.event.get()
        for event in events:
            keyboard.readKeyboard(event)
            mouse.readMouse(event)
            # self.sticks.listenJoystick(self.player, event)
            if event.type == pg.QUIT:
                self.playing = False
                self.running = False
                # sys.exit()

    def draw(self):
        self.DISPLAY.fill(settings.WHITE)

        self.all_sprites.draw(self.DISPLAY)

        pg.display.flip()
