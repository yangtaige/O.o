# -*- coding:utf-8 -*-

import pygame

from Settings import *
from Attributes import *

class NPC(pygame.sprite.Sprite, Collidable):
    def __init__(self, x, y, name):
        # Initialize father classes
        pygame.sprite.Sprite.__init__(self)
        Collidable.__init__(self)

        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    def update(self):
        raise NotImplementedError

    def reset_talkCD(self):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    def draw(self, window, dx=0, dy=0):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####


class DialogNPC(NPC):
    def __init__(self, x, y, name, dialog):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####
    
    def update(self, ticks):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

class ShopNPC(NPC):
    def __init__(self, x, y, name, items, dialog):
        super().__init__(x, y, name)

        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####
    
    def update(self, ticks):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####
    

class Monster(pygame.sprite.Sprite):
    def __init__(self, x, y, HP = 10, Attack = 3, Defence = 1, Money = 15):
        super().__init__()
        
        ##### Your Code Here ↓ #####
        self.image = pygame.transform.scale(pygame.image.load(GamePath.monster),
                            (NPCSettings.npcWidth,
                             NPCSettings.npcHeight))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = NPCSettings.npcSpeed
        self.direction = 1

        self.HP = HP
        self.attack = Attack
        self.defence = Defence
        self.clock = 0
        self.money = Money

        ##### Your Code Here ↑ #####

    def draw(self, window, dx=0, dy=0):
        ##### Your Code Here ↓ #####
        window.blit(self.image, self.rect)
        ##### Your Code Here ↑ #####

    def move(self, x, y):
        self.rect.x += x
        self.rect.y += y

class Boss(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    def draw(self, window, dx=0, dy=0):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####
