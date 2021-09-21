"""
print("Welcome to Coding Club")
"""
#Firstly, we need to install our dependencies
import numpy as np #Used for the grid
import pygame #Used for graphics

x_length = 25
y_length = 25

grid =[["[ ]"]*x_length]*y_length
grid = np.array(grid)

"""
KEY
---

Starting Position (sp) - /
Current Position (cp) - *
Blocked Position (bp) - +
Finish Position (fp) - =

"""
#Starting Position
sp = {
    "x": 0,
    "y": 0
}
#Finishing position
fp = {
    "x": x_length - 1,
    "y": y_length - 1
}
#Current Position
cp = {
    "x": sp["x"],
    "y": sp["y"]
}
#Blocked positions
bp = []

#Initial positions
path = [[cp["x"],cp["y"]]]
direct = []
direct_checked = []
checked = []
weights = []
possible = True
