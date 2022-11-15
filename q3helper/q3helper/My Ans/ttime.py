from goody import type_as_str
from pickle import FALSE
import copy

class Time:
    def __init__(self, *args):
        self.hour = 0
        self.minute = 0
        self.second = 0
        if len(args) == 1:
            if args[0] not in range(24) or type(args[0]) != int:
                raise AssertionError('Hour not between 0-23 or Value is not Int: ' + type_as_str(args[0]))
            else:
                self.hour = args[0]
        elif len(args) == 2:
            if args[0] not in range(24) or type(args[0]) != int:
                raise AssertionError('Hour not between 0-23 or Value is not Int: ' + type_as_str(args[0]))
            elif args[1] not in range(60) or type(args[1]) != int:
                raise AssertionError('Minute not between 0-59 or Value is not Int: ' + type_as_str(args[1]))
            else:
                self.hour = args[0]
                self.minute = args[1]
        elif len(args) == 3:
            if args[0] not in range(24) or type(args[0]) != int:
                raise AssertionError('Hour not between 0-23 or Value is not Int: ' + type_as_str(args[0]))
            elif args[1] not in range(60) or type(args[1]) != int:
                raise AssertionError('Minute not between 0-59 or Value is not Int: ' + type_as_str(args[1]))
            elif args[2] not in range(60) or type(args[2]) != int:
                raise AssertionError('Second not between 0-59 or Value is not Int: ' + type_as_str(args[2]))
            else:
                self.hour = args[0]
                self.minute = args[1]
                self.second = args[2]

        
    def __getitem__(self, index):
        if type(index) not in [int, tuple]:
            raise IndexError('Index is not of the correct type: ' + type_as_str(index))
        elif type(index) == int and index not in [1, 2, 3]:
            raise IndexError('Index is not a correct value: ' + type_as_str(index))
        elif type(index) == tuple:
            for x in index:
                if x not in [1, 2, 3]:
                    raise IndexError('Index is not a correct value: ' + type_as_str(index))
        if type(index) == int:
            if index == 1:
                return self.hour
            elif index == 2:
                return self.minute
            elif index == 3:
                return self.second
        elif type(index) == tuple:
            list1 = []
            for x in index:
                if x == 1:
                    list1.append(self.hour)
                elif x == 2:
                    list1.append(self.minute)
                elif x == 3:
                    list1.append(self.second)
            return tuple(list1)
    
    def __repr__(self):
        rep = 'Time(' + str(self.hour) + ',' + str(self.minute) + ',' + str(self.second) + ')'
        return rep
    
    def __str__(self):
        if self.hour > 12:
            self.hour -= 12
            self.ampm = 'pm'
        elif self.hour == 12:
            self.ampm = 'pm'
        elif self.hour == 0:
            self.hour += 12
            self.ampm = 'am'
        else:
            self.ampm = 'am'
        if self.minute < 10 or self.minute == 0:
            self.minute2 = '0' + str(self.minute)
        if self.second < 10 or self.second == 0:
            self.second2 = '0' + str(self.second)
        if self.minute > 10 and self.second > 10:
            time_str = str(self.hour) + ':' + str(self.minute) + ':' + str(self.second) + self.ampm
        elif self.minute < 10 and self.second > 10:
            time_str = str(self.hour) + ':' + self.minute2 + ':' + str(self.second) + self.ampm
        elif self.minute > 10 and self.second < 10:
            time_str = str(self.hour) + ':' + str(self.minute) + ':' + self.second2 + self.ampm
        else:
            time_str = str(self.hour) + ':' + self.minute2 + ':' + self.second2 + self.ampm
        return time_str

    def __bool__(self):
        if self.hour == 0 and self.minute == 0 and self.second == 0:
            return False
        else:
            return True

    def __len__(self):
        self.seconds = 0
        self.seconds += (self.hour * 60) * 60
        self.seconds += self.minute * 60
        self.seconds += self.second
        return self.seconds

    def __lt__(self, other):
        self.x = self.__len__()
        if type(other) == int:
            return self.x < other
        elif type(other) == Time:
            return self.x < other.__len__()
        elif type(other) != int:
            raise TypeError('NotImplemented: ' + type_as_str(other))

    def __iter__(self):
        return self
    
    def __copy__(self):
        return Time(self.hour, self.minute, self.second)
    
    def __add__(self, other):
        Time2 = Time(self.hour, self.minute, self.second)
        if type(other) != int:
            raise TypeError('NotImplemented')
        while other != 0:
            Time2.second += 1
            if Time2.second >= 60:
                Time2.second -= 60
                Time2.minute += 1
            if Time2.minute >= 60:
                Time2.minute -= 60
                Time2.hour += 1
            if Time2.hour == 24:
                Time2.hour -= 24
            other -= 1
        if Time2.hour > 12:
            Time2.hour -= 12
            Time2.ampm = 'pm'
        elif Time2.hour == 12:
            Time2.ampm = 'pm'
        elif Time2.hour == 0:
            Time2.hour += 12
            Time2.ampm = 'am'
        else:
            Time2.ampm = 'am'
        time_str = f"{Time2.hour}" + ':' + f"{Time2.minute:02d}" + ':' + f"{Time2.second:02d}" + Time2.ampm
        return time_str
    
    def __radd__(self, other):
        Time2 = Time(self.hour, self.minute, self.second)
        if type(other) != int:
            raise TypeError('NotImplemented')
        while other != 0:
            Time2.second += 1
            if Time2.second >= 60:
                Time2.second -= 60
                Time2.minute += 1
            if Time2.minute >= 60:
                Time2.minute -= 60
                Time2.hour += 1
            if Time2.hour == 24:
                Time2.hour -= 24
            other -= 1
        if Time2.hour > 12:
            Time2.hour -= 12
            Time2.ampm = 'am'
        elif Time2.hour == 12:
            Time2.ampm = 'am'
        elif Time2.hour == 0:
            Time2.hour += 12
            Time2.ampm = 'am'
        else:
            Time2.ampm = 'am'
        time_str = f"{Time2.hour}" + ':' + f"{Time2.minute:02d}" + ':' + f"{Time2.second:02d}" + Time2.ampm
        return time_str

    def __call__(self, a, b, c):
        self.hour = a
        self.minute = b
        self.second = c
        if a not in range(24) or type(a) != int:
            raise AssertionError('Hour not between 0-23 or Value is not Int: ' + type_as_str(a))
        elif b not in range(60) or type(b) != int:
            raise AssertionError('Hour not between 0-59 or Value is not Int: ' + type_as_str(b))
        elif c not in range(60) or type(c) != int:
            raise AssertionError('Hour not between 0-59 or Value is not Int: ' + type_as_str(c))


if __name__ == '__main__':
    # Put in simple tests for Time before allowing driver to run
    # Debugging is easier in script code than in bsc tests

    print('Start simple testing')
    print()

    import driver
    driver.default_file_name = 'bscq31S22.txt'
#     driver.default_show_traceback=True
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
    driver.driver()



        
        
        
        
        
