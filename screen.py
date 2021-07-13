from tkinter import *
class Screen:
    def __init__(self,w,h):
        self.tk=Tk()
        self.canvas=Canvas(self.tk,width=w,height=h)
        self.width=w
        self.height=h
        self.canvas.pack()
        self.tk.update()

    def loop(self):
        self.tk.update()