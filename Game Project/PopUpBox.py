# -*- coding:utf-8 -*-

import pygame

from typing import *
from Settings import *

class DialogBox:
    def __init__(self, window, npc,
                 fontSize: int = DialogSettings.textSize, 
                 fontColor: Tuple[int, int, int] = (255, 255, 255), 
                 bgColor: Tuple[int, int, int, int] = (0, 0, 0, 150)):
        ##### Your Code Here ↓ #####
        self.window = window

        self.fontSize = fontSize
        self.fontColor = fontColor
        self.font = pygame.font.Font(None, self.fontSize)

        self.bg = pygame.Surface((DialogSettings.boxWidth, DialogSettings.boxHeight),
                                 pygame.SRCALPHA)
        self.bg.fill(bgColor)

        self.npc = npc
        ##### Your Code Here ↑ #####
        
    def draw(self):
        ##### Your Code Here ↓ #####
        self.window.blit(self.bg, (DialogSettings.boxStartX, DialogSettings.boxStartY))
        ##### Your Code Here ↑ #####
        

class BattleBox:
    def __init__(self, window, player, monster, fontSize: int = BattleSettings.textSize, 
                 fontColor: Tuple[int, int, int] = (255, 255, 255), bgColor: Tuple[int, int, int, int] = (0, 0, 0, 200)) :
        ##### Your Code Here ↓ #####

        self.window = window

        self.fontSize = fontSize
        self.fontColor = fontColor
        self.font = pygame.font.Font(None, self.fontSize)

        self.bg = pygame.Surface((BattleSettings.boxWidth, BattleSettings.boxHeight),
                                 pygame.SRCALPHA)
        self.bg.fill(bgColor)

        # 初始化相关角色的参数，没有实际操作的权力
        self.player = player
        self.playerHP = player.HP
        self.playerImg = pygame.image.load(GamePath.player[0])
        self.playerImg = pygame.transform.scale(self.playerImg,
                                                (BattleSettings.playerWidth,BattleSettings.playerHeight))

        self.playerX = BattleSettings.playerCoordX
        self.playerY = BattleSettings.playerCoordY

        self.monster = monster
        self.monsterHP = monster.HP
        self.monsterImg = pygame.image.load((GamePath.monster[0]))
        self.monsterImg = pygame.transform.scale(self.monsterImg,
                                                 (BattleSettings.monsterWidth, BattleSettings.monsterHeight))
        self.monsterImg = pygame.transform.flip(self.monsterImg, True, False)

        self.monsterX = BattleSettings.monsterCoordX
        self.monsterY = BattleSettings.monsterCoordY
        # 默认玩家先手
        self.attacker = 0
        # 区分放动画状态和攻击结算状态
        self.isPlayingAnimation= True
        self.currentPlayingCount = 0
        # 移动方向
        self.dir = 1
        # 是否结束
        self.isFinished = False

        ##### Your Code Here ↑ #####


    def draw(self):
        ##### Your Code Here ↓ #####

        # 绘制背景和文字
        self.window.blit(self.bg, (BattleSettings.boxStartX, BattleSettings.boxStartY))
        self.window.blit(self.playerImg, (self.playerX, self.playerY))
        self.window.blit(self.monsterImg, (self.monsterX, self.monsterY))
        # 绘制战斗过程
        if self.isPlayingAnimation:
            if self.currentPlayingCount < BattleSettings.animationFrameCount:
                currentDir = self.dir
            else:
                currentDir = self.dir * -1

            if self.attacker == 0:
                self.playerX += currentDir * BattleSettings.stepspeed
            else:
                self.monsterX += currentDir * BattleSettings.stepspeed

            self.currentPlayingCount += 1

            if self.currentPlayingCount == 30:
                self.isPlayingAnimation = False
                self.currentPlayingCount = 0

        # 战斗判定以及结算
        else:
            if self.attacker == 0:
                self.monsterHP -= (self.player.Attack - self.monster.defence)
                self.attacker = 1
                self.dir = -1
                if self.monsterHP <= 0:
                    self.monsterHP = 0

            else:
                self.playerHP -= (self.monster.attack - self.player.Defence)
                self.attacker = 0
                self.dir = 1
                if self.playerHP <= 0:
                    self.playerHP = 0

        self.isPlayingAnimation = True

        text = 'player HP:' + str(self.playerHP)
        self.window.blit(self.font.render(text, True, self.fontColor),
                         (BattleSettings.textPlayerStartX, BattleSettings.textStartY))

        text = 'monster HP:' + str(self.monsterHP)
        self.window.blit(self.font.render(text, True, self.fontColor),
                         (BattleSettings.textMonsterStartX, BattleSettings.textStartY))
        # 战斗结束
        if self.playerHP == 0 or self.monsterHP == 0:
            self.isFinished = True

        ##### Your Code Here ↑ #####

class ShoppingBox:
    def __init__(self, window, npc, player,
                 fontSize: int = DialogSettings.textSize, 
                 fontColor: Tuple[int, int, int] = (255, 255, 255), 
                 bgColor: Tuple[int, int, int, int] = (0, 0, 0, 150)):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    def buy(self):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    def draw(self):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####
