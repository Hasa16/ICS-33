from collections import defaultdict


class TrackHistory:
    def __init__(self):
        pass

    
    def __getattr__(self,name):
        name2 = name.split('_')
        if name2[0] in self.__dict__:
            if name2[1][-1].isnumeric() is True:
                x = int(name2[1][-1])
                if x == 0:
                    return self.__dict__[name2[0]]
                elif f'{name2[0]}{x}' not in self.__dict__.keys():
                    return None
                else:
                    return self.__dict__[f'{name2[0]}{x}']
            elif len(name2) > 2:
                raise NameError('Value after _prev is not a number')
            elif name2[1][-1] == 'v':
                return self.__dict__[f'{name2[0]}{1}']
        else:
            raise NameError('Value is not within the object.')


    def __getitem__(self,index):
        keys = []
        new_dict = {}
        if index > 0:
            raise IndexError('Value is not 0 or negative.')
        elif index == 0:
            for x in self.__dict__.keys():
                if x[-1].isnumeric() is True:
                    continue
                else:
                    keys.append(x)
            for y in keys:
                new_dict[y] = self.__dict__[y]
            return new_dict
        
        elif index == -1:
            for x in self.__dict__.keys():
                if x[0] == 'y' and x[-1].isnumeric() is True:
                    keys.append(x)
                elif x[-1].isnumeric() is True:
                    if int(x[-1]) == abs(index):
                        keys.append(x)
                else:
                    continue
            for y in keys:
                new_dict[y[0]] = self.__dict__[y]
            return new_dict
        
        elif index == -2:
            for x in self.__dict__.keys():
                if x[0] == 'y':
                    new_dict[x[0]] = None
                elif x[-1].isnumeric() is True:
                    if int(x[-1]) == abs(index):
                        keys.append(x)
                else:
                    continue
            for y in keys:
                new_dict[y[0]] = self.__dict__[y]
            return new_dict
        
        
    def __setattr__(self,name,value):
        if '_prev' in name:
            raise NameError
        else:
            if name in self.__dict__:
                self.__dict__[f'{name}{3-self.__dict__[name]}'] = self.__dict__[name]
                self.__dict__[name] = value
            else:
                self.__dict__[name] = value




if __name__ == '__main__':
    # Put in simple tests for TrackHistory before allowing driver to run
    # Debugging is easier in script code than in bsc tests
    
    print('Start simple testing')
    print()
    
    import driver
    driver.default_file_name = 'bscq32S22.txt'
#     driver.default_show_traceback=True
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
    driver.driver()
