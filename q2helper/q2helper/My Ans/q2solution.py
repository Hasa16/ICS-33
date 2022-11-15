#Author jchan20(Chan, Justin)



import re


# Before running the driver on the bsc.txt file, ensure you have put a regular
#   expression pattern in the files repattern1a.txt, repattern1b.txt,
#   repattern1c.txt, and repattern2.txt.
# The patterns must be all on the first line, enclosed in ^ and $


def expand_re(pat_dict:{str:str}):
    list1 = []
    x = 10
    for key in pat_dict.keys():
        list1.append(key)
    while x != 0:
        for k, v in pat_dict.items():
            value_list = v.split('#')
            for i in range(len(value_list)):
                if value_list[i] in list1:
                    value_list[i] = f'(?:{pat_dict.get(list1[list1.index(value_list[i])])})'
            v2 = ''.join(value_list)
            pat_dict[k] = v2
        x -= 1
    return pat_dict


def multi_search(pat_file : open, text_file : open) -> [(int,str,[int])]:
    patternsform = []
    for pattern in pat_file:
        patternsform.append(pattern.rstrip())
    j = 1
    finalresult = []
    for line in text_file:
        matching_patterns = []
        line = line.rstrip()
        for k in range(0, len(patternsform)):
            if re.search(patternsform[k], line):
                matching_patterns.append(k+1)
        if line == '(pause)':
            j += 1
        if len(matching_patterns) != 0:
            finalresult.append((j, line, matching_patterns))
            j += 1
    pat_file.close()
    text_file.close()
    return finalresult

#printing the file
print(multi_search(open('pats1.txt'),open('texts1.txt')))




if __name__ == '__main__':
    
    p1a = open('repattern1a.txt').readline().rstrip() # Read pattern on first line
    print('Testing the pattern p1a: ',p1a)
    for text in open('bm1a.txt'):
        text = text.rstrip()
        print('Matching against:',text)
        m = re.match(p1a,text)
        print(' ','Matched' if m != None else "Not matched")


    p1b = open('repattern1b.txt').readline().rstrip() # Read pattern on first line
    print('\nTesting the pattern p1b: ',p1b)
    for text in open('bm1b.txt'):
        text = text.rstrip()
        print('Matching against:',text)
        m = re.match(p1b,text)
        print('  ','Matched' if m != None else 'Not matched' )
        
        
    p1c = open('repattern1c.txt').readline().rstrip() # Read pattern on first line
    print('\nTesting the pattern p1c: ',p1c)
    for text in open('bm1b.txt'):                 # Same file as before
        text = text.rstrip()
        print('Matching against:',text)
        m = re.match(p1c,text)
        print('  ','Matched with groups ='+ str(m.groups()) if m != None else 'Not matched' )
        
        
    p2 = open('repattern2.txt').read().rstrip() # Read pattern on first line
    print('\nTesting the pattern p2: ',p2)
    for text in open('bm2.txt'):
        text = text.rstrip()
        print('Matching against:',text)
        m = re.match(p2,text)
        print('  ','Matched' if m != None else 'Not matched' )
        
    
    
    print('\nTesting expand_re')
    pd = dict(digit = r'[0-9]', integer = r'[+-]?#digit##digit#*')
    print('  Expanding ',pd)
    expand_re(pd)
    print('  result =',pd)
    # produces/prints the dictionary
    # {'digit': '[0-9]', 'integer': '[+-]?(?:[0-9])(?:[0-9])*'}
     
    pd = dict(integer       = r'[+-]?[0-9]+',
              integer_range = r'#integer#(..#integer#)?',
              integer_list  = r'#integer_range#(,#integer_range#)*',
              integer_set   = r'{#integer_list#?}')
    print('\n  Expanding ',pd)
    expand_re(pd)
    print('  result =',pd)
    # produces/prints the dictionary 
    # {'integer': '[+-]?[0-9]+',
    #  'integer_range': '(?:[+-]?[0-9]+)(..(?:[+-]?[0-9]+))?',
    #  'integer_list': '(?:(?:[+-]?[0-9]+)(..(?:[+-]?[0-9]+))?)(,(?:(?:[+-]?[0-9]+)(..(?:[+-]?[0-9]+))?))*',
    #  'integer_set': '{(?:(?:(?:[+-]?[0-9]+)(..(?:[+-]?[0-9]+))?)(,(?:(?:[+-]?[0-9]+)(..(?:[+-]?[0-9]+))?))*)?}'
    # }
     
    pd = dict(a='correct',b='#a#',c='#b#',d='#c#',e='#d#',f='#e#',g='#f#')
    print('\n  Expanding ',pd)
    expand_re(pd)
    print('  result =',pd)
    # produces/prints the dictionary 
    # {'a': 'correct',
    #  'b': '(?:correct)',
    #  'c': '(?:(?:correct))',
    #  'd': '(?:(?:(?:correct)))',
    #  'e': '(?:(?:(?:(?:correct))))',
    #  'f': '(?:(?:(?:(?:(?:correct)))))',
    #  'g': '(?:(?:(?:(?:(?:(?:correct))))))'
    # }


        
    print()
    print()
    import driver
    driver.default_file_name = "bscq2S22.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
