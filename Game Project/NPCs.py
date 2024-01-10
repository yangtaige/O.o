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
        self.image = pygame.image.load(GamePath.npc)
        self.image = pygame.transform.scale(self.image, (NPCSettings.npcWidth, NPCSettings.npcHeight))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.name = name

        self.talking = False
        self.talkCD = 0
        ##### Your Code Here ↑ #####

    def update(self):
        raise NotImplementedError

    def reset_talkCD(self):
        ##### Your Code Here ↓ #####
        '''将talkCD重置'''
        self.talkCD = NPCSettings.talkCD
        ##### Your Code Here ↑ #####

    def draw(self, window, dx=0, dy=0):
        ##### Your Code Here ↓ #####
        self.rect = self.rect.move(dx, dy)
        window.blit(self.image, self.rect)
        ##### Your Code Here ↑ #####


class DialogNPC(NPC):
    def __init__(self, x, y, name, dialog):
        ##### Your Code Here ↓ #####
        super().__init__(x=x, y=y, name=name)
        self.speed = NPCSettings.npcSpeed
        self.facing_East = 1
        self.dialog = dialog
        self.walking_time = 3 * WindowSettings.fps  #每移动三秒换向
        self.clock = 0  # 当前移动时间
        ##### Your Code Here ↑ #####
    
    def update(self):
        ##### Your Code Here ↓ #####
        '''传入self.tick(self, fps)方法'''
        if not self.talking:
            self.rect = self.rect.move(self.speed * self.facing_East, 0)
            if self.clock == self.walking_time:  # 换向
                self.facing_East *= -1
                self.image = pygame.transform.flip(self.image, True, False)
                self.clock = 0
            else:
                self.clock += 1
            if self.talkCD > 0:
                self.talkCD -= 1
        ##### Your Code Here ↑ #####

class ShopNPC(NPC):
    def __init__(self, x, y, name, items, dialog):
        super().__init__(x, y, name)

        ##### Your Code Here ↓ #####
        super().__init__(x=x, y=y, name=name)
        self.speed = NPCSettings.npcSpeed
        self.items = items
        self.dialog = dialog
        ##### Your Code Here ↑ #####
    
    def update(self, ticks):
        ##### Your Code Here ↓ #####
        if not self.talking and self.talkCD > 0:
            self.talkCD -= 1
        ticks
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
        self.money = Money

        ##### Your Code Here ↑ #####

    def draw(self, window, dx=0, dy=0):
        ##### Your Code Here ↓ #####
        self.rect = self.rect.move(dx, dy)
        window.blit(self.image, self.rect)
        ##### Your Code Here ↑ #####


class Boss(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        
        ##### Your Code Here ↓ #####
        self.image = pygame.transform.scale(pygame.image.load(GamePath.boss),
                            (BossSettings.width,
                             BossSettings.height))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.HP = 500
        self.attack = 150
        self.defence = 50
        self.money = 888
        ##### Your Code Here ↑ #####

    def draw(self, window, dx=0, dy=0):
        ##### Your Code Here ↓ #####
        self.rect = self.rect.move(dx, dy)
        window.blit(self.image, self.rect)
        ##### Your Code Here ↑ #####
