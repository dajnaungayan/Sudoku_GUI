from tkinter import *
import tkinter.font as font
import tkinter as tk


# Class that renders the cell
# Used by the Board class
# @author Dan-Alfred-John.Naungayan

class Cell:

    fontSize = 20
    cellHeight = 0
    cellWidth = 0
    xCoor = 0
    yCoor = 0
    xPixel = 0
    yPixel = 0
    dimension = 0
    windowSize = 0

    def __init__(self, number, xCoor, yCoor, canvas, boardSize, windowSize):
        self.number = number
        self.xCoor = xCoor
        self.yCoor = yCoor
        self.canvas = canvas
        self.dimension = windowSize/boardSize
        # self.fontSize = int(20*boardSize/9)
        # self.fontSize = int ( 180/500 * boardSize / boardSize )
        self.initialize()
        self.draw()

    def initialize(self):
        self.computeXCoor(self.xCoor)
        self.computeYCoor(self.yCoor)

    def draw(self):
        if not (self.number == 0):
            self.canvas.create_text(self.xPixel, self.yPixel, text = str(self.number), font= ('Helvetica', str(self.fontSize), 'bold'))
        else:
            e1 = Entry(self.canvas, fg="blue")
            e1.config({"background": "White"})
            e1.config({"font": "Helvetica " + str(self.fontSize) + " bold"})
            e1.config(borderwidth = 0)
            e1.pack(padx=0, pady=0)
            self.canvas.create_window(self.xPixel, self.yPixel, window = e1, height = (self.dimension - (self.dimension/3)), width = (self.dimension - (4*(self.dimension/7))))

    def computeXCoor(self, aXCoor):
        self.xPixel = (self.dimension * aXCoor) + self.dimension/2

    def computeYCoor(self, aYCoor):
        self.yPixel = (self.dimension * aYCoor) + self.dimension/2


    