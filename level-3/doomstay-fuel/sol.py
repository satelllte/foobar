import numpy as np

def detect_states(matrix):
    active, terminal = [], []
    for rowN, row in enumerate(matrix):
        (active if sum(row) else terminal).append(rowN)
    return (active, terminal)

def simplest_form(B):
    B = B.round().astype(int).A1
    gcd = np.gcd.reduce(B)
    B = np.append(B, B.sum())                   
    return (B / gcd).astype(int)

def solution(m):
    active, terminal = detect_states(m)
    if 0 in terminal:
        return [1] + [0]*len(terminal[1:]) + [1]
    m = np.matrix(m, dtype=float)[active, :]
    comm_denom = np.prod(m.sum(1))
    P = m / m.sum(1)            
    Q, R = P[:, active], P[:, terminal]
    I = np.identity(len(Q))
    N = (I - Q) ** (-1)   
    B = N[0] * R * comm_denom / np.linalg.det(N)
    return simplest_form(B)
