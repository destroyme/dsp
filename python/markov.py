#!/usr/bin/env python

# Write a Markov text generator, [markov.py](python/markov.py). Your program should be called from the command line 
# with two arguments: the name of a file containing text to read, and the number of words to generate. 
# For example, if `chains.txt` contains the short story by Frigyes Karinthy, we could run:

# ```bash
# ./markov.py chains.txt 40
# ```

# A possible output would be:

# > show himself once more than the universe and what I often catch myself playing our well-connected game went on. 
# Our friend was absolutely correct: nobody from the group needed this way. We never been as the Earth has the 
# network of eternity.

# There are design choices to make; feel free to experiment and shape the program as you see fit. 
# Jeff Atwood's [Markov and You](http://blog.codinghorror.com/markov-and-you/) is a fun place to get started 
# learning about what you're trying to make.

import sys
import re
import random

from pprint import pprint as pp

if len(sys.argv) == 3:
    textfile = sys.argv[1]
    numwords = int(sys.argv[2])
else:
    sys.exit('usage: ./markov.py <text> <num of generated words>')
    
# GLOBALS
MARKOV_ORDER = 5

def textparser():
    r_text = re.compile(r"(\w+\s*[=\/+@!'#$\%\^\-\*]\s*\w+|\w+\.*|\(\w+\))", re.UNICODE)
    data = []

    with open(textfile, 'r') as f:
        for line in f:
            data.extend(r_text.findall(line.lower()))
    
    return data

data = textparser()
# print(data)

def get_ordered_data(data):
    ordered_data = []
    for i in range(0, len(data), MARKOV_ORDER):
        if i + MARKOV_ORDER < len(data):
            ordered_data.append(tuple(data[i:i+MARKOV_ORDER]))
        else:
            d = [data[i]]
            d.extend(data[0:MARKOV_ORDER-1])
            ordered_data.append(tuple(d))
    return ordered_data

ordered_data = get_ordered_data(data)
# pp(ordered_data)

def build_chain(data):
    chain = {}
    last_index = len(data) - 1
    for i, val in enumerate(data):
        if val not in chain and i != last_index:
            chain[val] = [(data[i+1], 1)]
        elif val not in chain and i == last_index:
            chain[val] = [(data[-2], 1)]
        elif val in chain and i != last_index:
            chain[val].append((data[i+1], 1))
        elif val in chain and i == last_index:
            chain[val].append((data[-2], 1))
    return chain

chain = build_chain(ordered_data)
# pp(chain)

def randomize_chain(data):
    k = len(data) // 1
    s1 = random.sample(data.keys(), k)
    s2 = random.sample(data.keys(), k)
    for i,s in enumerate(s1):
        data[s].append((s2[i],1))

randomize_chain(chain)

def determine_probabilities(data):
    for k, connections in data.items():
        
        conn_len = len(connections)

        if conn_len > 1:
            p = 1/conn_len
            new_conn = []
            for ind, connection in enumerate(connections):
                new_conn.append((connection[0], ind * p))
            data[k] = new_conn

determine_probabilities(chain)
# pp(chain)

def markov_traverse(node):
    p = random.random()
    best = (0,0)

    if len(node) == 1:
        best = node[0]
    else:
        for connection in node:
            if connection[1] <= p and  best[1] <= connection[1]:
                best = connection
    return chain[best[0]]

def print_chain():
    start = random.choice(list(chain.keys()))

    output = [start]
    _next = chain[start]
    for i in range(numwords // MARKOV_ORDER):
        _next = markov_traverse(_next)
        # pp(_next)
        output.append(_next[0][0])
    
    output = [item for sublist in output for item in sublist]
    output = ' '.join(map(str, output[:numwords]))
    return output


output = print_chain()
print(output)