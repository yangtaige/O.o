# import random
# cards = [2,3,4,5,6,7,8,9,10,'J','Q','K','A']
# def get_score(hand):
#     score = sum(cards.index(card) for card in hand)
#     if 'A' in hand:
#         if score + 11 <= 21:
#             return score + 11
#         else:
#             return score + 1
#     else:
#         return score
# def deal_cards():
#     return(random.choice(cards) for _ in range(2))
# def play_game():
#     player_hand = deal_cards()
#     computer_hand = deal_cards()    
#     player_score = get_score(player_hand)
#     computer_score = get_score(computer_hand)
#     print(f'玩家手中有：{player_hand}')
#     print(f'电脑手中有:{computer_hand}')
#     while player_score < 21 and computer_score < 21:
#         print('玩家决策')
#         while True:
#             decision = input() #1：要牌；0：不要牌
#             if decision == 1:
#                 player_hand.append(random.choice(cards))
#                 player_score = get_score(player_hand)
#                 print(f'玩家手中有：{player_hand}')
#             elif decision == 0:
#                 break
#             else:
#                 print('输入无效,请重新输入0(不要牌)或1(要牌)')
#         if player_score > 21:
#             print('失败请重新再来')
#         if player_score == 21:
#             print('恭喜你,看看电脑能否和你一样lucky~')
#         else:
#             print(f'玩家得分：{player_score}')
#         computer_decision = random.choice([0,1])
#         if computer_decision == 0:
#             pass
#         elif computer_decision == 1:
#             computer_hand.append(random.choice(cards))  
#             computer_score = get_score(computer_hand)  
#             print(f'电脑手中有: {computer_hand}')  
#         if player_score <= 21 and computer_score <= 21:
#             if player_score <= computer_score:
#                 print('别灰心,再来一次')
#             if player_score == 21 and player_score > computer_score:
#                print('恭喜你,完美通关') 
#             else:
#                 print('恭喜你，通关')
import pygame
import random
from Settings import *
# 初始化 Pygame
pygame.init()

# 设置游戏窗口
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('21点游戏')

# 加载背景音乐和图片
background_image = pygame.image.load(r".\assets\cards\55.png")
card_images = [pygame.transform.scale(pygame.image.load(img), (PlayerSettings.cardswidth,
                                            PlayerSettings.cardsheight)) for img in GamePath.card_images]
# card_images_rect = [img.get_rect() for img in card_images]

# 发牌
def deal_card():
    number = random.randint(0,51)
    if card_images[number] != None:
         card = card_images[number]
         card_images[number] = None
         return (card, number)
    else: 
        deal_card()
# 显示牌
def show_card(card, x, y):
    screen.blit(card, (x, y))


def get_score(hand):
    score = sum(hand)
    if 'A' in hand:
        if score + 11 <= 21:
            return score + 11
        else:
            return score + 1
    else:
        return score
    

def play_game():
    player_score = get_score(player_cards)
    dealer_score = get_score(dealer_cards)
    while player_score < 21 and dealer_score < 21:
        print('玩家决策')
        while True:
            decision = input() #1：要牌；0：不要牌
            if decision == 1:
                player_hand.append(random.choice(cards))
                player_score = get_score(player_hand)
                print(f'玩家手中有：{player_hand}')
            elif decision == 0:
                break
            else:
                print('输入无效,请重新输入0(不要牌)或1(要牌)')
        if player_score > 21:
            print('失败请重新再来')
        if player_score == 21:
            print('恭喜你,看看电脑能否和你一样lucky~')
        else:
            print(f'玩家得分：{player_score}')
        computer_decision = random.choice([0,1])
        if computer_decision == 0:
            pass
        elif computer_decision == 1:
            computer_hand.append(random.choice(cards))  
            computer_score = get_score(computer_hand)  
            print(f'电脑手中有: {computer_hand}')  
        if player_score <= 21 and computer_score <= 21:
            if player_score <= computer_score:
                print('别灰心,再来一次')
            if player_score == 21 and player_score > computer_score:
               print('恭喜你,完美通关') 
            else:
                print('恭喜你，通关')

# 主循环
m1 = deal_card()
m2 = deal_card()
m3 = deal_card()
m4 = deal_card()
player_cards = [m1[0], m3[0]]
dealer_cards = [m2[0], m4[0]]
player_value = [m1[1],m3[1]]
dealer_value = [m2[1],m4[1]]
running = True
screen.blit(background_image, (0, 0))
n = 0
while running:
    
    # 玩家和庄家发牌
    

    # 显示玩家和庄家的牌
    show_card(player_cards[0], 100, 300)
    show_card(player_cards[1], 240, 300)
    show_card(dealer_cards[0], 100, 100)
    show_card(dealer_cards[1], 240, 100)
    # 处理玩家操作
    # ...
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:  # 检测按键按下事件
            if event.key == pygame.K_t: 
                player_cards.append(deal_card()[0])
                n += 1
                show_card(player_cards[-1], (240 + 140*n), 300)
            elif event.key == pygame.K_f: 
                 running = False

    # 计算点数并判断输赢
    # ...

    # 处理游戏结束
    # ...

    pygame.display.flip()

    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# 退出游戏
pygame.quit()



        

