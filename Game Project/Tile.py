# -*- coding:utf-8 -*-

import pygame

from Settings import *

class Tile(pygame.sprite.Sprite):
    def __init__(self, image, x=0, y=0, width=SceneSettings.tileWidth, height=SceneSettings.tileHeight):
        super().__init__()
        self.image = pygame.transform.scale(image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self, window, dx=0, dy=0):
        self.rect = self.rect.move(dx, dy)
        window.blit(self.image, self.rect)

class Tree(pygame.sprite.Sprite):  # 树木tile用于制造动画树木
    def __init__(self, images, x=0, y=0, width=SceneSettings.tileWidth, height=SceneSettings.tileHeight):
        super().__init__()
        self.images = [pygame.transform.scale(image, (width, height)) for image in images]
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self, window, dx=0, dy=0):
        self.update()
        self.rect = self.rect.move(dx, dy)
        window.blit(self.image, self.rect)

    def update(self):   # 树木tile动画
        self.index = (self.index + 1 / 3) % len(self.images)
        self.image = self.images[int(self.index)]