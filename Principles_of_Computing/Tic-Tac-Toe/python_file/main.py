"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 200         # Number of trials to run
SCORE_CURRENT = 1.0 # Score for squares played by the current player
SCORE_OTHER = 1.0   # Score for squares played by the other player
    
# Add your functions here.

# main function
def mc_trial(board, player):
    '''mc_trial'''
    lst = board.get_empty_squares()
    random.shuffle(lst)
    
    for ele in lst:
        board.move(ele[0],ele[1],player)
        player = provided.switch_player(player)
        if board.check_win():
            break  
    #print board        
    #return player

def mc_update_scores(scores, board, player):
    '''mc_update_scores'''    
    win_status = board.check_win()
    dim = board.get_dim()
    if win_status == provided.DRAW:
        pass
    else:
        for row in range(0, dim):
            for col in range(0, dim):
                if win_status == player:
                    if board.square(row,col) == player:
                        scores[row][col] += SCORE_CURRENT
                    elif board.square(row,col) == provided.switch_player(player): 
                        scores[row][col] -= SCORE_OTHER
                elif win_status == provided.switch_player(player):
                    if board.square(row,col) == player:
                        scores[row][col] -= SCORE_CURRENT
                    elif board.square(row,col) == provided.switch_player(player):  
                        scores[row][col] += SCORE_OTHER                    
                            
def get_best_move(board, scores):
    '''get_best_move'''     
    empty = board.get_empty_squares()
    if empty:
        random.shuffle(empty)
        max_value = -100
        for ele in empty:
            if scores[ele[0]][ele[1]] > max_value:
                max_value = scores[ele[0]][ele[1]]
                max_index = (ele[0],ele[1])
        print empty        
        return max_index
    else:
        print "err, no empty space"

def mc_move(board, player, trials):
    '''mc_move'''     
    scores = [[0 for _col in range(board.get_dim())] 
              for _row in range(board.get_dim())]
    
    for dummy in range(trials):
        clone = board.clone()
        mc_trial(clone, player)
        mc_update_scores(scores, clone, player)
        
    return get_best_move(board, scores)

     

# Test game with the console or the GUI.  Uncomment whichever 
# you prefer.  Both should be commented out when you submit 
# for testing to save time.

provided.play_game(mc_move, NTRIALS, False)        
poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)
