from predicate import is_prime
from turtledemo.forest import doit1
from builtins import RuntimeError

def hide(iterable):
    for v in iterable:
        yield v


def primes(max=None):
    p = 2
    while max == None or p <= max:
        if is_prime(p):
            yield p
        p += 1

def differences(iterable1,iterable2):
    it1 = iter(iterable1)
    it2 = iter(iterable2)
    for i, t in enumerate(zip(it1, it2), start=1):
        if t[0] != t[1]:
            yield (i, t[0], t[1])

print([d for d in differences(primes(), hide([2, 3, 1, 7, 11, 1, 17, 19, 1, 29]))])
print([d for d in differences('3.14159265', '3x14129285')])
print([d for d in differences(hide('3.14159265'), hide('3x14129285'))])

if __name__ == '__main__':
    '''import driver
    driver.default_file_name = '123.txt'
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()'''
 
