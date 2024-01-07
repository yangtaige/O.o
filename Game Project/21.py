import random
cards = [2,3,4,5,6,7,8,9,10,'J','Q','K','A']
def get_score(hand):
    score = sum(cards.index(card) for card in hand)
    if 'A' in hand:
        if score + 11 <= 21:
            return score + 11
        else:
            return score + 1
    else:
        return score
def deal_cards():
    return(random.choice(cards) for _ in range(2))
def play_game():
    player_hand = deal_cards()
    computer_hand = deal_cards()    
    player_score = get_score(player_hand)
    computer_score = get_score(computer_hand)
    print(f'玩家手中有：{player_hand}')
    print(f'电脑手中有:{computer_hand}')
    while player_score < 21 and computer_score < 21:
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



        

