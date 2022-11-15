from helpers import primes, hide, nth
from builtins import RuntimeError



def differences(iterable1,iterable2):
    it1 = iter(iterable1)
    it2 = iter(iterable2)
    for i, t in enumerate(zip(it1, it2), start=1):
        if t[0] != t[1]:
            yield (i, t[0], t[1])
    
            
   
def once_in_a_row(iterable):
    last_value = ''
    for x in iterable:
        if x == last_value:
            continue
        else:
            yield x
        last_value = x


def in_between(iterable, starter, stopper):
    start = False
    stopp = False
    for value in iterable:
        if starter(value):
            start = False
            stopp = False
        if start and not stopp:
            yield value
        elif not start:
            if starter(value):
                start = True
                yield value
        if start and not stopp:
            if stopper(value):
                stopp = True


def pick(iterable, n):
    itera = iter(iterable)
    list1 = []
    count = 0
    while True:
        count += 1
        item = next(itera, 'empty')
        if item == 'empty':
            break
        if count <= n:
            list1.append(item)
        if len(list1) == n:
            yield [*list1]
            list1.clear()
            count -= 4


def slice_gen(iterable, start, stop, step):
    itera = iter(iterable)
    if start < 0 or stop < 0 or step <= 0:
        raise AssertionError
    count = -1
    next_item = start
    while True:
        count += 1
        try:
            item = next(itera)
            if count == stop:
                break
            elif count == next_item:
                next_item = next_item + step
                yield item
        except:
            return



 
def alternate_all(*args):
    itera = [iter(arg) for arg in args]
    while itera != []:
        temp = []
        for i in itera:
            try:
                yield next(i)
                temp.append(i)
            except StopIteration:
                pass
            itera = temp
        
        



class ListSI:
    def __init__(self,initial):
        self._real_list  = list(initial)
        self._list_count = len(initial)
        self._iter_count = 0
    
    def __repr__(self):
        return repr(self._real_list)
    
    def __len__(self):
        return len(self._real_list)
    
    def append(self,value):
        self._real_list.append(value)
            
    def __getitem__(self,index):
        return self._real_list[index]
            
    def __setitem__(self,index, value):
        self._real_list[index] = value
            
    def __delitem__(self,index):
        self._real_list.pop(index)
            
    def __iter__(self):
        class ListSI_iter:
            def __init__(self,aListSI):
                self.original_size = aListSI._list_count
                self._list = aListSI
                self._counter = 0
                
            def __next__(self):
                if len(self._list) != self.original_size:
                    raise RuntimeError
                if self._counter < len(self._list._real_list):
                    result = self._list._real_list[self._counter]
                    self._counter +=1
                    return result
                raise StopIteration
             
            def __iter__(self):
                return self
             
        return ListSI_iter(self)


def fool_it():
    l = ListSI(['a','b', 'c'])
    for i in l:
        l.append('z')
        if len(l) > 4:
            break
    l.append('z')  # so that this statement incorrectly raises a RuntimeError exception    


if __name__ == '__main__':
    
    import driver
    driver.default_file_name = 'bscq4S22.txt'
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
    
    
