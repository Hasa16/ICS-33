#Author: jchan20(Chan, Justin)

import goody
import prompt
from collections import defaultdict


def read_graph(file : open) -> {str:{str}}:
    graph = dict()
    for line in file:
        start, end = line[0], line[2]
        if start in graph:
            graph[start].update({end})
        elif start not in graph:
            graph[start] = ({end})
    return graph


def graph_as_str(graph : {str:{str}}) -> str:
    graph_list = sorted(graph.items())
    graph_string = ''
    for i in graph_list:
        graph_string += '  {} -> {}\n'.format(i[0], list(sorted(i[1])))
    return graph_string

        
def reachable(graph : {str:{str}}, start : str, trace : bool = False) -> {str}:
    explore_list = [start]
    reached = set()
    while explore_list != []:
        explore = explore_list.pop(0)
        reached.update({explore})
        if len(reached) > len(graph) or len(explore_list) > len(graph):
            break
        if explore not in graph:
            continue
        for reachable_node in graph[explore]:
            explore_list.append(reachable_node)
    return reached


if __name__ == '__main__':
    # Write script here
    while True:
        file = input('Enter name of a file representing a graph: ')
        try:
            graph_dict = read_graph(open(file))
            print(graph_as_str(graph_dict))
            break
        except:
            print('Not a valid file name, please try again.')

    while True:
        start = input('Enter a starting node: ')
        if start == 'quit':
            break
        try:
            reached = reachable(graph_dict, start, False)
            print('From the starting node: {}, the reachable nodes are'.format(start), reached)
            break
        except:
            print(start, 'is not a valid starting node, please try again.')

    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc1.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
