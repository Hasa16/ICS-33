from goody import type_as_str  # Useful for some exceptions
from pickle import FALSE

class DictList:
    def __init__(self, *args):
        assert len(args) != 0, 'DictList.__init__:  parameter is empty'
        self.dl = []
        for x in args:
            assert x != None, 'DictList.__init__:  parameter is empty'
            assert x != {}, 'DictList.__init__: ' + str(x) + ' is not a dictionary'
            assert type(x) == dict, 'DictList.__init__:  ' + str(x) +'   is not a dictionary'
            self.dl.append(x)
    
    def __len__(self):
        final = []
        for x in self.dl:
            for k in x.keys():
                final.append(k)
        return len(set(final))

    def __bool__(self):
        return len(self.dl) != 1

    def __repr__(self):
        return 'DictList(' + ', '.join(str(x) for x in self.dl) + ')'
    
    def __contains__(self, item):
        return any(item in v for v in [x.keys() for x in self.dl])
        
    def __getitem__(self, item):
        for x in self.dl[::-1]:
            if item in x:
                return x[item]
        else:
            raise KeyError
                
    def __setitem__(self, item, value):
        for x in self.dl[::-1]:
            if item in x:
                x[item] = value
                break
        else:
            self.dl.append({item: value})
    
    def __delitem__(self, item):
        for x in self.dl[::-1]:
            if item in x:
                del x[item]
                break
        else:
            raise KeyError
    
    def __call__(self, item):
        final = {}
        for i, x in enumerate(self.dl):
            if item in x:
                final[i] = x[item]
        return [(k, v) for k, v in final.items()]
        
    def _gen(self):
        for x in self:
            yield x
    
    def __iter__(self):
        list1 = []
        for x in self.dl[::-1]:
            list2 = []
            for k in x.keys():
                if k not in list1:
                    list2.append(k)
            list1+=sorted(list2)
        return DictList._gen(list1)
    
    def items(self):
        dict1 = {}
        for x in self.__iter__():
            dict1[x] = self.__getitem__(x)
        return DictList._gen([(k, v) for k, v in dict1.items()])        
        
    def collapse(self):
        dict1 = {}
        for x in self.__iter__():
            dict1[x] = self.__getitem__(x)
        return dict1  
    
    def __eq__(self, item):
        new_dict = {}
        for x in self.dl[::-1]:
            for k, v in x.items():
                if k not in new_dict:
                    new_dict[k] = v
        new_dict2 = {}     
        if type(item) == dict:
            return new_dict == item
        elif type(item) == DictList:
            for x in item.dl[::-1]:
                for k, v in x.items():
                    if k not in new_dict2:
                        new_dict2[k] = v
                    
            return new_dict == new_dict2
        else:
            raise TypeError
        
    def __lt__(self, item):
        new_dict = {}
        for x in self.dl[::-1]:
            for k, v in x.items():
                if k not in new_dict:
                    new_dict[k] = v
        new_dict2 = {}     
        if type(item) == dict:
            return new_dict == item
        elif type(item) == DictList:
            for x in item.dl[::-1]:
                for k, v in x.items():
                    if k not in new_dict2:
                        new_dict2[k] = v
                    

            for x in sorted(new_dict.items()):
                if all(x) in sorted(new_dict2.items()):
                    return True
                else:
                    return False
        else:
            raise TypeError
        
if __name__ == '__main__':
    #Simple tests before running driver
    #Put your own test code here to test DictList before doing bsc tests

    ''''d = DictList(dict(a=1,b=2), dict(b=12,c=13))
    print('len(d): ', len(d))
    print('bool(d):', bool(d))
    print('repr(d):', repr(d))
    print(', '.join("'"+x+"'" + ' in d = '+str(x in d) for x in 'abcx'))
    print("d['a']:", d['a'])
    print("d['b']:", d['b'])
    print("d('b'):", d('b'))
    print('iter results:', ', '.join(i for i in d))
    print('item iter results:', ', '.join(str(i) for i in d.items()))
    print('d.collapse():', d.collapse())
    print('d==d:', d==d)
    print('d+d:', d+d)
    print('(d+d).collapse():', (d+d).collapse())'''
    
    print()
    import driver
    driver.default_file_name = 'bsc22S22.txt'
#     driver.default_show_exception= True
#     driver.default_show_exception_message= True
#     driver.default_show_traceback= True
    driver.driver()
