# Put your imports here
from goody import irange
from nearestneighbor import closest_2d
from performance import Performance
import random

# Put your code for performance analysis here 

list_of_coord = []
def create_random(n) -> list:
    global list_of_coord
    for _ in range(n):
        list_of_coord.append((random.random(), random.random()))
    return list_of_coord


for i in irange(0,8):
    size = 100 * 2**i
    try:
        p = Performance(lambda: closest_2d(list_of_coord), lambda: create_random(size),5,'\nNearest Neighbor, size = {}'.format(size))
        p.evaluate()
        p.analyze()
    except:
        print('Error, 0 time-elapsed; cannot show analysis')

        