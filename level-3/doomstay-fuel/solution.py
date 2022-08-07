# Technique used:
# https://en.wikipedia.org/wiki/Absorbing_Markov_chain
# https://brilliant.org/wiki/absorbing-markov-chains/

from fractions import Fraction
import numpy as np

def solution(m):
    active_states = []
    terminal_states = []

    for i, row in enumerate(m):
        (active_states if sum(row) else terminal_states).append(i)

    if 0 in terminal_states:
        return [1] + [0]*len(terminal_states[1:]) + [1]

    m = np.matrix(m, dtype=float)[active_states, :]    
    p_matrix = m / m.sum(axis=1)
    q_matrix = p_matrix[:, active_states]
    r_matrix = p_matrix[:, terminal_states]
    identity_matrix = np.identity(len(q_matrix))
    fundamental_matrix = np.linalg.inv(np.subtract(identity_matrix, q_matrix))
    absorption_probabilities_matrix = np.matmul(fundamental_matrix, r_matrix)

    final_probabilities = np.array(absorption_probabilities_matrix[0,:])[0]
    fractions = [Fraction(i).limit_denominator() for i in final_probabilities]
    final_denominator = np.lcm.reduce([fraction.denominator for fraction in fractions])

    return [fraction.numerator * (final_denominator / fraction.denominator) for fraction in fractions] + [final_denominator]
