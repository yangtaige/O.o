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
        self.movingWest = False
        self.movingEast = False
        self.movingNorth = False
        self.movingSouth = False
        self.dx = 0
        self.dy = 0
        self.facingEast = True

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

    def reset_scene(self):
        if self.collidingWith['obstacle']:
            for obstacle in self.collidingObject['obstacle']:
                obstacle.kill()
            self.collidingWith['obstacle'] = False
            self.collidingObject['obstacle'] = []

        if self.collidingWith['monster']:
            self.collidingObject['monster'].kill()
            self.collidingWith['monster'] = False
            self.collidingObject['monster'] = None

    def try_move(self):
        ##### Your Code Here ↓ #####
        '''尝试移动'''
        
        self.dx = 0
        self.dy = 0
        if self.movingNorth and self.rect.top > 0:
            self.dy -= self.speed

        if self.movingSouth and self.rect.bottom < WindowSettings.height:
            self.dy += self.speed

        if self.movingWest and self.rect.left > 0:
            self.dx -= self.speed

        if self.movingEast and self.rect.right < WindowSettings.width:
            self.dx += self.speed

        self.rect = self.rect.move(self.dx, self.dy)

        ##### Your Code Here ↑ #####

    def update(self, width, height):
        ##### Your Code Here ↓ #####
        '''调整坐标，播放角色动画'''
        redx = 0    # 重置移动的距离
        redy = 0
        if self.collidingWith['obstacle']:
            redx = width
            redy = height

        if self.movingEast:
            if not self.facingEast:
                for i in range(len(self.images)):
                    self.images[i] = pygame.transform.flip(self.images[i], 1, 0)
                self.facingEast = True

        if self.movingWest:
            if self.facingEast:
                for i in range(len(self.images)):
                    self.images[i] = pygame.transform.flip(self.images[i], 1, 0)
                self.facingEast = False
    
        if self.dx or self.dy:
            self.index = (self.index + 1) % len(self.images)
            self.image = self.images[self.index]
        else:
            self.index = 0
            self.image = self.images[self.index]

        self.rect = self.rect.move(redx, redy)
        self.collidingWith['obstacle'] = False
        self.collidingObject['obstacle'] = []
        ##### Your Code Here ↑ #####


    def draw(self, window, dx=0, dy=0):
        ##### Your Code Here ↓ #####
        self.rect = self.rect.move(dx, dy)
        window.blit(self.image, self.rect)
        ##### Your Code Here ↑ #####



