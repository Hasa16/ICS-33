#Author jchan20(Chan, Justin)


import goody


def read_fa(file : open) -> {str:{str:str}}:
    fa = dict()
    for line in file:
        split_line = line.strip().split(';')
        for num in range(1, len(split_line), 2):
            fa.setdefault(split_line[0], dict()).update({split_line[num]:split_line[num + 1]})
    return fa


def fa_as_str(fa : {str:{str:str}}) -> str:
    sort_fa = sorted(fa.items())
    fa_string = ''
    for key in sort_fa:
        fa_string += '  {} transitions: {}\n'.format(key[0], list(sorted(key[1].items())))
    return fa_string   

    
def process(fa : {str:{str:str}}, state : str, inputs : [str]) -> [None]:
    fa_result = [state]
    for x in inputs:
        in_fa = False
        for value in fa[state]:
            if value == x:
                state = fa[state][value]
                fa_result.append((x, state))
                in_fa = True
        if in_fa == False:
            fa_result.append((x, None))
    return fa_result 


def interpret(fa_result : [None]) -> str:
    interpret_string = 'Start state = {}\n'.format(fa_result[0])
    for i in fa_result[1:]:
        if i[1] != None:
            interpret_string += '  Input = {}; new state = {}\n'.format(i[0], i[1])
        else:
            interpret_string += '  Input = {}; {}\n'.format(i[0], 'illegal input: simulation terminated')
    interpret_string += 'Stop state = {}\n'.format(fa_result[-1][-1])
    return interpret_string




if __name__ == '__main__':
    # Write script here
    while True:
        try:
            file = input('Please enter the name of a file representing a finite automaton: ')
            fa = read_fa(open(file,'r'))
            print(fa_as_str(fa))
            break
        except:
            print('Invalid FA file, please try again')

    while True:
        try:
            file = input('Enter the name of a file storing the start-state and inputs to process:')
            file = open(file,'r')
            for line in file:
                print(interpret(process(fa, line.strip().split(';')[0], line.strip().split(';')[1:])))
            break
        except:
            print('Invalid start-state and input file, please try again.')
            
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc3.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
