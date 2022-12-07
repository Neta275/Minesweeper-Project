# -*- coding: utf-8 -*-
"""
Student :Netanel Azoviv
Id : 313152209
Assignment no.6
Program : minesweeper.py
 
"""
import random
import re

class Board:
    def __init__(self,dim_size,num_bombs):
        self.dim_size=dim_size
        self.num_bombs=num_bombs
        
        self.board=self.make_new_borad()
        self.assign_values_to_board()
        #intialize a set to track of which location we have uncovered
        # we will save (row,col) tupels into this set
        self.dug=set() # if we dig at 0,0 then self.dug= {(0,0)}
        
    def __str__(self):
        #return a string that shows the board to the player
        visible_board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if (row,col) in self.dug:
                    visible_board[row][col] = str(self.board[row][col])
                else:
                    visible_board[row][col] = ' '
                string_rep=''
        #get max colum widths for printing
        widths=[]
        for idx in range(self.dim_size):
            columns = map(lambda x: x[idx],visible_board)
            widths.append(
                len(
                    max(columns, key = len)
                    
                )
            )
        indices = [i for i in range(self.dim_size)]
        indices_row= "   "
        cells=[]
        for idx, col in enumerate(indices):
            format = '%-' + str(widths[idx]) + "s"
            cells.append(format % (col))
        indices_row += "  ".join(cells)
        indices_row += '  \n'
        
        for i in range(len(visible_board)):
            row = visible_board[i]
            string_rep += f'{i} |'
            cells = []
            for idx,col in enumerate(row):
                format = '%-' + str(widths[idx]) + "s"
                cells.append(format % (col))
            string_rep += ' |'.join(cells)
            string_rep += ' |\n'
        str_len = int(len(string_rep) / self.dim_size)
        string_rep = indices_row + '-'*str_len + '\n' + string_rep + '-'*str_len
        
        return string_rep
    def make_new_borad(self):
        #construcrt a new board based on the diz sise and num bobms
        #generate an new board
        
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        
        #plant the bombs
        bombs_planted=0
        while bombs_planted < self.num_bombs:
            loc=random.randint(0,self.dim_size**2 -1)
            row = loc // self.dim_size
            col = loc % self.dim_size
            if board[row][col] == '*':
                #this means we planted a bomb there already
                continue
            board[row][col] = '*' #plant the bomb
            bombs_planted += 1
        return board
            
    def assign_values_to_board(self):
        #represent how many neighbor bobms there are
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[r][c] == '*':
                    # if this is already a bomb we dont wanna calculate anything
                    continue
                self.board[r][c] = self.get_num_neighbor_bombs(r,c)
    
    def get_num_neighbor_bombs(self,row,col):   
        # iterate through each of the neighbors position and sum number of bumbs
        num_neighbors_boms = 0
        for r in range(max(0,row-1),min(self.dim_size-1,row+1)+1):
            for c in range(max(0,col-1),min(self.dim_size-1,col+1)+1):
                if r == row and c == col:
                    #our original location
                    continue
                if self.board[r][c] == '*':
                    num_neighbors_boms +=1
                    
        return num_neighbors_boms
    
    def dig(self,row,col):
        #dig at that location
        #return True if succesfull dig ,return False if bomb dug
        #there are few options
        #hit a bomb =game over
        #dig at location with neighbor bobms = finish dig
        #dig at locations with no neighbor bombs = recursively dig neighbors
        self.dug.add((row,col)) #to keep track that we dug here
        
        if self.board[row][col] == '*':
            return False
        elif self.board[row][col] > 0:
            return True 
        #self.board[r][c]==0
        for r in range(max(0,row-1),min(self.dim_size-1,row+1)+1):
            for c in range(max(0,col-1),min(self.dim_size-1,col+1)+1):
                if (r,c) in self.dug:
                    continue # dont dig where you have already dug
                self.dig(r,c)
        return True
    
def play(dim_size=9,num_bombs=16):
    board = Board(dim_size,num_bombs)
    safe = True
    while len(board.dug) < board.dim_size ** 2 - num_bombs:
        print(board)
        user_input = re.split(',(\\s)*',input("where would you like to dig? input as row,col: "))
        row,col =int(user_input[0]),int(user_input[-1])
        if row < 0 or row >=board.dim_size or col <0 or col >= dim_size:
            print("invalid location")
            continue
        #if its valid,we dig 
        safe = board.dig(row,col)
        if not safe:#we dig a bomb
            break #game over
    if safe:
        print("congatulations you won !!!!")
    else:
        print("sorry game over")
        #then we need to reveal the whole board 
        board.dug = [(r,c) for r in range(board.dim_size) for c in range(board.dim_size)]
        print(board)
if __name__ == '__main__':
    play()
            
        