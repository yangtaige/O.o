# -*- coding:utf-8 -*-

from Settings import *
import pygame
import Map
import DialogBox
import NPC

class SceneManager:
    def __init__(self, window):
        self.state = GameState.GAME_PLAY_WILD
        self.map = Map.gen_map()
        
        self.window = window
        self.clock = pygame.time.Clock()
        self.cameraX = 0
        self.cameraY = 0
        self.obstacle = Map.build_obstacle()

    def tick(self, fps):
        pass
    
    def get_width(self):
        return WindowSettings.width * WindowSettings.outdoorScale

    def get_height(self):
        return WindowSettings.height * WindowSettings.outdoorScale

    def update_camera(self, player):
        if player.rect.x > WindowSettings.width / 4 * 3:
            self.cameraX += player.speed
            if self.cameraX < self.get_width() - WindowSettings.width:
                player.fix_to_middle(player.speed,0)
            else:
                self.cameraX = self.get_width() - WindowSettings.width
        elif player.rect.x < (WindowSettings.width - player.rect.x) / 4:
            self.cameraX -= player.speed
            if self.cameraX > 0:
                player.fix_to_middle(-player.speed, 0)
            else:
                self.cameraX = 0

        if player.rect.y > WindowSettings.height / 4 * 3:
            self.cameraY += player.speed
            if self.cameraY < self.get_height() - WindowSettings.height:
                player.fix_to_middle(0, player.speed)
            else:
                self.cameraY = self.get_height() - WindowSettings.height
        elif player.rect.y < (WindowSettings.height - player.rect.y) / 4:
            self.cameraY -= player.speed
            if self.cameraY > 0:
                player.fix_to_middle(0, -player.speed)
            else:
                self.cameraY = 0
    def render(self):
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                self.window.blit(self.map[i][j],
                                 (i * SceneSettings.tileWidth - self.cameraX,
                                  j * SceneSettings.tileHeight - self.cameraY))
