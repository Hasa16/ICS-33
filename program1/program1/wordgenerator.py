#Author: jchan20(Chan, Justin)


import goody
from goody import irange
import prompt
from random import choice


# For use in read_corpus: leave unchanged in this file
def word_at_a_time(file : open):
    for line in file:
        for item in line.strip().split():
                yield item


def read_corpus(os : int, file : open) -> {(str):[str]}:
    corpus = dict()
    word_list = list(file)
    start = 0
    while (start + os) < len(word_list):
        word_tuple = tuple(word_list[start:start + os])
        corpus.setdefault(word_tuple, [word_list[start + os]]).append(word_list[start + os])
        start += 1
    for i in corpus:
        corpus[i] = list(dict.fromkeys(corpus[i]))
    return corpus


def corpus_as_str(corpus : {(str):[str]}) -> str:
    minimum, maximum = 1, 1
    corpus_string = ''
    for i in sorted(corpus):
        corpus_string += '  {} can be followed by any of {}\n'.format(i, corpus[i])
        if len(corpus[i]) < minimum:
            minimum = len(corpus[i])
        if len(corpus[i]) > maximum:
            maximum = len(corpus[i])        
    corpus_string += 'min/max list lengths = {}/{}\n'.format(minimum, maximum)
    return corpus_string


def produce_text(corpus : {(str):[str]}, start : [str], count : int) -> [str]:
    for i in range(count):
        if tuple(start[i:len(start) + i]) not in corpus:
            start.append(None)
            return start
        value_list = corpus[tuple(start[i:len(start) + i])]
        start.append(choice(value_list))
    return start




        
if __name__ == '__main__':
    # Write script here
    while True:
        try:
            os = int(input('Specify the order statistic: '))
            assert(os > 0), 'Number must be bigger than 0' 
            file = input('Specify the file name representing the text to process: ')
            corpus = read_corpus(os, word_at_a_time(open(file)))
            print('Corpus\n' + corpus_as_str(corpus))
            break
        except:
            print('Please enter valid parameters')

        
    while True:
        try:
            print("Specify {} words starting the list".format(os))
            start = []
            for i in range(os):
                start.append(input('Specify word {}: '.format(i + 1)))
            count = eval(input("Specify # of words to append at the end of the started list: "))
            print('Random Text =', produce_text(corpus, start, count))
            break
        except:
            print('Please enter valid parameters')

    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc5.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
