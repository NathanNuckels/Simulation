from tkinter import *
import PIL
import PIL.ImageTk
import PIL.Image

class Cell:
    def __init__(self, window, x, y):
        self.screen = window
        self.x = x
        self.y = y
        self.image=PIL.ImageTk.PhotoImage(PIL.Image.open("images/rooms/cell.png"))
        self.screen.canvas.create_image(self.x,self.y,anchor=NW,image=self.image)
