# -*- coding:utf-8 -*-

import sys
import pygame

import NPCs
from Player import Player
from Scene import *
from Settings import *
from PopUpBox import *


class GameManager:
    def __init__(self):

        ##### Your Code Here ↓ #####
        self.window = pygame.display.set_mode((WindowSettings.width,
                                               WindowSettings.height))
        pygame.display.set_caption(WindowSettings.name)
        self.fps = WindowSettings.fps
        self.clock = pygame.time.Clock()
        self.state = GameState.MAIN_MENU
        self.sceneType = None
        self.scene = None
        self.obstacles = None
        self.battleBox = None
        self.keys = None
        self.player = Player(WindowSettings.width // 2, WindowSettings.height // 2)
        ##### Your Code Here ↑ #####

    def game_reset(self):

        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    # Necessary game components here ↓
    def tick(self, fps):
        ##### Your Code Here ↓ #####
        self.clock.tick(fps)
        ##### Your Code Here ↑ #####

    def get_time(self):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    # Scene-related update functions here ↓
    def flush_scene(self, GOTO: SceneType):
        ##### Your Code Here ↓ #####
        if GOTO == SceneType.CITY:
            self.scene = CityScene(self.window)
            self.state = GameState.GAME_PLAY_CITY
        ##### Your Code Here ↑ #####

    def update(self):
        ##### Your Code Here ↓ #####
        self.tick(self.fps)
        self.keys = pygame.key.get_pressed()
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == GameEvent.EVENT_SWITCH:
                self.flush_scene(self.sceneType)
        if self.state == GameState.MAIN_MENU:
            self.update_main_menu(events)
        elif self.state == GameState.GAME_PLAY_WILD:
            self.update_wild(events)
        elif self.state == GameState.GAME_PLAY_CITY:
            self.update_city(events)
        elif self.state == GameState.GAME_PLAY_BOSS:
            self.update_boss(events)


        ##### Your Code Here ↑ #####

    def update_main_menu(self, events):
        ##### Your Code Here ↓ #####
        if self.keys[pygame.K_RETURN]:
            self.sceneType = SceneType.CITY
            pygame.event.post(pygame.event.Event(GameEvent.EVENT_SWITCH))
        ##### Your Code Here ↑ #####

    def update_city(self, events):
        # Deal with EventQueue First
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

        # Then deal with regular updates
        ##### Your Code Here ↓ #####
        self.player.update(self.player.try_move(self.keys)[0],
                           self.player.try_move(self.keys)[1])
        self.scene.update_camera(self.player)
        ##### Your Code Here ↑ #####

    def update_wild(self, events):
        # Deal with EventQueue First
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

        # Then deal with regular updates
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    def update_boss(self, events):
        # Deal with EventQueue First
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

        # Then deal with regular updates
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    # Collision-relate update funtions here ↓
    def update_collide(self):
        # Player -> Obstacles
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

        # Player -> NPCs; if multiple NPCs collided, only first is accepted and dealt with.
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

        # Player -> Monsters
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

        # Player -> Portals
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

        # Player -> Boss
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    def update_NPCs(self):
        # This is not necessary. If you want to re-use your code you can realize this.
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    # Render-relate update functions here ↓
    def render(self):
        ##### Your Code Here ↓ #####
        if self.state == GameState.MAIN_MENU:
            self.render_main_menu()
        elif self.state == GameState.GAME_PLAY_WILD:
            self.render_wild()
        elif self.state == GameState.GAME_PLAY_CITY:
            self.render_city()
        elif self.state == GameState.GAME_PLAY_BOSS:
            self.render_boss()
        ##### Your Code Here ↑ #####

    def render_main_menu(self):
        ##### Your Code Here ↓ #####
        main_manu = StartMenu(self.window)
        main_manu.render(30)
        ##### Your Code Here ↑ #####

    def render_city(self):
        ##### Your Code Here ↓ #####
        self.scene.render(self.player)
        ##### Your Code Here ↑ #####

    def render_wild(self):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    def render_boss(self):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

