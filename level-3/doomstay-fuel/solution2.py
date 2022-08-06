# Technique used:
# https://en.wikipedia.org/wiki/Absorbing_Markov_chain
# https://brilliant.org/wiki/absorbing-markov-chains/

import numpy as np

class MarkovChain:
    def __init__(self, p):
        self.p = p

def get_markov_chain_probabilities(m):
    p = []

    for i, row in enumerate(m):
        p_row = []
        row_sum = sum(row)
        for j, value in enumerate(row):
            if row_sum > 0:
                p_row.append(float(value) / row_sum)
            else:
                p_row.append(float(1) if i == j else float(0))
        p.append(p_row)

    return p

def solution(m):
    p = get_markov_chain_probabilities(m)
    print('p: {}'.format(p))
    markov_chain = MarkovChain(p)
    print('markov_chain.p: {}'.format(markov_chain.p))
    return 0
