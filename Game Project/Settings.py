# -*- coding:utf-8 -*-

from enum import Enum
import pygame


class WindowSettings:
    name = "Thgink Luos"
    width = 1280
    height = 720
    outdoorScale = 1.5  # A necessary scale to allow camera movement in outdoor scenes
    fps = 30


class SceneSettings:
    tileXnum = 48  # 64
    tileYnum = 27  # 36
    tileWidth = tileHeight = 40
    obstacleDensity = 0.1


class ManuSettings:
    textSize = 30
    blinkInterval = 30


class PlayerSettings:
    # Initial Player Settings
    playerSpeed = 5
    playerWidth = 60
    playerHeight = 55
    playerHP = 20
    playerAttack = 5
    playerDefence = 1
    playerMoney = 100


class PlayerDirection(Enum):
    Right = 2
    Left = 1
    Up = 3
    Down = 0


class NPCSettings:
    npcSpeed = 1
    npcWidth = 60
    npcHeight = 60
    talkCD = 2 * WindowSettings.fps  # 2秒


class NPCType(Enum):
    DIALOG = 1
    MONSTER = 2
    SHOP = 3


class Action(Enum):
    SITTING = 1
    STANDING = 2
    DIE = 3


class BossSettings:
    width = 300
    height = 300
    coordX = (SceneSettings.tileXnum / 2) * SceneSettings.tileWidth - width / 2
    coordY = (SceneSettings.tileYnum / 2) * SceneSettings.tileHeight - height / 2


class SceneType(Enum):
    CITY = 1
    WILD = 2
    BOSS = 3


class DialogSettings:
    boxWidth = 800
    boxHeight = 180
    boxStartX = WindowSettings.width // 4  # Coordinate X of the box
    boxStartY = WindowSettings.height // 3 * 2 + 20  # Coordinate Y of the box

    textSize = 48  # Default font size
    textStartX = WindowSettings.width // 4 + 10  # Coordinate X of the first line of dialog
    textStartY = WindowSettings.height // 3 * 2 + 30  # Coordinate Y of the first line of dialog
    textVerticalDist = textSize // 4 * 3  # Vertical distance of two lines

    npcWidth = WindowSettings.width // 5
    npcHeight = WindowSettings.height // 3
    npcCoordX = 0
    npcCoordY = WindowSettings.height * 2 // 3 - 20


class BattleSettings:
    boxWidth = WindowSettings.width * 3 // 4
    boxHeight = WindowSettings.height * 3 // 4
    boxStartX = WindowSettings.width // 8  # Coordinate X of the box
    boxStartY = WindowSettings.height // 8
    textSize = 48  # Default font size
    textStartX = WindowSettings.width // 4
    textPlayerStartX = WindowSettings.width // 4  # Coordinate X of the first line of dialog
    textMonsterStartX = WindowSettings.width // 2 + 100
    textStartY = WindowSettings.height // 3  # Coordinate Y of the first line of dialog
    textVerticalDist = textSize // 4 * 3  # Vertical distance of two lines

    playerWidth = WindowSettings.width // 6
    playerHeight = WindowSettings.height // 3
    playerCoordX = WindowSettings.width // 8
    playerCoordY = WindowSettings.height // 2

    monsterWidth = WindowSettings.width // 6
    monsterHeight = WindowSettings.height // 3
    monsterCoordX = WindowSettings.width * 5 // 8
    monsterCoordY = WindowSettings.height // 2

    stepSize = 20
    animationFrameCount = 15


class ShopSettings:
    boxWidth = 800
    boxHeight = 200
    boxStartX = WindowSettings.width // 4  # Coordinate X of the box
    boxStartY = WindowSettings.height // 3  # Coordinate Y of the box

    textSize = 56  # Default font size
    textStartX = boxStartX + 10  # Coordinate X of the first line of dialog
    textStartY = boxStartY + 25  # Coordinate Y of the first line of dialog


class GamePath:
    # Window related path
    menu = r".\assets\background\menu.png"
    wild = r".\assets\background\wild.png"
    mapBlock = r".\assets\background\map.png"

    # player/npc related path
    npc = r".\assets\npc\npc.png"
    player = [
        [r".\assets\player\1.png",
         r".\assets\player\2.png",
         r".\assets\player\3.png",
         r".\assets\player\4.png"],
        [r".\assets\player\5.png",
         r".\assets\player\6.png",
         r".\assets\player\7.png",
         r".\assets\player\8.png"],
        [r".\assets\player\9.png",
         r".\assets\player\10.png",
         r".\assets\player\11.png",
         r".\assets\player\12.png"],
        [r".\assets\player\13.png",
         r".\assets\player\14.png",
         r".\assets\player\15.png",
         r".\assets\player\16.png"]]
    monster = [[r".\assets\npc\monster\1\1.png",
                r".\assets\npc\monster\1\2.png",
                r".\assets\npc\monster\1\3.png",
                r".\assets\npc\monster\1\4.png",
                r".\assets\npc\monster\1\5.png",
                r".\assets\npc\monster\1\6.png"],
               [r".\assets\npc\monster\2\1.png",
                r".\assets\npc\monster\2\2.png",
                r".\assets\npc\monster\2\3.png",
                r".\assets\npc\monster\2\4.png",
                r".\assets\npc\monster\2\5.png",
                r".\assets\npc\monster\2\6.png"],
               [r".\assets\npc\monster\3\1.png",
                r".\assets\npc\monster\3\2.png",
                r".\assets\npc\monster\3\3.png",
                r".\assets\npc\monster\3\4.png",
                r".\assets\npc\monster\3\5.png",
                r".\assets\npc\monster\3\6.png"]
               ]
    boss = r".\assets\npc\boss.png"

    groundTiles = [
        r".\assets\tiles\ground1.png",
        r".\assets\tiles\ground2.png",
        r".\assets\tiles\ground3.png",
        r".\assets\tiles\ground4.png",
        r".\assets\tiles\ground5.png",
        r".\assets\tiles\ground6.png",
    ]

    cityTiles = [
        r".\assets\tiles\city1.png",
        r".\assets\tiles\city2.png",
        r".\assets\tiles\city3.png",
        r".\assets\tiles\city4.png",
        r".\assets\tiles\city5.png",
        r".\assets\tiles\city6.png",
    ]

    cityWall = r".\assets\tiles\cityWall.png"

    bossTiles = [
        r".\assets\tiles\boss1.png",
        r".\assets\tiles\boss2.png",
        r".\assets\tiles\boss3.png",
        r".\assets\tiles\boss4.png",
        r".\assets\tiles\boss5.png",
        r".\assets\tiles\boss6.png",
    ]

    bossWall = r".\assets\tiles\bossWall.png"

    portal = r".\assets\background\portal.png"

    tree = r".\assets\tiles\tree.png"

    bgm = [r".\assets\bgm\city.mp3",
           r".\assets\bgm\wild.mp3",
           r".\assets\bgm\boss.mp3"]


class PortalSettings:
    width = 320
    height = 320
    coordX = (SceneSettings.tileXnum - 10) * SceneSettings.tileWidth - width / 2
    coordY = (SceneSettings.tileYnum / 2) * SceneSettings.tileHeight - height / 2


class GameState(Enum):
    MAIN_MENU = 1
    GAME_TRANSITION = 2
    GAME_OVER = 3
    GAME_WIN = 4
    GAME_PAUSE = 5
    GAME_PLAY_WILD = 6
    GAME_PLAY_CITY = 7
    GAME_PLAY_BOSS = 8


class GameEvent:
    EVENT_BATTLE = pygame.USEREVENT + 1
    EVENT_DIALOG = pygame.USEREVENT + 2
    EVENT_SWITCH = pygame.USEREVENT + 3
    EVENT_RESTART = pygame.USEREVENT + 4
    EVENT_SHOP = pygame.USEREVENT + 5
