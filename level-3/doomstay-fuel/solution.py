# MarkovChain:
# - constructor(p)
# - transient states count
# - absorbing states count
# - fundamental_matrix
# - absorbing_states
# - absorbing_probabilities
# Matrix:
# - constructor(2x array)
# - subtract
# - multiply
# - inverse

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    @property
    def matrix(self):
        return self.matrix
    
    @property
    def cols_count(self):
        return len(self.matrix)

class MarkovChain:
    def __init__(self, probabilities):
        self.probabilities = probabilities
    
    @staticmethod
    def is_absorbing_row(row, index):
        if row[index] != 1:
            return False

        absorbing = True
        for i, value in enumerate(row):
            if i != index and value != 0:
                absorbing = False
        return absorbing

    @property
    def transient_row_indexes(self):
        indexes = []
        for i, row in enumerate(self.probabilities.matrix):
            if not self.is_absorbing_row(row, i):
                indexes.append(i)
        return indexes

    @property
    def transient_rows(self):
        indexes = self.transient_row_indexes
        rows = []
        for i in indexes:
            rows.append(self.probabilities.matrix[i])
        return rows
    
    @property
    def absorbing_row_indexes(self):
        indexes = []
        for i, row in enumerate(self.probabilities.matrix):
            if self.is_absorbing_row(row, i):
                indexes.append(i)
        return indexes

    @property
    def absorbing_rows(self):
        indexes = self.absorbing_row_indexes
        rows = []
        for i in indexes:
            rows.append(self.probabilities.matrix[i])
        return rows

    @property
    def transient_states_count(self):
        return len(self.transient_row_indexes)

    @property
    def absorbing_states_count(self):
        return len(self.absorbing_row_indexes)

    @property
    def q(self):
        t = self.transient_states_count
        q = []
        for row in self.transient_rows:
            q_row = []
            for j in range(t):
                q_row.append(row[j])
            q.append(q_row)
        return Matrix(q)

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
    probabilities = Matrix(get_probabilities(m))
    print('probabilities.matrix: {}'.format(probabilities.matrix))
    markov_chain = MarkovChain(probabilities)
    print('markov_chain.transient_row_indexes: {}'.format(markov_chain.transient_row_indexes))
    print('markov_chain.transient_rows: {}'.format(markov_chain.transient_rows))
    print('markov_chain.absorbing_row_indexes: {}'.format(markov_chain.absorbing_row_indexes))
    print('markov_chain.absorbing_rows: {}'.format(markov_chain.absorbing_rows))
    print('markov_chain.absorbing_states_count: {}'.format(markov_chain.absorbing_states_count))
    print('markov_chain.transient_states_count: {}'.format(markov_chain.transient_states_count))
    print('markov_chain.q.matrix: {}'.format(markov_chain.q.matrix))
    return 0