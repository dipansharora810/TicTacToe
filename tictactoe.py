#!/usr/bin/env python
# coding: utf-8

# In[1]:


from random import randint


# In[2]:


turn = "X"  


# In[3]:


Board = [".",".",".",".",".",".",".",".","."]


# In[4]:


new_game_board = [".",".",".",".",".",".",".",".","."]


# In[5]:


legal_moves = [1,2,3,4,5,6,7,8,9]


# In[6]:


def display_board(board):
    print(board[0],board[1],board[2],"        ","1","2","3")
    print(board[3],board[4],board[5],"        ","4","5","6")
    print(board[6],board[7],board[8],"        ","7","8","9\n")


# In[7]:


#functin to switch the player

def switch_turn(var):
    if(var== "X"):
        return "0"
    else:
        return "X"


# In[8]:


def user_turn():
    global turn
    global legal_moves
    
    #check if it's computer turn  and call ai_turn() if it's computer turn
    if(turn=="X"):
        ai_turn()
        turn = switch_turn(turn)
        return
   
    user_input = input("Choose a place from 1 - 9 : ")
    print("\n")
    
    #check if input is between 1 to 9
    while user_input not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        print("Please Enter A Valid Input\n")
        user_turn()
        return
      
    
    user_input = int(user_input)
    
    #check if the user is trying to select already taken place
    if(Board[user_input-1] != "."):
        print("Place already taken, Choose a valid place.")
        user_turn()
        return

    
    legal_moves.remove(user_input)
    Board[user_input-1] = turn
    turn = switch_turn(turn)
   


# In[9]:


# this is the function called when it's computer turn and this function call random_playout to do random playouts and 
def ai_turn():
    global Board
    global legal_moves
    global turn
    
    num_legal_moves = len(legal_moves)
    
    #these are to keep track of random playouts wins,loss and ties
    wins = []
    loss = []
    ties = []
    
    temp_turn = "X"   #this is AI
    
    #this for loop makes all possible next legal move one by one
    for i in range(num_legal_moves):
        
        temp_board = Board.copy()
        temp_legal_moves = legal_moves.copy()
        
        temp_board[legal_moves[i]-1] = "X"
        temp_turn = switch_turn(temp_turn)       #switch turn in our simulation
        temp_legal_moves.remove(legal_moves[i])
                
        wins.append(0)
        loss.append(0)
        ties.append(0)
        
        #this loop is for random playouts for each possible legal move, i am doing it 2000 random playouts
        for j in range(2000):
            
            board_reset = temp_board.copy()
            moves_reset = temp_legal_moves.copy()
            turn_reset = temp_turn
            
            
            result = random_playout(board_reset,moves_reset,turn_reset)   
            
            if(result == "WIN"):
                wins[i]+=1
            elif(result== "LOSS"):
                loss[i]+=1
            elif(result == "TIE"):
                ties[i]+=1

    min_loss_index = loss.index(min(loss))      
    Board[legal_moves[min_loss_index]-1] = turn        #computer put "X" in which it gets minimum losses from random playouts
    legal_moves.remove(legal_moves[min_loss_index])
    
    

    


# In[10]:


# This function does random playouts 
def random_playout(this_board,moves_left,my_turn):
    
    length = len(moves_left)

    temp = length
    for i in range(length):
        
        rand = randint(0,temp-1)
        this_board[moves_left[rand]-1] = my_turn
        moves_left.pop(rand)
        temp= temp-1
        
        res = check_if_over(this_board)
        my_turn = switch_turn(my_turn)
        
        if(res == "X"):
            return "WIN"
            
        elif(res == "0"):
            return "LOSS"
            
        elif(res == "TIE"):
            return "TIE"
            


# In[11]:


def check_rows(board):
    if(board[0]==board[1]==board[2] and board[0]!="."):
        return board[0]
    elif(board[3]==board[4]==board[5] and board[3]!="."):
        return board[3]
    elif(board[6]==board[7]==board[8] and board[6]!="."):
        return board[6]
    else:
        return -1


# In[12]:


def check_columns(board):
    if(board[0]==board[3]==board[6] and board[0]!="."):
        return board[0]
    elif(board[1]==board[4]==board[7] and board[1]!="."):
        return board[1]
    elif(board[2]==board[5]==board[8] and board[2]!="."):
        return board[2]
    else:
        return -1


# In[13]:


def check_diagonals(board):
    if(board[0]==board[4]==board[8] and board[0]!="."):
        return board[0]
    elif(board[2]==board[4]==board[6] and board[2]!="."):
        return board[2]
    else:
        return -1


# In[14]:


def check_tie(board):
    if("."in board):
        return -1
    else:
        return "TIE"
    


# In[15]:


# returns "X" or "0" winner or "TIE" or -1 if still running
def check_if_over(board):
  
    if(check_rows(board)!= -1):
        return check_rows(board)
    
    elif(check_columns(board)!= -1):
        return check_columns(board)
    
    elif(check_diagonals(board)!= -1):
        return check_diagonals(board)
    
    elif(check_tie(board)!= -1):
        return check_tie(board)
    
    else:
        return -1


# In[16]:


def play_game():
   
    global new_game_board
    global Board
    global legal_moves
    global turn
    
    #initialize a new game
    Board = new_game_board.copy()
    legal_moves = [1,2,3,4,5,6,7,8,9]
    
    
    print("Instructions : You are playing as 0 and Computer is X \n"  )

    
    while 1:
        display_board(Board)
        user_turn()
        check_if_over(Board)
        if(check_if_over(Board)!= -1):
            display_board(Board)
            if(check_if_over(Board)== "TIE"):
                print("It's a tie")
                break
            elif(check_if_over(Board)== "X"):
                print("AI WON")
                break
            else:
                print("Congrats!! YOU WON")
                break


# In[17]:


if __name__ == '__main__':
      play_game()


# In[ ]:





# In[ ]:




