import random
import Cell_Backend
import math

# Processes the generation of a Sudoku Puzzle
# @author Dan-Alfred-John.Naungayan

class SudokuPuzzle:
    masterPuzzle = []
    puzzleRow = []
    puzzleRow_Holder = []
    # sudokuSize = 9
    rowChecker = []
    columnChecker = []
    boxChecker = []
    # availableNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    availableNumbers = []
    # populableNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    clues = 50
    cell_Backends = []
    filled_cells = []
    unfilled_cells = []
    ordered_trial_list = []
    boardSize = 0

    def __init__(self, boardSize):
        # self.newMasterPuzzle()
        # self.newMasterPuzzle2()
        self.sudokuSize = self.boardSize = boardSize

        for row in range(self.sudokuSize):
            cell_Backends_row = []
            for column in range(self.sudokuSize):
                my_cell = Cell_Backend.Cell_Backend(row, column, self.sudokuSize)
                cell_Backends_row.append( my_cell )
                self.unfilled_cells.append(my_cell)
            self.cell_Backends.append(cell_Backends_row)
        self.newMasterPuzzle3()
        self.removeClues()
        
        # puzzleCounter = 0
        # while puzzleCounter < 3000:
        #     for row in range(self.sudokuSize):
        #         cell_Backends_row = []
        #         for column in range(self.sudokuSize):
        #             my_cell = Cell_Backend.Cell_Backend(row, column, self.sudokuSize)
        #             cell_Backends_row.append( my_cell )
        #             self.unfilled_cells.append(my_cell)
        #         self.cell_Backends.append(cell_Backends_row)
        #     self.newMasterPuzzle3()
        #     self.removeClues()
        #     puzzleCounter = puzzleCounter + 1
        #     print(str(puzzleCounter) + " puzzles made")
        #     self.masterPuzzle = []
        #     self.puzzleRow = []
        #     self.puzzleRow_Holder = []
        #     # sudokuSize = 9
        #     self.rowChecker = []
        #     self.columnChecker = []
        #     self.boxChecker = []
        #     # availableNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        #     self.availableNumbers = []
        #     # populableNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        #     clues = 50
        #     self.cell_Backends = []
        #     self.filled_cells = []
        #     self.unfilled_cells = []
        #     self.ordered_trial_list = []

    def newMasterPuzzle3(self):
        self.masterPuzzle = []
        for x in range(self.boardSize):
            self.availableNumbers.append(x + 1)
        # self.availableNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        # self.populableNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        # print(self.availableNumbers)

        for row in range(self.sudokuSize):
            for column in range(self.sudokuSize):
                self.puzzleRow_Holder.append(0)
            self.puzzleRow = self.puzzleRow_Holder.copy()
            self.masterPuzzle.append(self.puzzleRow)
            self.puzzleRow_Holder.clear()
        # add recursive function
        self.populatePuzzle()

    def removeClues(self):
        cluesRemoved = 0
        while(cluesRemoved < self.clues):
            x_remove = random.randint(0, self.sudokuSize - 1)
            y_remove = random.randint(0, self.sudokuSize - 1)
            if self.masterPuzzle[x_remove][y_remove] == 0:
                continue
            else:
                self.masterPuzzle[x_remove][y_remove] = 0
                cluesRemoved = cluesRemoved + 1

    def populatePuzzle(self):
        if(len(self.unfilled_cells) == 0):
            # print("finished")
            return True

        unfilled_cells_with_least_candidates = self.get_unfilled_cells_with_least_candidates()

        # editingCell = random.choice(self.unfilled_cells)
        editingCell = random.choice( unfilled_cells_with_least_candidates )
        x_coor = editingCell.x_coor
        y_coor = editingCell.y_coor
        valid = False
        
        while editingCell.isCellFilled():
            # x_coor  = random.randint(0, self.sudokuSize - 1)
            # y_coor  = random.randint(0, self.sudokuSize - 1)
            # valid = False
            # editingCell = self.cell_Backends[x_coor][y_coor]

            editingCell = random.choice(self.unfilled_cells)
            x_coor = editingCell.x_coor
            y_coor = editingCell.y_coor
            valid = False

        editingCell.available_numbers = self.set_available_numbers(editingCell)
        successful_population = True

        while not valid:

            if editingCell.get_sizeof_available_numbers() == 0:                
                return False
            
            cell_Value = random.choice(editingCell.get_available_list())
            valid = self.validValue( cell_Value, x_coor, y_coor )
            if valid:
                # self.printPuzzle()
                # print()
                # print()
                editingCell.set_cell_Value(cell_Value )
                self.masterPuzzle[x_coor][y_coor] = cell_Value
                editingCell.isFilled = True
                self.unfilled_cells.remove(editingCell)
                self.ordered_trial_list.append(editingCell)
                valid = self.populatePuzzle()
                successful_population = valid # check if came out of retrial
            else:
                editingCell.remove_from_available_list( cell_Value )
                continue
            
            # Should and will only be accessed if all the available numbers from previous recursion have been tried
            if not successful_population:
                editingCell.set_cell_Value(0)
                editingCell.isFilled = False
                editingCell.remove_from_available_list( cell_Value )
                self.unfilled_cells.append(editingCell)
                self.ordered_trial_list.remove(editingCell)

                # Update Master puzzle list
                self.masterPuzzle[x_coor][y_coor] = 0

        return True
        
    def set_available_numbers(self, a_editing_cell):
        cell_master_available = []
        for x in range( self.boardSize ):
            if self.validValue(x+1, a_editing_cell.x_coor, a_editing_cell.y_coor):
                cell_master_available.append(x+1)
        return cell_master_available
    
    def get_count_available_numbers(self, a_editing_cell):
        cell_master_available = []
        for x in range( self.boardSize ):
            if self.validValue(x+1, a_editing_cell.x_coor, a_editing_cell.y_coor):
                cell_master_available.append(x+1)
        return len(cell_master_available)

    def get_unfilled_cells_with_least_candidates(self):
        least_count_candidates = self.boardSize
        cells_with_least_candidates = []
        for unfilled_cell in self.unfilled_cells:
            least_count_candidates = min( self.get_count_available_numbers(unfilled_cell), least_count_candidates )

        for unfilled_cell in self.unfilled_cells:
            if self.get_count_available_numbers(unfilled_cell) == least_count_candidates:
                cells_with_least_candidates.append(unfilled_cell)

        return cells_with_least_candidates


    # def newMasterPuzzle2(self):
    #     self.masterPuzzle = []
    #     self.availableNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    #     self.populableNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    #     for row in range(self.sudokuSize):
    #         for column in range(self.sudokuSize):
    #             self.puzzleRow_Holder.append(0)
    #         self.puzzleRow = self.puzzleRow_Holder.copy()
    #         self.masterPuzzle.append(self.puzzleRow)
    #         self.puzzleRow_Holder.clear()

    #     for counter in range(self.clues):
    #         row = random.choice(range(self.sudokuSize))
    #         column = random.choice(range(self.sudokuSize))
    #         while not (self.masterPuzzle[row][column] == 0):
    #             row = random.choice(range(self.sudokuSize))
    #             column = random.choice(range(self.sudokuSize))
            
    #         cellValue = random.choice(self.populableNumbers)
    #         while( not self.validValue(cellValue, row, column)):
    #             cellValue = random.choice(self.populableNumbers)
            
    #         self.masterPuzzle[row][column] = cellValue
    #         self.populableNumbers = self.populableNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # def newMasterPuzzle(self):
    #     self.masterPuzzle = []
    #     self.availableNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    #     self.populableNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    #     for row in range(self.sudokuSize):
    #         for column in range(self.sudokuSize):
    #             self.puzzleRow_Holder.append(0)
    #         self.puzzleRow = self.puzzleRow_Holder.copy()
    #         self.masterPuzzle.append(self.puzzleRow)
    #         self.puzzleRow_Holder.clear()
            
    #     for row in range(self.sudokuSize):
    #         for column in range(self.sudokuSize):
    #             self.generateMasterCellValue(row, column)

    def getMasterCellValue(self, row, column):
        return self.masterPuzzle[row][column]
    
    # def generateMasterCellValue(self, row, column):
    #     # self.printPuzzle()
    #     cellValue = random.choice(self.populableNumbers)
    #     # print(cellValue)
    #     while( not self.validValue(cellValue, row, column)):
    #         cellValue = random.choice(self.populableNumbers)

    #     # print(row, column)
    #     if ( self.masterPuzzle[row][column] == 0):
    #         self.masterPuzzle[row][column] = cellValue

    #     # if ( len(self.puzzleRow_Holder) == 9):
    #     #     self.puzzleRow = self.puzzleRow_Holder.copy()
    #     #     self.masterPuzzle.append(self.puzzleRow)
    #     #     self.puzzleRow_Holder.clear()
    #     self.populableNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    # def validValue(self, cellValue, row, column):
    #     if ( not ( (self.columnCheck(cellValue, row, column)) and (self.rowCheck(cellValue, row, column)) and (self.boxCheck(cellValue, row, column))) ):
    #         self.populableNumbers.remove(cellValue)
    #         if len(self.populableNumbers) == 0:
    #             # self.newMasterPuzzle()
    #             # self.newMasterPuzzle2()
    #             self.newMasterPuzzle3()
    #         else:
    #             return False
    #     return True

    def validValue(self, cellValue, row, column):
        if ( not ( (self.columnCheck(cellValue, row, column)) and (self.rowCheck(cellValue, row, column)) and (self.boxCheck(cellValue, row, column))) ):
            return False
        else:
            return True

    def columnCheck(self, cellValue, row, column):
        for counter in range(self.sudokuSize):
            if (cellValue == self.masterPuzzle[counter][column]):
                return False
        return True
    
    def rowCheck(self, cellValue, row, column):
        for counter in range(self.sudokuSize):
            if (cellValue == self.masterPuzzle[row][counter]):
                return False
        return True
    
    def boxCheck(self, cellValue, row, column):
        divider = int( math.sqrt(self.boardSize) )
        columnBox = column // divider
        rowBox = row // divider
        matchCounter = 0
        for rowGroup in range( (rowBox * divider ),  ((rowBox + 1) * divider ) ):
            for columnGroup in range( (columnBox * divider ),  ((columnBox + 1) * divider ) ):
                if ( (cellValue == (self.masterPuzzle[rowGroup][columnGroup]))):
                    return False
        return True

    def printPuzzle(self):
        for x in range(self.sudokuSize):
            print(self.masterPuzzle[x])
