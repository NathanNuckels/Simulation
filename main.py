from tkinter import *
import screen
import rooms

game = screen.Screen(1680,720)
cell = rooms.Cell(game,0,0)
while 1:
    game.loop()
