# -*- coding:utf-8 -*-

import pygame
import Maps
from random import randint

from enum import Enum
from Settings import *
from NPCs import *
from PopUpBox import *
from Portal import *
from BgmPlayer import *


class Scene():
    def __init__(self, window):
        ##### Your Code Here ↓ #####
        self.window = window
        self.map = None
        self.sceneType = None

        self.width, self.height = (WindowSettings.width * WindowSettings.outdoorScale,
                                   WindowSettings.height * WindowSettings.outdoorScale)
        self.x_direction, self.y_direction = 0, 0
        self.cameraX, self.cameraY = 0, 0

        self.obstacles = pygame.sprite.Group()
        self.npcs = pygame.sprite.Group()
        self.portals = pygame.sprite.Group()
        self.monsters = pygame.sprite.Group()
        ##### Your Code Here ↑ #####

    def trigger_dialog(self, npc):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    def end_dialog(self):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    def trigger_battle(self, player):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    def end_battle(self):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    def trigger_shop(self, npc, player):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    def end_shop(self):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    def update_camera(self, player):
        ##### Your Code Here ↓ #####
        self.x_direction, self.y_direction = 0, 0
        if player.rect.x > WindowSettings.width / 4 * 3:
            self.cameraX += player.speed
            if self.cameraX < self.width - WindowSettings.width:
                player.fix_to_middle(player.speed, 0)
                self.x_direction = -1
            elif self.cameraX == self.width - WindowSettings.width:
                self.x_direction = -1
            else:
                self.cameraX = self.width - WindowSettings.width
        elif player.rect.x < WindowSettings.width / 4:
            self.cameraX -= player.speed
            if self.cameraX > 0:
                player.fix_to_middle(-player.speed, 0)
                self.x_direction = 1
            elif self.cameraX == 0:
                self.x_direction = 1
            else:
                self.cameraX = 0

        if player.rect.y > WindowSettings.height / 4 * 3:
            self.cameraY += player.speed
            if self.cameraY < self.height - WindowSettings.height:
                player.fix_to_middle(0, player.speed)
                self.y_direction = -1
            elif self.cameraY == self.height - WindowSettings.height:
                self.y_direction = -1
            else:
                self.cameraY = self.height - WindowSettings.height
        elif player.rect.y < WindowSettings.height / 4:
            self.cameraY -= player.speed
            if self.cameraY > 0:
                player.fix_to_middle(0, -player.speed)
                self.y_direction = 1
            elif self.cameraY == 0:
                self.y_direction = 1
            else:
                self.cameraY = 0
        ##### Your Code Here ↑ #####

    def render(self, player):
        ##### Your Code Here ↓ #####
        for i in range(SceneSettings.tileXnum):
            for j in range(SceneSettings.tileYnum):
                self.window.blit(self.map[i][j],
                                 (i * SceneSettings.tileWidth - self.cameraX,
                                  j * SceneSettings.tileHeight - self.cameraY))
        for obstacle in self.obstacles:
            obstacle.move(self.x_direction * player.speed,
                          self.y_direction * player.speed)
        for portal in self.portals:
            portal.move(self.x_direction * player.speed,
                        self.y_direction * player.speed)
        for monster in self.monsters:
            monster.move(self.x_direction * player.speed,
                        self.y_direction * player.speed)
        self.obstacles.draw(self.window)
        self.npcs.draw(self.window)
        self.portals.draw(self.window)
        self.monsters.draw(self.window)
        player.draw(self.window)
        ##### Your Code Here ↑ #####


class StartMenu():
    def __init__(self, window):
        ##### Your Code Here ↓ #####
        self.bg = pygame.image.load(GamePath.menu)
        self.bg = pygame.transform.scale(self.bg, (WindowSettings.width,
                                                   WindowSettings.height))
        self.window = window

        ##### Your Code Here ↑ #####

    def render(self, time):
        ##### Your Code Here ↓ #####
        self.window.blit(self.bg, (0, 0))
        ##### Your Code Here ↑ #####


class CityScene(Scene):
    def __init__(self, window):
        super().__init__(window=window)
        ##### Your Code Here ↓ #####
        self.map = Maps.gen_city_map()
        self.sceneType = SceneType.CITY
        self.window = window
        self.obstacles = Maps.gen_city_obstacle()
        self.portals.add(Portal(PortalSettings.coordX,
                                PortalSettings.coordY, self.sceneType))
        self.monsters.add(Monster(BattleSettings.monsterCoordX,
                                  BattleSettings.monsterCoordY))
        ##### Your Code Here ↑ #####

    def gen_CITY(self):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####


class WildScene(Scene):
    def __init__(self, window):
        super().__init__(window=window)
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    def gen_WILD(self):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    def gen_monsters(self, num=10):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####


class BossScene(Scene):
    def __init__(self, window):
        super().__init__(window=window)
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    # Overwrite Scene's function
    def trigger_battle(self, player):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    def gen_BOSS(self):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####
