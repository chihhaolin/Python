"""
Clone of 2048 game.
"""

import poc_2048_gui
import random


# 2048 DIM
DIM_H = 4
DIM_W = 4

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    # replace with your code
    res = move_left(line)
    res = add_to_left(res)
    return res

def move_left(line):
    """
    step 1: move item to left 
    """
    res = [0 for dummy in range(len(line))]
    index = 0
    for item in line:
        if item != 0:
            res[index] = item
            index += 1
    return res

def add_to_left(line):
    """
    step 2: add together
    """
    res = [0 for dummy in range(len(line))]
    index = 0
    index_res = 0
    while(index < (len(line)-1)):
        if line[index] == line[index+1]:            
            res[index_res] = line[index]*2            
            index += 2
        else:
            res[index_res] = line[index]
            index += 1
        index_res += 1
    
    if index < len(line):
        res[index_res] = line[-1]
            
    return res


class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        # replace with your code
        self._grid_height = grid_height
        self._grid_width = grid_width
        # call reset to create an initial grid  
        self.reset()
        self._start_cell = {UP:[(0,i) for i in range(self._grid_width)],
                           DOWN:[(self._grid_height-1,i) for i in range(self._grid_width)],
                           LEFT:[(i,0) for i in range(self._grid_height)],
                           RIGHT:[(i,self._grid_width-1) for i in range(self._grid_height)]}
        self._num_steps = {UP:self._grid_height,
                          DOWN:self._grid_height,
                          LEFT:self._grid_width,
                          RIGHT:self._grid_width}    

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self._grid = [[0 for _col in range(self._grid_width)]
                           for _row in range(self._grid_height)]
        self.new_tile()
        self.new_tile()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        # replace with your code
        return "" 

    def get_grid_height(self):
        """
        Get the height of the board.
        """        
        # replace with your code
        return self._grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        # replace with your code
        return self._grid_width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        # replace with your code
        
        #UP = 1
        #DOWN = 2
        #LEFT = 3
        #RIGHT = 4
       
        checklist = [[self._grid[row][col] for col in range(self._grid_width)]
                                          for row in range(self._grid_height)]

        
        for start_cell in self._start_cell[direction]:        	
            indices, value = self.traverse_grid(start_cell, OFFSETS[direction], self._num_steps[direction])    
            line = merge(value)
            count = 0
            for index in indices:
                self._grid[index[0]][index[1]] = line[count]
                count += 1
                
        if not checklist == self._grid:
            self.new_tile()
            


#OFFSETS = {UP: (1, 0),
#           DOWN: (-1, 0),
#           LEFT: (0, 1),
#           RIGHT: (0, -1)}
   
    def traverse_grid(self, start_cell, direction, num_steps):
        """
        Function that iterates through the cells in a grid
        in a linear direction
        Both start_cell is a tuple(row, col) denoting the
        starting cell
        direction is a tuple that contains difference between
        consecutive cells in the traversal
        """
        processing_cell = []
        processing_cell_value = []

        for step in range(num_steps):
            row = start_cell[0] + step * direction[0]
            col = start_cell[1] + step * direction[1]
            processing_cell +=  [(row, col)]
            processing_cell_value +=  [self._grid[row][col]] 
        return [processing_cell, processing_cell_value]
      
    
    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        space_detecotr = False
        for col in range(self._grid_width):
            for row in range(self._grid_height):
                if self._grid[row][col] == 0:
                    space_detecotr = True
        if not space_detecotr:
            return 
        
        flag = True        
        while flag:
            col_number = random.randrange(0, self._grid_width)
            row_number = random.randrange(0, self._grid_height)
            rand_number = random.random()
            if self._grid[row_number][col_number] == 0:
                flag = False
                if rand_number < 0.9:
                    self._grid[row_number][col_number] = 2
                else:
                    self._grid[row_number][col_number] = 4

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        # replace with your code
        return self._grid[row][col]

poc_2048_gui.run_gui(TwentyFortyEight(DIM_H, DIM_W))
