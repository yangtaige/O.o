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
                self.index = (self.index + 1) % len(self.images)
                self.image = self.images[self.index]

            if keys[pygame.K_s] and self.rect.bottom < WindowSettings.height:
                dy += self.speed
                self.index = (self.index + 1) % len(self.images)
                self.image = self.images[self.index]

            if keys[pygame.K_a] and self.rect.left > 0:
                dx -= self.speed
                if not self.facing:
                    for i in range(len(self.images)):
                        self.images[i] = pygame.transform.flip(self.images[i], 1, 0)
                    self.facing = True
                self.index = (self.index + 1) % len(self.images)
                self.image = self.images[self.index]

            if keys[pygame.K_d] and self.rect.right < WindowSettings.width:
                dx += self.speed
                if self.facing:
                    for i in range(len(self.images)):
                        self.images[i] = pygame.transform.flip(self.images[i], 1, 0)
                    self.facing = False
                self.index = (self.index + 1) % len(self.images)
                self.image = self.images[self.index]

            self.rect = self.rect.move(dx, dy)


    def render(self, window):
        window.blit(self.image, self.rect)

    def fix_to_middle(self, dx, dy):
        self.rect.x -= dx
        self.rect.y -= dy