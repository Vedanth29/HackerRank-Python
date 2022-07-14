#Vedanth M
# rock paper scissor game 
def welcome_msg() :
    text = '''
################################################
Welcome to Rock , Paper and Scissor Game-V1.0.0
Developed by Vedanth M
################################################
'''
    print(text)

welcome_msg()
import random

def GameWin(comp,you):

  
    if comp == you:
        return None

    elif comp == 'r':
            if you == 's':
                return False
            elif you =='p':
                return True
  
    elif comp == 'p':
            if you =='r':
                return False
            elif you == 's':
                return True

    elif comp == 's':
            if you =='p':
                return False
            elif you == 'r':
                return True

player = input('enter your name:-')

print('Computer turn: Rock(r), Paper(p) or Scissor(s):')

randnum = random.randint(1,3)

if randnum == 1:
    comp = 'r'
   
elif randnum == 2:
    comp = 'p'
   
elif randnum == 3:
    comp = 's'


you = input(f'{player} turn: Rock(r), Paper(p) or Scissor(s)?:\n')

g = GameWin(comp,you)

print(f'computer choose {comp}')
print(f'you choose {you}')


if g == None:
    print('The match is tie between both the players')
elif g:
    print(f'****** {player} won the game ******')
else:
    print('****** Computer won the game ******')
    
