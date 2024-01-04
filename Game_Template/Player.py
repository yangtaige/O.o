# -*- coding:utf-8 -*-

import pygame

from Settings import *
from Attributes import *

class Player(pygame.sprite.Sprite, Collidable):
    def __init__(self, x, y):
        # Must initialize everything one by one here
        pygame.sprite.Sprite.__init__(self)
        Collidable.__init__(self)

        ##### Your Code Here ↓ #####
        self.images = [pygame.transform.scale(pygame.image.load(img), 
                            (PlayerSettings.playerWidth, PlayerSettings.playerHeight)) for img in GamePath.player]
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = PlayerSettings.playerSpeed
        self.talking = False
        self.direction = True
        self.facing = False

        self.HP = PlayerSettings.playerHP
        self.Attack = PlayerSettings.playerAttack
        self.Defence = PlayerSettings.playerDefence
        self.Money = PlayerSettings.playerMoney
        ##### Your Code Here ↑ #####

    def attr_update(self, addCoins = 0, addHP = 0, addAttack = 0, addDefence = 0):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    def reset_pos(self, x=WindowSettings.width // 2, y=WindowSettings.height // 2):
        ##### Your Code Here ↓ #####
        self.rect.x = x
        self.rect.y = y
        ##### Your Code Here ↑ #####

    def try_move(self, keys):
        ##### Your Code Here ↓ #####
        '''接受按键参数，判断移动距离'''
        if self.talking:
            self.index = 0
            self.image = self.images[self.index]
            return 0, 0
        else:
            dx = 0
            dy = 0
            if keys[pygame.K_w] and self.rect.top > 0:
                dy -= self.speed

            if keys[pygame.K_s] and self.rect.bottom < WindowSettings.height:
                dy += self.speed

            if keys[pygame.K_a] and self.rect.left > 0:
                dx -= self.speed

            if keys[pygame.K_d] and self.rect.right < WindowSettings.width:
                dx += self.speed
            return dx, dy

        ##### Your Code Here ↑ #####

    def update(self, width, height):
        ##### Your Code Here ↓ #####
        '''移动角色，更变角色图片'''
        if width < 0:
            if not self.facing:
                for i in range(len(self.images)):
                    self.images[i] = pygame.transform.flip(self.images[i], 1, 0)
                self.facing = True

        if width > 0:
            if self.facing:
                for i in range(len(self.images)):
                    self.images[i] = pygame.transform.flip(self.images[i], 1, 0)
                self.facing = False
        if width or height:
            self.index = (self.index + 1) % len(self.images)
            self.image = self.images[self.index]

        self.rect = self.rect.move(width, height)
        ##### Your Code Here ↑ #####


    def draw(self, window, dx=0, dy=0):
        ##### Your Code Here ↓ #####
        window.blit(self.image, self.rect)
        ##### Your Code Here ↑ #####


    def fix_to_middle(self, x, y):
        self.rect.x -= x
        self.rect.y -= y
