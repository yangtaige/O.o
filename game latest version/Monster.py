# -*- coding:utf-8 -*-

from Settings import *
import pygame

class Monster(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.images = [pygame.transform.scale(pygame.image.load(img),
                            (MonsterSettings.monsterWidth, MonsterSettings.monsterHeight)) for img in GamePath.monster]
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = MonsterSettings.monsterSpeed
        self.direction = 1

        self.HP = MonsterSettings.monsterHP
        self.attack = MonsterSettings.monsterAttack
        self.defence = MonsterSettings.monsterDefence
        self.clock = 0

    def move(self,x,y):
        self.rect.x += x
        self.rect.y += y

    def update(self):
        self.index = (self.index + 0.125) % len(self.images)
        self.image = self.images[int(self.index)]

        self.rect = self.rect.move(self.speed * self.direction, 0)

        if self.clock == 100:
            self.direction *= -1
            self.clock = 0
        else:
            self.clock += 1
        if  self.direction == -1:
            self.image = pygame.transform.flip(self.image, True, False)

