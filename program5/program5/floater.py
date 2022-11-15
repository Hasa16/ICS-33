# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage 


#from PIL.ImageTk import PhotoImage
from prey import Prey
from random import random
import math


class Floater(Prey): 
    radius = 5
    
    def __init__(self, x, y):
        Prey.__init__(self, x, y, Floater.radius*2, Floater.radius*2, 2*math.pi*random(), 5)
    
    def update(self, _):
        if random() <= .3:
            x = random() - .5
            self._angle += x
            if self._speed - x > 3.0 and self._speed + x < 7:
                self._speed += x
            
        Prey.move(self)
        Prey.wall_bounce(self)
        
    def display(self,canvas):
        canvas.create_oval(self._x-Floater.radius*2      , self._y-Floater.radius*2,
                                self._x+Floater.radius*2, self._y+Floater.radius*2,
                                fill='red')
