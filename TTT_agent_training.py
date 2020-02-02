
import pandas as pd
import numpy as np
import TTT_game_env 

#initialize q_table
q_table = pd.DataFrame({"state":[1],1:[0.2],2:[0.3],3:[0.5],4:[0.1],5:[0.2],6:[0.5],7:[0.6],8:[0.7],9:[0.8]})
q_table=q_table.set_index("state")




game = TTT_game_env.TicTacToe() # create a game environment

game.score() 

# parameters required for modify the q_table
discount_factor =0.95
learning_rate =0.1

episodes=0
while True:
    print("episode ",episodes)
    episodes+=1
    if episodes%100==0:  # for every 100 episode it saves the q_table
        q_table.to_excel("q_table.xlsx") 
    if episodes%10000==0: # it will train for 10000 games
        break
  
    while True:
            state = []
            _,_,done = game.env_x()  # play x moves
            game.show()
            if done:
                #if X wins in the end so we have to send the reward to its previous steps-------------->
                for i in range(len(game.state)-1):
                    s = TTT_game_env.state_modify(game.state[:-i-1])
                    try:
                        act = np.argmax(q_table.loc[s])
                    except KeyError:
                        q_table.loc[s]=np.random.uniform(0,-1,size=9)
                        act = np.argmax(q_table.loc[s])
                    new_state,reward,event = game.state[:-i],-50,True
                    new_state = TTT_game_env.state_modify(new_state)
                    q_previous = list(q_table.loc[s])[act-1]
                    #print("prev:",list(q_table.loc[s]))
                    try:
                        q_next = np.max(q_table.loc[new_state])
                    except KeyError:
                        q_table.loc[new_state]=np.random.uniform(0,-1,size=9)
                        q_next = np.max(q_table.loc[new_state])
                    #game.show()
                    new_q = (1-learning_rate)*q_previous + learning_rate * (reward +discount_factor* q_next)

                    q_table.loc[s][act] = new_q
                    #print("new q:",new_q,"prev:",list(q_table.loc[s]))
                  #------------------------------------------------------------------------------------>
                
                
                game.reset()
                break


            s = TTT_game_env.state_modify(game.state)
            # if the state 's' is not present in the table then create it then change the values thats why the try except statement is there
            try:
                act = np.argmax(q_table.loc[s])
            except KeyError:
                q_table.loc[s]=np.random.uniform(0,-1,size=9)
                act = np.argmax(q_table.loc[s]) # choose the action from q_table

            new_state,reward,event = game.env_o(int(act))
            new_state = TTT_game_env.state_modify(new_state)
            q_previous = list(q_table.loc[s])[act-1]
    
            try:
                q_next = np.max(q_table.loc[new_state])
            except KeyError:
                q_table.loc[new_state]=np.random.uniform(0,-1,size=9)
                q_next = np.max(q_table.loc[new_state])
            game.show()
            new_q = (1-learning_rate)*q_previous + learning_rate * (reward +discount_factor* q_next)
            q_table.loc[s][act] = new_q
            #print("new q:",new_q,"prev:",list(q_table.loc[s]))
            #game.check_win()
            if event:
                break

