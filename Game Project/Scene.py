# -*- coding:utf-8 -*-

import pygame
from random import randint, random

from enum import Enum
from Settings import *
from NPCs import *
from PopUpBox import *
from Portal import *
from BgmPlayer import *
from Tile import *


class Scene():
    def __init__(self, window):
        ##### Your Code Here ↓ #####
        self.window = window
        self.map = pygame.sprite.Group()
        self.sceneType = None

        self.width, self.height = (WindowSettings.width * WindowSettings.outdoorScale,
                                   WindowSettings.height * WindowSettings.outdoorScale)
        self.dx, self.dy = 0, 0
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
        self.dx, self.dy = 0, 0
        if player.rect.x > WindowSettings.width / 4 * 3:
            self.cameraX += player.speed
            if self.cameraX < self.width - WindowSettings.width:
                self.dx = - player.speed
            else:
                self.cameraX = self.width - WindowSettings.width
                self.dx = 0
        elif player.rect.x < WindowSettings.width / 4:
            self.cameraX -= player.speed
            if self.cameraX > 0:
                self.dx = player.speed
            else:
                self.cameraX = 0
                self.dx = 0
        if player.rect.y > WindowSettings.height / 4 * 3:
            self.cameraY += player.speed
            if self.cameraY < self.height - WindowSettings.height:
                self.dy = - player.speed
            else:
                self.cameraY = self.height - WindowSettings.height
                self.dy = 0
        elif player.rect.y < WindowSettings.height / 4:
            self.cameraY -= player.speed
            if self.cameraY > 0:
                self.dy = player.speed
            else:
                self.cameraY = 0
                self.dy = 0
        ##### Your Code Here ↑ #####

    def render(self, player):
        ##### Your Code Here ↓ #####
        for pixel in self.map:
            pixel.draw(self.window, self.dx,
                       self.dy)
        for obstacle in self.obstacles:
            obstacle.draw(self.window, self.dx,
                          self.dy)
        for portal in self.portals:
            portal.draw(self.window, self.dx,
                        self.dy)
        for monster in self.monsters:
            monster.draw(self.window, self.dx,
                         self.dy)
        player.draw(self.window, self.dx,
                    self.dy)
        ##### Your Code Here ↑ #####


class StartMenu():
    def __init__(self, window):
        ##### Your Code Here ↓ #####
        self.bg = pygame.image.load(GamePath.menu)
        self.bg = pygame.transform.scale(self.bg, (WindowSettings.width,
                                                   WindowSettings.height))
        self.window = window
        self.font = pygame.font.Font(None, ManuSettings.textSize)
        self.text = self.font.render('Press ENTER to start', True, (255, 255, 255))
        self.textRect = self.text.get_rect(center=(WindowSettings.width // 2,
                                                   WindowSettings.height - 50))
        self.blinkTimer = 0
        ##### Your Code Here ↑ #####

    def render(self, time):
        ##### Your Code Here ↓ #####
        self.window.blit(self.bg, (0, 0))

        self.blinkTimer += 1
        if self.blinkTimer < time:
            self.window.blit(self.text, self.textRect)
        elif self.blinkTimer == time * 2:
            self.blinkTimer = 0

        ##### Your Code Here ↑ #####


class CityScene(Scene):
    def __init__(self, window):
        super().__init__(window=window)
        self.gen_CITY()
        self.sceneType = SceneType.CITY
        self.window = window

    def gen_city_map(self):

        ##### Your Code Here ↓ #####
        images = [pygame.image.load(tile) for tile in GamePath.cityTiles]

        for i in range(SceneSettings.tileXnum):
            for j in range(SceneSettings.tileYnum):
                self.map.add(Tile(images[randint(0, len(images) - 1)], i * SceneSettings.tileWidth,
                                  j * SceneSettings.tileHeight))

        ##### Your Code Here ↑ #####

    def gen_city_obstacle(self):
        ##### Your Code Here ↓ #####
        image = pygame.image.load(GamePath.cityWall)

        for i in range(SceneSettings.tileXnum):
            for j in range(SceneSettings.tileYnum):
                if i == 0 or i == SceneSettings.tileXnum - 1\
                        or j == 0 or j == SceneSettings.tileYnum - 1:
                    self.obstacles.add(Tile(image, i * SceneSettings.tileWidth,
                                            j * SceneSettings.tileHeight))
        ##### Your Code Here ↑ #####

    def gen_CITY(self):

        ##### Your Code Here ↓ #####
        self.gen_city_map()
        self.gen_city_obstacle()
        self.portals.add(Portal(PortalSettings.coordX,
                                PortalSettings.coordY, self.sceneType))
        ##### Your Code Here ↑ #####


class WildScene(Scene):
    def __init__(self, window):
        super().__init__(window=window)

        ##### Your Code Here ↓ #####
        self.gen_WILD()
        self.sceneType = SceneType.WILD
        self.window = window

        ##### Your Code Here ↑ #####

    def gen_wild_map(self):

        ##### Your Code Here ↓ #####
        images = [pygame.image.load(tile) for tile in GamePath.groundTiles]

        for i in range(SceneSettings.tileXnum):
            for j in range(SceneSettings.tileYnum):
                self.map.add(Tile(images[randint(0, len(images) - 1)], i * SceneSettings.tileWidth,
                                  j * SceneSettings.tileHeight))

    ##### Your Code Here ↑ #####

    def gen_wild_obstacle(self):

        ##### Your Code Here ↓ #####
        image = pygame.image.load(GamePath.tree)
        obstacles = pygame.sprite.Group()
        midX = SceneSettings.tileXnum // 2
        midY = SceneSettings.tileYnum // 2

        for i in range(SceneSettings.tileXnum):
            for j in range(SceneSettings.tileYnum):
                if random() < SceneSettings.obstacleDensity \
                        and ((i not in range(midX - 3, midX + 3))
                             or (j not in range(midY - 3, midY + 3))) \
                        and (i > midX or j > midY):
                    obstacles.add(Tile(image, i * SceneSettings.tileWidth,
                                       j * SceneSettings.tileHeight))
        return obstacles
        ##### Your Code Here ↑ #####

    def gen_WILD(self):

        ##### Your Code Here ↓ #####
        self.gen_wild_map()
        self.gen_wild_obstacle()
        ##### Your Code Here ↑ #####

    def gen_monsters(self, num=10):

        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####


class BossScene(Scene):
    def __init__(self, window):
        super().__init__(window=window)
        self.gen_BOSS()
        self.type = SceneType.BOSS

    # Overwrite Scene's function
    def trigger_battle(self, player):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    def gen_boss_obstacle(self):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    def gen_boss_map(self):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    def gen_BOSS(self):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####
