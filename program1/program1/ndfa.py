#Author jchan20(Chan, Justin)


import goody


def read_ndfa(file : open) -> {str:{str:{str}}}:
    ndfa = dict()
    for line in file:
        split = line.strip().split(';')
        ndfa[split[0]] = dict()
        for num in range(1, len(split), 2):
            if split[num] not in ndfa[split[0]]:
                ndfa[split[0]][split[num]] = {split[num + 1]}
            else:
                ndfa[split[0]][split[num]].add(split[num + 1])
    return ndfa


def ndfa_as_str(ndfa : {str:{str:{str}}}) -> str:
    ndfa1 = sorted(ndfa.items())
    ndfa_string = ''
    for x in range(len(ndfa1)):
        if ndfa1[x][1] == {}:
            ndfa_string += '  {} transitions: {}\n'.format(ndfa1[x][0], list(ndfa1[x][1]))
        else:
            for key, value in ndfa1[x][1].items():
                ndfa1[x][1][key] = list(sorted(ndfa1[x][1][key]))
            ndfa_string += '  {} transitions: {}\n'.format(ndfa1[x][0], sorted(ndfa1[x][1].items()))
    return ndfa_string

       
def process(ndfa : {str:{str:{str}}}, state : str, inputs : [str]) -> [None]:
    result = [state]
    state_set = {state}
    storage_set = set()
    for x in inputs:
        in_ndfa = False
        for state in state_set:
            if x in ndfa[state]:
                storage_set.update(ndfa[state][x])
                in_ndfa = True
        if not in_ndfa:
            result.append((x, set()))
            return result
        result.append((x, set(storage_set)))
        state_set.clear()
        state_set.update(storage_set)
        storage_set.clear()
    return result


def interpret(result : [None]) -> str:
    interpret_string = 'Start state = {}\n'.format(result[0])
    for i in result[1:]:
        if i[1] != None:
            interpret_string += '  Input = {}; new possible states = {}\n'.format(i[0], list(sorted(i[1])))
        else:
            interpret_string += '  Input = {}; {}\n'.format(i[0], 'illegal input: simulation terminated')
    interpret_string += 'Stop state(s) = {}\n'.format(list(sorted(result[-1][-1])))
    return interpret_string





if __name__ == '__main__':
    # Write script here
    while True:
        try:
            file = input('Please enter the name of a file representing a non-deterministic finite automaton: ')
            ndfa = read_ndfa(open(file,'r'))
            print(ndfa_as_str(ndfa))
            break
        except:
            print('Invalid NDFA file, please try again')
            
    while True:
        try:
            file = input('Enter the name of a file storing the start-state and inputs to process: ')
            file = open(file,'r')
            for line in file:
                print(interpret(process(ndfa, line.strip().split(';')[0], line.strip().split(';')[1:])))
            break
        except:
            print('Invalid start-state and input file, please try again.')

    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc4.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
