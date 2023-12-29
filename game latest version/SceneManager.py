# -*- coding:utf-8 -*-

from Settings import *
import pygame
import Map
import DialogBox
import NPC
import Monster
import BattleBox
class SceneManager:
    def __init__(self, window):
        self.state = GameState.GAME_PLAY_WILD
        self.map = Map.gen_map()
        self.cameraX = 0
        self.cameraY = 0
        self.npcs = pygame.sprite.Group()
        self.npcs.add(NPC.NPC(WindowSettings.width // 4, WindowSettings.height // 4 + 80))
        self.player_speed = PlayerSettings.playerSpeed

        self.obstacles = Map.build_obstacles()
        self.window = window
        self.x_direction, self.y_direction = 0, 0

        self.monsters = pygame.sprite.Group()
        self.monsters.add(Monster.Monster(WindowSettings.width // 4, WindowSettings.height // 4 + 180))
        self.battleBox = None

    def get_width(self):
        return WindowSettings.width * WindowSettings.outdoorScale

    def get_height(self):
        return WindowSettings.height * WindowSettings.outdoorScale
    
    def check_event_talking(self, player, keys):
        for npc in self.npcs:
            if npc.talking and keys[pygame.K_RETURN]:
                npc.talking = False
                player.talking = False
                npc.reset_talk_CD()
            elif npc.can_talk() and pygame.sprite.collide_rect(npc, player):
                npc.talking = True
                player.talking = True
                dialogTemp = DialogBox.DialogBox(self.window, GamePath.npc,
                                                 ["Happy", "2023!"])
                dialogTemp.render()

    def check_event_battle(self, player, keys):
        if self.battleBox is None:
            for monster in self.monsters:
                if pygame.sprite.collide_rect(player, monster):
                    self.battleBox = BattleBox.BattleBox(self.window,
                                                         player, monster)
                    self.battleBox.render()
        else:
            self.battleBox.render()

    def update_camera(self, player):
        self.x_direction, self.y_direction = 0, 0
        if player.rect.x > WindowSettings.width / 4 * 3:
            self.cameraX += player.speed
            if self.cameraX < self.get_width() - WindowSettings.width:
                player.fix_to_middle(player.speed, 0)
                self.x_direction = -1
            elif self.cameraX == self.get_width() - WindowSettings.width:
                self.x_direction = -1
            else:
                self.cameraX = self.get_width() - WindowSettings.width
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
            if self.cameraY < self.get_height() - WindowSettings.height:
                player.fix_to_middle(0, player.speed)
                self.y_direction = -1
            elif self.cameraY == self.get_height() - WindowSettings.height:
                self.y_direction = -1
            else:
                self.cameraY = self.get_height() - WindowSettings.height
        elif player.rect.y < WindowSettings.height/ 4:
            self.cameraY -= player.speed
            if self.cameraY > 0:
                player.fix_to_middle(0, -player.speed)
                self.y_direction = 1
            elif self.cameraY == 0:
                self.y_direction = 1
            else:
                self.cameraY = 0

    def update(self):
        for npc in self.npcs:
            npc.update()

    def render(self):
        for i in range(SceneSettings.tileXnum):
            for j in range(SceneSettings.tileYnum):
                self.window.blit(self.map[i][j], 
                                 (i * SceneSettings.tileWidth - self.cameraX,
                                  j * SceneSettings.tileHeight - self.cameraY))

        for obstacle in self.obstacles:   # 障碍物镜头移动
            obstacle.move(self.x_direction * self.player_speed, self.y_direction * self.player_speed)
        self.obstacles.draw(self.window)

        for npc in self.npcs:   # NPC镜头移动
            npc.move(self.x_direction * self.player_speed, self.y_direction * self.player_speed)

        for monster in self.monsters:
            monster.move(self.x_direction * self.player_speed, self.y_direction * self.player_speed)
        self.npcs.draw(self.window)
        self.monsters.draw((self.window))

    
