import pygame
import controller
def load_image(name):
    image = pygame.image.load(name)
    return image

class ClickIndicator(pygame.sprite.Sprite):
    def __init__(self):
        super(ClickIndicator, self).__init__()
        self.images = []
        self.images.append(load_image('./assets/effects/clickindicator/ci1.png'))
        self.images.append(load_image('./assets/effects/clickindicator/ci2.png'))
        self.images.append(load_image('./assets/effects/clickindicator/ci3.png'))
        # assuming both images are 64x64 pixels

        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        # self.rect = pygame.Rect(5, 5, 64, 64)

    def update(self):
        '''This method iterates through the elements inside self.images and
        displays the next one each tick. For a slower animation, you may want to
        consider using a timer of some sort so it updates slower.'''
        interval = 3
        self.index += 1

        if self.index >= len(self.images)*interval:
            self.index = 0
            self.remove(controller.activeGame.all_sprites)
        if self.index % interval == 0:
            self.image = self.images[self.index/interval]