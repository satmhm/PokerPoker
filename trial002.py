from multiprocessing.sharedctypes import Value
from re import A
import numpy as np
import random


def Poker():
    #Number of Player
    average, shape = 7, 0.5
    X = np.random.lognormal(mean=average, sigma=shape, size=1)
    X = np.log2(X)
    Y = int(X)

    #Card Availability 
    Card = [x for x in range (1,53,1)]

    #Card on Player hand
    Card_dist = []
    for i in range(2*Y):
        Card_dist.append(random.choice(Card))
        Card = [x for x in Card if x not in Card_dist]
    
    #Player's Money
    dealer = [100]
    money = [100 for i in range(Y)]
    id = list(range(Y))
    id_money = {key: value for key, value in zip(id, money)}
    money_table = sum(id_money.values())   

    #Player's Card
    Card_dist_01 = np.array_split(Card_dist, Y)
    Card_dist_02 = np.array(Card_dist_01)
    Card_dist_03 = Card_dist_02.tolist()

    id_card = {key: value for key, value in zip(id, Card_dist_03)}
    
    #Card on Dealer: Before Round 1 (FLOP)
    Card_00 = Card

    #BET FIRST

    #First Round (FLOP): 3 Card on Table
    Card_table_1 = []
    for i in range(3):
        Card_table_1.append(random.choice(Card_00))
        Card_00 = [x for x in Card_00 if x not in Card_table_1]
    Card_01 = Card_00

    #BET SECOND

    #Second Round (TURN): 3 + 1 = 4 Card on Table
    Turn = [random.choice(Card_01)]
    Card_02 = [x for x in Card_01 if x not in Turn]
    Card_table_2 = Card_table_1 + Turn

    #BET THIRD
    

    #Thir Round (River): 4 + 1 = 5 Card on Table
    River = [random.choice(Card_02)]
    Card_03 = [x for x in Card_02 if x not in River]
    Card_table_3 = Card_table_2 + River

    #BET FOURTH

    total_card = len(Card_dist+Card_table_3+Card_03)    

    return (
        #Card_dist, 
        #Card_table_3, 
        #Card_03, 
        #total_card,
        Y
        #id_card, 
        #id_money
    )
    
    
    






    
    



        



       