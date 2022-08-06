# Technique used:
# https://en.wikipedia.org/wiki/Absorbing_Markov_chain
# https://brilliant.org/wiki/absorbing-markov-chains/

import numpy as np
from fractions import Fraction

class MarkovChain:
    def __init__(self, p):
        self.p = p
    
    @staticmethod
    def is_absorption_row(row, index):
        if row[index] != 1.0:
            return False

        absorption = True
        for i, value in enumerate(row):
            if i != index and value != 0:
                absorption = False
        return absorption
    
    @property
    def transient_row_indexes(self):
        indexes = []
        for i, row in enumerate(self.p):
            if not self.is_absorption_row(row, i):
                indexes.append(i)
        return indexes

    @property
    def transient_rows(self):
        indexes = self.transient_row_indexes
        rows = []
        for i in indexes:
            rows.append(self.p[i])
        return rows
    
    @property
    def absorption_row_indexes(self):
        indexes = []
        for i, row in enumerate(self.p):
            if self.is_absorption_row(row, i):
                indexes.append(i)
        return indexes

    @property
    def absorption_rows(self):
        indexes = self.absorption_row_indexes
        rows = []
        for i in indexes:
            rows.append(self.p[i])
        return rows

    @property
    def transient_states_count(self):
        return len(self.transient_row_indexes)

    @property
    def absorption_states_count(self):
        return len(self.absorption_row_indexes)

    @property
    def q(self):
        t = self.transient_states_count
        q = []
        for row in self.transient_rows:
            q_row = []
            for j in range(t):
                q_row.append(row[j])
            q.append(q_row)
        return q
    
    @property
    def r(self):
        t = self.transient_states_count
        a = self.absorption_states_count
        r = []
        for row in self.transient_rows:
            r_row = []
            for j in range(t, t+a):
                r_row.append(row[j])
            r.append(r_row)
        return r
    
    @property
    def fundamental_matrix(self):
        q = self.q
        i = np.identity(len(q))
        n = np.linalg.inv(np.subtract(i, q))
        return n
    
    @property
    def absorption_probabilities(self):
        return np.matmul(self.fundamental_matrix, self.r)

def get_markov_chain_probabilities_from_input(m):
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
    p = get_markov_chain_probabilities_from_input(m)

    markov_chain = MarkovChain(p)

    if 0 in markov_chain.absorption_row_indexes:
        return [1] + [0]*(len(markov_chain.absorption_row_indexes) - 1) + [1]

    final_probabilities = markov_chain.absorption_probabilities[0]
    fractions = [Fraction(i).limit_denominator() for i in final_probabilities]
    final_denominator = np.lcm.reduce([fraction.denominator for fraction in fractions])

    result = []
    for fraction in fractions:
        result.append(fraction.numerator * (final_denominator / fraction.denominator))
    result.append(final_denominator)

    return result
