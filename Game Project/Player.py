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
        self.images = [[pygame.transform.scale(pygame.image.load(img), (PlayerSettings.playerWidth,
                                                                        PlayerSettings.playerHeight))
                        for img in image_list] for image_list in GamePath.player]
        self.direction = PlayerDirection.Right.value
        self.index = 0
        self.image = self.images[self.direction][self.index]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = PlayerSettings.playerSpeed
        self.talking = False
        self.buying = False

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

    def attr_update(self, addCoins=0, addHP=0, addAttack=0, addDefence=0):
        ##### Your Code Here ↓ #####
        if self.Money + addCoins < 0:
            return
        if self.HP + addHP < 0:
            return
        self.Money += addCoins
        self.HP += addHP
        self.Attack += addAttack
        self.Defence += addDefence
        ##### Your Code Here ↑ #####

    def reset_pos(self, x=WindowSettings.width // 2, y=WindowSettings.height // 2):
        ##### Your Code Here ↓ #####
        self.rect.x = x
        self.rect.y = y
        ##### Your Code Here ↑ #####

    def reset_scene(self):
        # 人物重置时将重叠的关务和障碍物移除
        if self.collidingWith['obstacle']:
            for obstacle in self.collidingObject['obstacle']:
                obstacle.kill()
            self.collidingWith['obstacle'] = False
            self.collidingObject['obstacle'] = []

        if self.collidingWith['monster']:
            self.collidingObject['monster'].action = Action.DIE
            self.collidingWith['monster'] = False
            self.collidingObject['monster'] = None

    def try_move(self):
        ##### Your Code Here ↓ #####
        '''尝试移动'''
        if not self.talking and not self.buying:
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
        if not self.talking and not self.buying:
            redx = 0  # 重置移动的距离
            redy = 0
            if self.collidingWith['obstacle']:
                redx = width
                redy = height

            if self.dx or self.dy:
                if self.dx > 0:
                    self.direction = PlayerDirection.Right.value
                if self.dx < 0:
                    self.direction = PlayerDirection.Left.value
                if self.dy > 0:
                    self.direction = PlayerDirection.Down.value
                if self.dy < 0:
                    self.direction = PlayerDirection.Up.value
                self.index = (self.index + 1 / 6) % len(self.images[self.direction])
                self.image = self.images[self.direction][int(self.index)]
            else:
                self.image = self.images[self.direction][int(self.index)]

            self.rect = self.rect.move(redx, redy)
            self.collidingWith['obstacle'] = False
            self.collidingObject['obstacle'] = []
        else:
            self.index = 0
            self.image = self.images[self.direction][self.index]
        ##### Your Code Here ↑ #####

    def draw(self, window, dx=0, dy=0):
        ##### Your Code Here ↓ #####
        self.rect = self.rect.move(dx, dy)
        window.blit(self.image, self.rect)
        ##### Your Code Here ↑ #####
