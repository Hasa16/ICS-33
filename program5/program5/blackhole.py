# A Black_Hole is derived from a Simulton base; it updates by finding+removing
#   any objects (derived from a Prey base) whose center is crosses inside its
#   radius (and returns a set of all eaten simultons); it displays as a black
#   circle with a radius of 10 (e.g., a width/height 20).
# Calling get_dimension for the width/height (for containment and displaying)'
#   will facilitate inheritance in Pulsator and Hunter

from simulton import Simulton
from prey import Prey
import random
import math

class Black_Hole(Simulton):  
    radius = 20
    
    def __init__(self, x, y):
        Simulton.__init__(self, x, y, Black_Hole.radius, Black_Hole.radius)
    
    def update(self, model):
        sett = model.find(lambda x: self.contains(x.get_location()))
        for x in sett:
            model.remove(x)
        return sett
        
    def display(self,canvas):
        canvas.create_oval(self._x-self.get_dimension()[0]      , self._y-self.get_dimension()[1],
                                self._x+self.get_dimension()[0], self._y+self.get_dimension()[1],
                                fill='black')

    def contains(self,xy):
        if self._x != xy[0] or self._y != xy[1]:
            return self.distance(xy) <= self.get_dimension()[1]
        