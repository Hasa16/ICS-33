# A special is a Pulsator but reversed; it updates as a Black_Hole
#   does, but also by growing/shrinking depending on
#   whether or not it eats Prey (and removing itself from
#   the simulation if its dimension becomes 0), and displays
#   as a Black_Hole but with varying dimensions 


from blackhole import Black_Hole
import random, math


class rev_Pulsator(Black_Hole): 
    counter_max = 30
    def __init__(self, x, y):
        Black_Hole.__init__(self, x, y)
        self.set_dimension(10, 10)
        self._counter = 0
        
    def update(self, model):
        self._counter += 1
        if self._counter >= rev_Pulsator.counter_max:
            self.change_dimension(1, 1)
            self._counter = 0
        if self.get_dimension() <= (0,0):
            model.remove(self)
    
        container_set = Black_Hole.update(self, model)
        for _ in container_set:
            self.change_dimension(-1,-1)
            
        
