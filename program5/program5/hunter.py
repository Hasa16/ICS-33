# A Hunter class is derived from a Pulsator and then Mobile_Simulton base.
#   It inherits updating+displaying from Pusator/Mobile_Simulton: it pursues
#   any close prey, or moves in a straight line (see Mobile_Simultion).


from prey  import Prey
from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from math import atan2
from math import pi
import random


class Hunter(Pulsator, Mobile_Simulton):  
    hunting_distance = 200
    def __init__(self, x, y):
        Mobile_Simulton.__init__(self, x, y, 10, 10, 2*pi*random.random(), 5)
        Pulsator.__init__(self, x, y)
        
    def update(self, model):
        Pulsator.update(self, model)
        Mobile_Simulton.move(self)
        Mobile_Simulton.wall_bounce(self)
        x = model.find(lambda x: isinstance(x, Prey) and x.distance(self.get_location()) < Hunter.hunting_distance)
        if len(x) != 0:
            closest = min(x, key=lambda x: x.distance(self.get_location()))
            self.set_angle(atan2(closest.get_location()[1] - self.get_location()[1], closest.get_location()[0] - self.get_location()[0]))
