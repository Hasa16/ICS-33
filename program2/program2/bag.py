from collections import defaultdict
from goody import type_as_str
from pickle import TRUE

class Bag:
    def __init__(self, items = None):
        self.dict = defaultdict(int)
        if items != None:
            for item in items:
                self.dict[item] += 1
    
    def __repr__(self):
        param = []
        for k,v in self.dict.items():
            for i in range(v):
                param.append(k)
        return f'Bag({param})'
        
        
    def __str__(self):
        return 'Bag(' + ','.join(f'{k}[{v}]' for k, v in self.dict.items()) + ')'
    
    def add(self, item):
        self.dict[item] += 1
        
    def unique(self):
        return len(self.dict)    
        
    def __contains__(self, object):
        return object in self.dict.keys()
    
    def count(self, item):
        if item in self.dict:
            return self.dict[item]
        else:
            return 0

    def __len__(self):
        return sum(v for v in self.dict.values())
    
    def __add__(self, object):
        new_dict = []
        if type(object) == Bag:
            for k, v in self.dict.items():
                for i in range(v):
                    new_dict.append(k)
            for k, v in object.dict.items():
                for i in range(v):
                    new_dict.append(k)
            return new_dict
        else:
            raise TypeError
    
    
    def remove(self, item):
        if item in self.dict:
            self.dict[item] -= 1
            if self.dict[item] == 0:
                del self.dict[item]
        else:
            raise ValueError
        
        for x, v in self.dict.items():
            if v == 0:
                self.dict.pop(x)
                
            
    def __eq__(self, object):
        if type(object) == Bag:
            return self.dict == object.dict
        else:
            return False
    
    def _gen(self):
        for k, v in self.items():
            for i in range(v):
                yield k  
                
    def __iter__(self):
        return Bag._gen(dict(self.dict.items()))
        
        
        
if __name__ == '__main__':
    #driver tests
    import driver
    driver.default_file_name = 'bsc21S22.txt'
#     driver.default_show_exception= True
#     driver.default_show_exception_message= True
#     driver.default_show_traceback= True
    driver.driver()
