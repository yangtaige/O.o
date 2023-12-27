# -*- coding:utf-8 -*-

from Settings import *
import pygame
import os


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.images = [pygame.transform.scale(pygame.image.load(img), 
                            (PlayerSettings.playerWidth, PlayerSettings.playerHeight)) for img in GamePath.player]
        self.index = 0
        self.image = self.images[self.index]
        self.speed = PlayerSettings.playerSpeed
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.facing = False
        self.talking = False

    def update(self, keys, scene):
        if self.talking:
            self.index = 0
            self.image = self.images[self.index]
        else:
            dx = 0
            dy = 0
            if keys[pygame.K_w] and self.rect.top > 0:
                dy -= self.speed
            if keys[pygame.K_s] and self.rect.bottom < WindowSettings.height:
                dy += self.speed
            if keys[pygame.K_a] and self.rect.left > 0:
                dx -= self.speed
                if not self.facing:
                    self.image = pygame.transform.flip(self.image, 1, 0)
                    self.facing = True
            if keys[pygame.K_d] and self.rect.right < WindowSettings.width:
                dx += self.speed
                if self.facing:
                    self.image = pygame.transform.flip(self.image, 1, 0)
                    self.facing = False

            self.rect = self.rect.move(dx, dy)

    def fix_to_middle(self, dx, dy):
        self.rect.x -= dx
        self.rect.y -= dy
