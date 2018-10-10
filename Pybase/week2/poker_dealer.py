# 模拟斗地主发牌

# 黑桃：('\u2660')
# 红桃：('\u2666')
# 梅花：('\u2663')
# 方块：('\u2665')
import random
import os

def get_poker():
    nums = ['A'] + list(map(str, range(2,11))) + \
            list('JQK') 
    suits = ['\u2660', '\u2666', '\u2663', '\u2665']

    cards = [x + y for x in suits for y in nums]+ ['大王', '小王']
    return cards


def poker_games():
    pk = get_poker()
    random.shuffle(pk)
    input()
    print('第一个人的牌',pk[:17])
    input()
    print('第二个人的牌',pk[17:34])
    input()
    print('第三个人的牌',pk[34:51])
    input()
    print('底牌',pk[51:])
    


poker_games()
