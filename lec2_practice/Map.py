# -*- coding:utf-8 -*-
from Settings import *
import pygame
from random import random, randint

class Block(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        super().__init__()
        self.image = pygame.transform.scale(image, 
        (SceneSettings.tileWidth, SceneSettings.tileHeight))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.fixposX = x
        self.fixposY = y

    def fix_with_BG(self, cameraX, cameraY):
        pass

def gen_map():
    images = [pygame.image.load(path)
              for path in GamePath.groundTiles]
    images = [pygame.transform.scale(image,
(SceneSettings.tileWidth, SceneSettings.tileHeight))for image in images]

    mapObj = []
    for i in range(SceneSettings.tileXnum):
        tmp = []
        for j in range(SceneSettings.tileYnum):
            tmp.append(images[randint(0, len(images) - 1)])
        mapObj.append(tmp)

    return mapObj

def build_obstacle():
    pass

