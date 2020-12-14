# Python Project: Tic-Tac-Toe by Zain Kazi


#%% Import packages
import pandas as pd
import numpy as np

#%% Create empty board
emptycol = ["","",""]
initialFrame = {"A" : emptycol,
                "B" : emptycol,
                "C" : emptycol}
boardFrame = pd.DataFrame(initialFrame); boardFrame.index = boardFrame.index + 1
print(boardFrame)

#%% Define invalid inputs
choices = ["A1","A2","A3","B1","B2","B3","C1","C2","C3"]
taken = []
result = False
def validity(pos1):
   while (pos1 in choices) == False or (pos1 in taken):
       pos1 = input("Invalid Option, Enter Different Position: ").upper()
   pos2 = pos1
   return pos2

#%% Determine if match is over
def outcome(df):
   result = False
   d1 = board.iloc[0,0] + board.iloc[1,1] + board.iloc[2,2]
   d2 = board.iloc[0,2] + board.iloc[1,1] + board.iloc[2,0]
   bvalues = board.sum(axis=0).append(board.sum(axis=1)).values
   bvalues = np.append(bvalues,d1)
   bvalues = np.append(bvalues,d2)
   if "XXX" in bvalues:
       result = True
       print("Player 1 wins. Player 2 loses.")
   elif "OOO" in bvalues: 
       result = True
       print("Player 2 wins. Player 1 loses.")
   elif i == 9:
       result = True
       print("Tied game.")
   return result

#%% Loop through game
result = True
board = boardFrame
for i in range(1,10):
    if i % 2 == 1:
        pos = input("For Player 1, Enter Position for X: ").upper()
        pos2 = validity(pos)
        board.loc[int(pos2[1]),pos2[0]] = "X"
        print(board)
    if i % 2 == 0:
        pos = input("For Player 2, Enter Position for O: ").upper()
        pos2 = validity(pos)
        board.loc[int(pos2[1]),pos2[0]] = "O"
        print(board)
    taken.append(pos2)
    if outcome(board) == True:
        break