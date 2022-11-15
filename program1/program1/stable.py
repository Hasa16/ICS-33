#Author jchan20(Chan, Justin)


from copy import deepcopy

# Use these global variables to index the list associated with each name in the dictionary.
# e.g., if men is a dictionary, men['m1'][match] is the woman who matches man 'm1', and 
# men['m1'][prefs] is the list of preference for man 'm1'.
# It would seems that this list might be better represented as a named tuple, but the
# preference list it contains is mutated, which is not allowed in a named tuple. 

match = 0   # Index 0 of list associate with name is match (str)
prefs = 1   # Index 1 of list associate with name is preferences (list of str)


def read_match_preferences(open_file : open) -> {str:[str,[str]]}:
    match_dict = dict()
    for line in open_file:
        person = line.split(';')[0]
        matches = line.strip().split(';')[1:]
        match_dict[person] = [None, matches]
    return match_dict


def dict_as_str(d : {str:[str,[str]]}, key : callable=None, reverse : bool=False) -> str:
    match_list = sorted(d, key=key, reverse=reverse)
    dict_str = ''
    for i in match_list:
        dict_str += '  {} -> {}\n'.format(i, d[i])
    return dict_str


def who_prefer(order : [str], p1 : str, p2 : str) -> str:
    return p1 if order.index(p1) < order.index(p2) else p2


def extract_matches(men : {str:[str,[str]]}) -> {(str,str)}:
    return {(c, men[c][0]) for c in [y for y in men]}


def make_match(men : {str:[str,[str]]}, women : {str:[str,[str]]}, trace : bool = False) -> {(str,str)}:
    men_copy = deepcopy(men)
    single_men = {man for man in men if men[man][match] == None}
    if trace:
        print('\nWomen Preferences (unchanging)\n{}'.format(dict_as_str(women)))
              
    while len(single_men) != 0:
        if trace:
            print('Men Preferences (current)\n{}'.format(dict_as_str(men_copy)))
            print('unmatched men = {}\n'.format(single_men))   
        single_man = single_men.pop()
        match_woman = men_copy[single_man][prefs].pop(0) 
        matches = [match_value[match] for match_value in list(men_copy.values())]
        if match_woman not in matches: 
            men_copy[single_man][match] = match_woman
            women[match_woman][match] = single_man
            if trace:
                print('{} proposes to {}, who is currently unmatched, accepting proposal\n'.format(single_man, match_woman))
        elif match_woman in matches:  
            proposed_man = women[match_woman][match]
            if who_prefer((women[match_woman][prefs]), single_man, proposed_man) == single_man:
                men_copy[single_man][match] = match_woman
                women[match_woman][match] = single_man
                men_copy[proposed_man][match] = None
                single_men.add(proposed_man)
                if trace:
                    print('{} proposes to {}, who is currently matched, accepting the proposal (likes new match better)\n'.format(single_man, match_woman))
            else:
                single_men.add(single_man)
                if trace:
                    print('{} proposes to {}, who is currently matched, rejecting the proposal (likes current match better)\n'.format(single_man, match_woman))
    return extract_matches(men_copy)
  


  
    
if __name__ == '__main__':
    # Write script here
    while True:
        try:
            men_file = input('Specify the file name representing the preferences for men: ')
            men_pref = read_match_preferences(open(men_file,'r'))
            women_file = input('Specify the file name representing the preferences for women: ')
            women_pref = read_match_preferences(open(women_file,'r'))
            print('\nMen Preferences\n{}'.format(dict_as_str(men_pref)))
            print('Women Preferences\n{}'.format(dict_as_str(women_pref)))
            break
        except:
            print('Invalid preference file, please try again')

    while True:
        trace = input('Specify choice for tracing algorithm[True]: ')
        if trace == 'True':
            trace = True
            break
        elif trace == 'False':
            trace = False
            break
        else:
            print('Please enter a valid boolean value: True or False')
    print('The final matches: {}'.format(make_match(men_pref, women_pref, trace)))
    print('')
            
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc2.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
