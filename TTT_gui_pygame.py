#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import TTT_game_env
import pygame


# In[4]:


pygame.init()
white = (255,255,255)
green = (0, 255, 0) 
blue = (0, 0, 128) 
gameDisplay = pygame.display.set_mode((300,300))
pygame.display.set_caption('TIC TAC TOE')
clock = pygame.time.Clock()
Ximg = pygame.image.load('X img.png')
Oimg = pygame.image.load('O img.png')

crashed = False
pos_pixel={1:(0,0),2:(100,0),3:(200,0),4:(0,100),5:(100,100),6:(200,100),7:(0,200),8:(100,200),9:(200,200)}    
def pixel_pos(data):
    x,y = data
    #first row
    if x <= 100 and y<=100:
        return 1
    elif x<=200 and x>100 and y<=100:
        return 2
    elif x<=300 and x>200 and y<=100:
        return 3
     # snd row
    elif x <= 100 and y>=100 and y< 200:
        return 4
    elif x <= 200 and x>100 and y>=100 and y< 200:
        return 5
    elif x<=300 and x>200 and y>=100 and y< 200:
        return 6
     # third row
    elif x <= 100 and y>=200 and y< 300:
        return 7
    elif x <= 200 and x>100 and y>=200 and y< 300:
        return 8
    elif x<=300 and x>200 and y>=200 and y< 300:
        return 9
flag = 0  
X_pos = [1,5,6]
O_pos = [2,3,4]
q_table = pd.read_excel('q_table_pre-trained.xlsx',index = 'state') # change the q_table file to load that values
q_table = q_table.set_index('state')
game = TTT_game_env.TicTacToe()
font = pygame.font.Font('freesansbold.ttf', 32) 
text = font.render(game.check_win(), True, green, blue)
count=0
game.score()
while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
        	crashed = True
        
        
        if game.check_win()=="X WINS" or game.check_win()=="O WINS":
                text = font.render(game.check_win(), True, green, blue)
                count=0
               
        
        if count%2!=0:
            game.player_o(int(np.argmax(q_table.loc[TTT_game_env.state_modify(game.state)])))
            count+=1
        
        if event.type == pygame.MOUSEBUTTONDOWN and flag == 0:
        	flag = 1         
        if event.type == pygame.MOUSEBUTTONUP and flag==1:
            
            if count%2==0:
                if pixel_pos(event.pos) not in game.state:
                    game.player_x(pixel_pos(event.pos))
                else:
                    print("wrong move try again" )
                    count-=1
            text = font.render(game.check_win(), True, green, blue)
            count+=1
            if count==9:
                text = font.render("Draw", True, green, blue) 
                count=0
                game.reset()
            elif game.check_win()=="X WINS" or game.check_win()=="O WINS":
                text = font.render(game.check_win(), True, green, blue)
                count=0
                game.reset()
            flag = 0 
            
        
        
    # background --------------------------------------------------------  
    
    gameDisplay.fill(white)
    rect = pygame.Rect(98, 0, 4, 300)
    pygame.draw.rect(gameDisplay, (0,0,0),rect)
    rect = pygame.Rect(198, 0, 4, 300)
    pygame.draw.rect(gameDisplay, (0,0,0),rect)
    rect = pygame.Rect(0 , 98, 300, 4)
    pygame.draw.rect(gameDisplay, (0,0,0),rect)
    rect = pygame.Rect(0, 198, 300,4)
    pygame.draw.rect(gameDisplay, (0,0,0),rect)
    # background --------------------------------------------------------
    
    # add the X and O images-------------------------------------------- 
    for i in game.x_positions:
        gameDisplay.blit(Ximg,pos_pixel[i])
    for i in game.o_positions:
        gameDisplay.blit(Oimg,pos_pixel[i])
    gameDisplay.blit(text,pos_pixel[5])
    # add the X and O images-------------------------------------------- 

    pygame.display.update()
    clock.tick(60)
pygame.quit()


# In[ ]:




