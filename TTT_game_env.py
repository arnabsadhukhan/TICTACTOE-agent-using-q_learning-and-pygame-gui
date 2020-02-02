import pandas as pd
import numpy as np
class TicTacToe:
    def score(self):
        self.x_wins=0
        self.o_wins=0
    def __init__(self):
        self.loc_tuple = {1:(0,0),2:(0,1),3:(0,2),4:(1,0),5:(1,1),6:(1,2),7:(2,0),8:(2,1),9:(2,2)}
        self.state=[]
        self.positions = np.arange(1,10)
        self.d= [0,1,2]
        self.dT =list(reversed(self.d))
        self.board = np.zeros((3,3),dtype=np.str)
        self.x_positions=np.array([])
        self.o_positions=np.array([])
        
    def player_x(self,action):
        if action not in self.o_positions and action not in self.x_positions:
            self.board[self.loc_tuple[action]] = "X"
            self.x_positions = np.append(self.x_positions,action)
            self.positions=np.delete(self.positions,np.where(self.positions==action)[0][0])
            self.state.append(action)
            return 1
        else:
            return 0
        
    def player_o(self,action):
        if action not in self.x_positions and action not in self.o_positions:
            self.o_positions = np.append(self.o_positions,action)
            self.board[self.loc_tuple[action]] = "O"
            self.positions=np.delete(self.positions,np.where(self.positions==action)[0][0])
            self.state.append(action)
            return 1
        else:
            return 0
        
    def show(self):
        print(self.board)

    def possible_positions(self):
          return list(set(self.positions) - set(self.x_positions) - set(self.o_positions))
        
    def check_win(self):
        if sum(self.board[0]=='X')==3 or sum(self.board[1]=='X')==3 or sum(self.board[2]=='X')==3 or sum(self.board[:,0]=='X')==3 or sum(self.board[:,1]=='X')==3 or sum(self.board[:,2]=='X')==3:
            self.x_wins+=1
            return "X WINS"
        elif sum(self.board[self.d,self.d]=='X')==3 or sum(self.board[self.d,self.dT]=='X')==3:
            self.x_wins+=1
            return "X WINS"
        elif sum(self.board[0]=='O')==3 or sum(self.board[1]=='O')==3 or sum(self.board[2]=='O')==3 or sum(self.board[:,0]=='O')==3 or sum(self.board[:,1]=='O')==3 or sum(self.board[:,2]=='O')==3:
            self.o_wins+=1
            return "O WINS"
        elif sum(self.board[self.d,self.d]=='O')==3 or sum(self.board[self.d,self.dT]=='O')==3:
            self.o_wins+=1
            return "O WINS"
    def nextmove(self,action):
        finish = self.player_o(action)
        if finish ==1:
            return
        else:
            print("try again wrong move")
            nextmove()
    def env_x(self):
        s = np.random.choice(self.possible_positions())
        finish = self.player_x(s)
        self.state.append(s)
        if self.check_win()=="X WINS" :
            print(self.check_win())
          #self.reset()
            return self.state,-50,True
        if len(self.state)==9:
            self.temp = self.state
            self.reset()
            return self.temp,-30,True
        else:
            return self.state,0,False
        
    def env_o(self,action):
        if self.check_win()=="O WINS" :
            print(self.check_win())
            self.temp = self.state 
            self.reset()
            return self.temp,100,True
        finish = self.player_o(action)
        if finish==0:
            self.temp=self.state
            self.reset()
            return self.temp,-50,False
        else:
            self.state.append(action)
            if self.check_win()=="O WINS" :
                print(self.check_win())
                self.temp = self.state 
                self.reset()
                return self.temp,10,True
            if len(self.state)==9:
                self.temp = self.state
                self.reset()
                return self.temp,-30,True
            return self.state,-1,False
        
        if len(self.state)==9:
            self.temp = self.state
            self.reset()
            return self.temp,-3,True
    def reset(self):
        self.__init__()

def state_modify(data):
    data = np.array(data)
    if len(data)>0:
        n = len(data)
        x = data[np.arange(0,n,2)]
        o = data[np.arange(1,n,2)]
        x = np.sort(x)
        o = np.sort(o)
        x,o
        data =[]
        j=0
        k=0
        for i in range(n):
            if i%2==0:
                data.append(x[j])
                j+=1
            else:
                data.append(o[k])
                k+=1
        s=data[0]
        for i in range(len(data)-1):
              s = s*10+data[i+1]
        return s
    else: 
        return 0