from goody import type_as_str
from pickle import FALSE
import copy

class Time:
    def __init__(self, hour: int=0, minute: int=0, second: int=0):
        assert type(hour) is int and 0 <= hour <= 23,   'Time.__init__: hour('+str(hour)+') is not int in range [0,23)'
        assert type(hour) is int and 0 <= minute <= 59, 'Time.__init__: minute('+str(minute)+') is not int in range [0,59)'
        assert type(hour) is int and 0 <= second <= 59, 'Time.__init__: second('+str(second)+') is not int in range [0,59)'
        self.hour   = hour
        self.minute = minute
        self.second = second
        
    def __getitem__(self, index):
        if type(index) is not tuple:
            index = (index,)
        if not all(type(i) is int and 1<=i<=3 for i in index):
            raise IndexError('Time.__getitem__: illegal argument in '+str(index))
        answer = tuple(self.hour if i==1 else self.minute if i==2 else self.second for i in index)
        if len(answer)==1:
            answer = answer[0]
        return answer
    
    def __repr__(self):
        rep = 'Time(' + str(self.hour) + ',' + str(self.minute) + ',' + str(self.second) + ')'
        return rep
    
    def __str__(self):
        def two_digit(d): return ('' if d >= 10 else '0' ) + str(d)            
        start = str(12 if self.hour == 0 else self.hour if self.hour <= 12 else self.hour-12)
        return start + ':'+two_digit(self.minute)+':'+two_digit(self.second)+('am' if self.hour<12 else 'pm')

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



        
        
        
        
        
