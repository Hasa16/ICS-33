# A Ball is Prey; it updates by moving in a straight
#   line and displays as blue circle with a radius
#   of 5 (width/height 10). 


from prey import Prey
import math, random


class Ball(Prey): 
    radius = 5
    
    def __init__(self, x, y):
        Prey.__init__(self, x, y, Ball.radius*2, Ball.radius*2, 2*math.pi*random.random(), 5)
    
    def update(self, _):
        Prey.move(self)
        Prey.wall_bounce(self)
        
    def display(self,canvas):
        canvas.create_oval(self._x-Ball.radius*2      , self._y-Ball.radius*2,
                                self._x+Ball.radius*2, self._y+Ball.radius*2,
                                fill='blue')