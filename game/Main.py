# -*- coding:utf-8 -*-

import pygame
import sys

from SceneManager import SceneManager
from Settings import *
from Player import Player

def run_game():
    pygame.init()

    window = pygame.display.set_mode((WindowSettings.width,
    WindowSettings.height))
    pygame.display.set_caption(WindowSettings.name)

    scene = SceneManager(window)

    # 创建角色 和 NPC 精灵
    player = Player(WindowSettings.width // 2, WindowSettings.height // 2)
    clock = pygame.time.Clock()

    # 游戏主循环
    while True:
        clock.tick(30)  # 控制帧率

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # 获取按键状态
        keys = pygame.key.get_pressed()


        # 更新 NPC / Player
        player.update(keys, scene)    # 主要是角色移动
        scene.update_camera(player)   # 主要是场景中对象的动画更新，暂时不涉及player的部分
    
        # 渲染场景
        scene.render()

        # 渲染player
        player.render(window)

        scene.check_event_talking(player, keys)

        pygame.display.flip()

if __name__ == "__main__":
    run_game()
