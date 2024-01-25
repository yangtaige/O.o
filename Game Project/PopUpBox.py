# -*- coding:utf-8 -*-

import pygame

from typing import *
from Settings import *


class DialogBox:
    def __init__(self, window, npc, dialog,
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
        self.dialog = dialog

        self.npc = pygame.transform.scale(npc.image, (DialogSettings.npcWidth,
                                                      DialogSettings.npcHeight))
        ##### Your Code Here ↑ #####

    def draw(self):
        ##### Your Code Here ↓ #####
        self.window.blit(self.bg, (DialogSettings.boxStartX, DialogSettings.boxStartY))
        self.window.blit(self.npc, (DialogSettings.npcCoordX, DialogSettings.npcCoordY))

        offset = 0
        for text in self.dialog:
            self.window.blit(self.font.render(text, True, self.fontColor),
                             (DialogSettings.textStartX, DialogSettings.textStartY + offset))
            offset += DialogSettings.textVerticalDist
        ##### Your Code Here ↑ #####


class BattleBox:
    def __init__(self, window, player, monster, fontSize: int = BattleSettings.textSize,
                 fontColor: Tuple[int, int, int] = (255, 255, 255),
                 bgColor: Tuple[int, int, int, int] = (0, 0, 0, 200)):
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
        self.playerImg = self.player.images[PlayerDirection.Right.value][0]
        self.playerImg = pygame.transform.scale(self.playerImg,
                                                (BattleSettings.playerWidth, BattleSettings.playerHeight))

        self.playerX = BattleSettings.playerCoordX
        self.playerY = BattleSettings.playerCoordY

        self.monster = monster
        try:
            self.monsterImg = monster.images[monster.type][0]
        except:
            self.monsterImg = monster.image
        self.monsterImg = pygame.transform.scale(self.monsterImg,
                                                 (BattleSettings.monsterWidth, BattleSettings.monsterHeight))
        self.monsterImg = pygame.transform.flip(self.monsterImg, True, False)

        self.monsterX = BattleSettings.monsterCoordX
        self.monsterY = BattleSettings.monsterCoordY
        # 默认玩家先手
        self.attacker = 0
        # 区分放动画状态和攻击结算状态
        self.isPlayingAnimation = True
        self.currentPlayingCount = 0
        # 移动方向
        self.dir = 1
        # 是否结束
        self.isFinished = False

        ##### Your Code Here ↑ #####

    def get_result(self):
        if self.attacker == 0:
            self.monster.HP = max(0, self.monster.HP -
                                  max(0, (self.player.Attack - self.monster.defence)))
            self.attacker = 1
            self.dir = -1
        else:
            self.player.HP = max(0, self.player.HP -
                                 max(0, (self.monster.attack - self.player.Defence)))
            self.attacker = 0
            self.dir = 1

        self.isPlayingAnimation = True

    def draw(self):
        ##### Your Code Here ↓ #####
        # 绘制背景和文字
        self.window.blit(self.bg, (BattleSettings.boxStartX, BattleSettings.boxStartY))
        self.window.blit(self.playerImg, (self.playerX, self.playerY))
        self.window.blit(self.monsterImg, (self.monsterX, self.monsterY))
        text = 'player HP:' + str(self.player.HP)
        self.window.blit(self.font.render(text, True, self.fontColor),
                         (BattleSettings.textPlayerStartX, BattleSettings.textStartY))

        text = 'monster HP:' + str(self.monster.HP)
        self.window.blit(self.font.render(text, True, self.fontColor),
                         (BattleSettings.textMonsterStartX, BattleSettings.textStartY))
        # 绘制战斗过程
        if self.isPlayingAnimation:
            if self.currentPlayingCount < BattleSettings.animationFrameCount:
                currentDir = self.dir
            else:
                currentDir = self.dir * -1

            if self.attacker == 0:
                self.playerX += currentDir * BattleSettings.stepSize
            else:
                self.monsterX += currentDir * BattleSettings.stepSize

            self.currentPlayingCount += 1

            if self.currentPlayingCount == BattleSettings.animationFrameCount * 2:
                self.isPlayingAnimation = False
                self.currentPlayingCount = 0

        # 战斗判定以及结算
        elif not self.isFinished:
            self.get_result()

        if self.player.HP == 0 or self.monster.HP == 0:
            if self.monster.HP == 0:
                text = 'YOU GET ' + str(self.monster.money) + ' MONEY'
            elif self.player.HP == 0:
                text = 'YOU DIED'
            self.window.blit(self.font.render(text, True, self.fontColor),
                             (BattleSettings.textStartX,
                              BattleSettings.textStartY + BattleSettings.textVerticalDist))

            self.isFinished = True
            self.isPlayingAnimation = False
        # 战斗结束

        ##### Your Code Here ↑ #####


class ShoppingBox:
    def __init__(self, window, npc, player,
                 fontSize: int = DialogSettings.textSize,
                 fontColor: Tuple[int, int, int] = (255, 255, 255),
                 bgColor: Tuple[int, int, int, int] = (0, 0, 0, 150)):
        ##### Your Code Here ↓ #####
        self.window = window
        self.fontSize = fontSize
        self.fontColor = fontColor
        self.font = pygame.font.Font(None, self.fontSize)
        self.bg = pygame.image.load(GamePath.shopBackground)
        self.bg = pygame.transform.scale(self.bg, (ShopSettings.boxWidth, ShopSettings.boxHeight))
        self.items = npc.items
        self.npc = npc
        self.npc_image = pygame.transform.scale(self.npc.image, (DialogSettings.npcWidth,
                                                                 DialogSettings.npcHeight))

        self.player = player

        self.selectedID = 0
        ##### Your Code Here ↑ #####

    def buy(self):
        ##### Your Code Here ↓ #####
        if self.selectedID == 0:
            self.player.attr_update(addCoins=-15, addAttack=1)
        elif self.selectedID == 1:
            self.player.attr_update(addCoins=-15, addDefence=1)
        elif self.selectedID == 2:
            self.player.attr_update(addCoins=-15, addHP=3)
        elif self.selectedID == 3:
            self.player.attr_update(addHP=-5, addWeak=1)
        ##### Your Code Here ↑ #####

    def draw(self):
        ##### Your Code Here ↓ #####
        self.window.blit(self.bg, (ShopSettings.boxStartX, ShopSettings.boxStartY))
        self.window.blit(self.npc_image, (DialogSettings.npcCoordX, DialogSettings.npcCoordY))

        offset = 0
        texts = ["Coins: " + str(self.player.Money),
                 "HP: " + str(self.player.HP),
                 "Attack: " + str(self.player.Attack),
                 "Defence: " + str(self.player.Defence)]

        for id, item in enumerate(list(self.items.keys())):
            if id == self.selectedID:
                text = '-->' + item + ' ' + self.items[item]
            else:
                text = '    ' + item + ' ' + self.items[item]
            self.window.blit(self.font.render(text, True, self.fontColor),
                             (ShopSettings.textStartX, ShopSettings.textStartY + offset))
            offset += DialogSettings.textVerticalDist

        offset = 0
        for text in texts:
            self.window.blit(self.font.render(text, True, self.fontColor),
                             (ShopSettings.textStartX + ShopSettings.boxWidth // 4 * 3 - 60,
                              ShopSettings.textStartY + offset))
            offset += DialogSettings.textVerticalDist
        ##### Your Code Here ↑ #####
