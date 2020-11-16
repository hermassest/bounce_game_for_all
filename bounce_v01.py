# Import important modules
import random
from tkinter import *
from time import sleep

# Build program envirnoment
env = Tk()
env.title("Bounce Game - Rayyan")
env.resizable(0, 0)
env.wm_attributes("-topmost", 1)

# Create and prepare our canvas
canvas = Canvas(env, width=800, height=600, bd=0, highlightthickness=0)
canvas.pack()
env.update()

# Create the ball and its functions using Class
class Ball:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 30, 30, fill=color)
        self.canvas.move(self.id, 393, 20)

    def draw(self):
        pass

ball = Ball(canvas, "red")

# Build the main loop of our program
while 1:
    env.update_idletasks()
    env.update()
    sleep(0.01)
        


