from tkinter import *
import Cell
import SudokuPuzzle
import math

# Class that renders the board
# Called by Sudoku_main
# @author Dan-Alfred-John.Naungayan

class Board:

    height = 500
    width = 500
    gridWidth = 1
    boardSize = sudokuColumnCount = sudokuRowCount = 9
    gridColumnCount = sudokuColumnCount - 1
    gridRowCount = sudokuRowCount - 1
    proofOfConcept = True

    # dimensions of each cell


    def __init__(self, window, canvas, proofOfConcept):
        self.window = window
        self.proofOfConcept = proofOfConcept
        self.canvas = canvas
    
    # method - initialize the GUI
    def initialize(self):
        # set window title
        self.window.title( "Python GUI" )
        # set window width and height
        self.window.geometry('500x500')
        # set window background color
        # self.window.configure( bg  = 'white' )
        self.canvas.configure( bg = 'white')
        self.generateGrid()

    def setFinalHeight(self, finalHeight):
        self.height = int(finalHeight)

    def getFinalHeight(self):
        return self.height

    def setFinalWidth(self, finalWidth):
        self.width = int(finalWidth)

    def getFinalWidth(self):
        return self.width

    def getGridColumnCount(self):
        return self.gridColumnCount
    
    def getGridRowCount(self):
        return self.gridRowCount
        
    # method - run the GUI    
    def start(self):    
        self.window.mainloop()

    # Generate Grid lines
    def generateGrid(self):
        self.populateNumbers()
        self.generateColumnGrids()
        self.generateRowGrids()
    
    # Generate Column Grid lines
    def generateColumnGrids(self):
        gridWidth = 1
        divider = int( math.sqrt(self.boardSize) )
        for column in range( self.getGridColumnCount() ):
            xCoordinate = ((self.width // self.sudokuColumnCount ) * column) + (self.width // self.sudokuColumnCount )
            if (column + 1) % divider == 0:
                gridWidth = 5
            else:
                gridWidth = 1
            self.canvas.create_line( xCoordinate, 0, xCoordinate, self.height, width = gridWidth )
        self.canvas.pack()

    # Generate Row Grid lines
    def generateRowGrids(self):
        gridWidth = 1
        divider = int( math.sqrt(self.boardSize) )
        for row in range( self.getGridColumnCount() ):
            yCoordinate = ((self.height // self.sudokuRowCount ) * row) + (self.height // self.sudokuRowCount )
            if (row + 1) % divider == 0:
                gridWidth = 5
            else:
                gridWidth = 1
            self.canvas.create_line( 0, yCoordinate, self.height, yCoordinate, width = gridWidth )
        self.canvas.pack()

    def populateNumbers(self):
        sudokuPuzzle = SudokuPuzzle.SudokuPuzzle( self.boardSize )
        for row in range(self.sudokuColumnCount):
            for column in range(self.sudokuRowCount):
                cell = Cell.Cell(sudokuPuzzle.getMasterCellValue(row, column), column, row, self.canvas, self.boardSize, self.height)
        self.canvas.pack()


