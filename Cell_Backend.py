# Class for each sudoku cell to be processed
# Holds information incluing:
#   coordinates
#   isFilled or not
#   available numbers if not yet filled

class Cell_Backend:
    x_coor = 0
    y_coor = 0
    board_size = 0
    # available_numbers = []
    cell_Value = 0
    # ordered_trial_list = []

    def __init__(self, x_coor, y_coor, board_size):
        self.x_coor = x_coor
        self.y_coor = y_coor
        self.board_size = board_size
        self.available_numbers = []
        for x in range(self.board_size):
            self.available_numbers.append(x+1)
        self.ordered_trial_list = []
        self.isFilled = False

    def setIsCellFilled(self, aIsCellFilled):
        self.isFilled = aIsCellFilled
    
    def isCellFilled(self):
        return self.isFilled
    
    def get_x_coor(self):
        return self.x_coor
    
    def get_y_coor(self):
        return self.y_coor
    
    def set_cell_Value(self, cell_Value):
        self.cell_Value = cell_Value

    def get_cell_Value(self):
        return self.cell_Value

    def get_sizeof_available_numbers(self):
        return len(self.get_available_list())
    
    def remove_from_available_list(self, removeCandidate):
        self.get_available_list().remove(removeCandidate)

    def add_from_available_list(self, addCandidate):
        self.get_available_list().add(addCandidate)

    def get_available_list(self):
        return self.available_numbers
    
    def get_ordered_trial_list(self):
        return self.ordered_trial_list
    
    def append_to_ordered_trial_list(self, a_Trial):
        self.get_ordered_trial_list().append(a_Trial)
        self.remove_from_available_list(a_Trial) # add check if it is in here

    def remove_from_trial_list(self, a_Trial):
        self.get_ordered_trial_list().pop(-1)