from tkinter import *
import Board
import pyautogui
from PIL import Image
from pyscreenshot import grab
  
#declare the window
window = Tk()
canvas = Canvas( width = 500, height = 500)

board = Board.Board(window, canvas, True)
board.initialize()
board.start()

# my_screenshot = pyautogui.screenshot()
# screenshot_path = r'C:\Users\Daj\Desktop\sudokuPuzzlePNG.png'
# my_screenshot.save(screenshot_path)

# image_1 = Image.open(screenshot_path)
# im_1 = image_1.convert('RGB')
# pdf_path = r'C:\Users\Daj\Desktop\sudokuPuzzlePDF.pdf'
# im_1.save(pdf_path)

# print(str(canvas.canvasx))