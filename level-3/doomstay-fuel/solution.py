# MarkovChain:
# - constructor(p)
# - fundamental_matrix
# - absorbing_states
# - absorbing_probabilities
# Matrix:
# - constructor(2x array)
# - subtract
# - multiply
# - inverse

def get_probabilities(m):
    probabilities = []

    for i, row in enumerate(m):
        probabilities_row = []
        row_sum = sum(row)
        for j, value in enumerate(row):
            if row_sum > 0:
                probabilities_row.append(float(value) / row_sum)
            else:
                probabilities_row.append(float(1) if i == j else float(0))
        probabilities.append(probabilities_row)

    return probabilities

def solution(m):
    p = get_probabilities(m)
    print('p: {}'.format(p))
    return 0
