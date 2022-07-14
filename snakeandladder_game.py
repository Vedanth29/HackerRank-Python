# Project1- Snake and Ladder Game
# Developed by Vedanth M emailid-mvedanth28@gmail.com
#
# importing the built-in modules
# 
import random
import time
import sys

max_value = 100

ladderDict = {
    '1' :'38',
    '4' :'14',
    '9' :'31',
    '21':'42',
    '28':'84',
    '51':'67',
    '72':'91',
    '80':'99'
}

SnakeDict = {
    '17':'7',
    '54':'34',
    '62':'19',
    '64':'60',
    '87':'36',
    '93':'73',
    '95':'75',
    '98':'79'
}

#sound effects

snakesound_Dict = {
    'hisss aww noh!',
    'ohhh noo poor',
    'snake bite!!',
    'aww noo bad'
    'my fate !!!'
}

laddersound_Dict ={
    'wooww congrats!',
    'omg awsome ;)',
    'yaayy hurray',
    'congrats awsome',
    'ohh my god, Lucky'
}


def welcome():
    text = ''' 
            Welcome to Snake & Ladder Game -version:1.0.0
            Developed by Vedanth M 

        ******************************************************************************

            rules-
            1- Initially Both the players are at the starting point.
            2 -Roll the dice to move forward in the game.
            3 -If you land at the bottom of the ladder move to the top of that ladder.
            4 -If you land at the top of snake move to the bottom of that snake.
            5 -The first player who get to the final position is the WINNER ;)

        ******************************************************************************
            '''
    print(text)

welcome()

def player_name():
    player1_name = input('enter the name of player 1:\n')
    player2_name = input('enter the name of player 2:\n')
    print('The match will be played between '+player1_name+' and '+player2_name+'\n')

#player_name()

def dice_value():
    dice_value = random.randint(1, 6)
    print("Its a " + str(dice_value))
    return dice_value

#dice_value()

def snake_bite(old_value,cur_value,player_name): 
    print('\n'+ random.choice(snakesound_Dict).upper()+ '----------->')
    print('\n'+ player_name +' got a snake bite. Down from '+str(old_value)+' to '+str(cur_value))

#snake_bite()

def ladder_jump(old_value,cur_value,player_name):
    print('\n'+random.choice(laddersound_Dict).upper()+'#############')
    print('\n'+ player_name +' climber the ladder from '+str(old_value)+' to '+str(cur_value))

#ladder_jump()

def snake_ladder(player_name,cur_value,dice_value):
    old_value = cur_value
    cur_value = cur_value + dice_value
    
    if cur_value > max_value:
        print('you need to win ')

