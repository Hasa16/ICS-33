# Put your imports here
from goody import irange
from nearestneighbor import closest_2d
import random
import cProfile
import pstats    

# Put your code for profile analysis here 

def create_random(n) -> list:
    list_of_coord = []
    for _ in range(n):
        list_of_coord.append((random.random(), random.random()))
    return list_of_coord

random_list = create_random(25600)
cProfile.run('closest_2d(random_list)','test_profile')
p = pstats.Stats('test_profile')
p.strip_dirs().sort_stats('calls').print_stats(12)
p.strip_dirs().sort_stats('time').print_stats(12)