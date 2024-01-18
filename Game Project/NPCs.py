# -*- coding:utf-8 -*-

import pygame

from Settings import *
from Attributes import *
from random import randint, random

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
        self.talking = False
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
        ##### Your Code Here ↑ #####
    
    def update(self):
        ##### Your Code Here ↓ #####
        '''传入self.tick(self, fps)方法'''
        if not self.talking:
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
    
    def update(self):
        ##### Your Code Here ↓ #####
        if not self.talking and self.talkCD > 0:
            self.talkCD -= 1
        ##### Your Code Here ↑ #####
    

class Monster(pygame.sprite.Sprite):
    def __init__(self, x, y, HP = 10, Attack = 3, Defence = 1, Money = 15):
        super().__init__()
        
        ##### Your Code Here ↓ #####
        self.images = [[pygame.transform.scale(pygame.image.load(img),
                            (NPCSettings.npcWidth,
                             NPCSettings.npcHeight)) for img in img_list] for img_list in GamePath.monster]
        self.type = randint(0, len(self.images) - 1)
        self.index = 3
        self.image = self.images[self.type][self.index]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = NPCSettings.npcSpeed
        self.direction = 1
        self.action = Action.SITTING
        self.delay = 20

        self.HP = HP
        self.attack = Attack
        self.defence = Defence
        self.money = Money

        ##### Your Code Here ↑ #####


    def update(self):
        if self.action == Action.STANDING:
            if self.index > 0:
                self.index -= 1 / 3
        if self.action == Action.DIE:
            if self.index < len(self.images[self.type]) - 1:
                self.index += 1 / 3
            elif self.delay > 0:
                self.delay -= 1
            else:
                self.kill()

        self.image = self.images[self.type][int(self.index)]

    def draw(self, window, dx=0, dy=0):
        ##### Your Code Here ↓ #####
        self.rect = self.rect.move(dx, dy)
        window.blit(self.image, self.rect)
        ##### Your Code Here ↑ #####


class Boss(pygame.sprite.Sprite):
    def __init__(self, x = (WindowSettings.width/2) + 200, y = WindowSettings.height/2):
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
