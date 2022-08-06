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
    def rows_count(self):
        return len(self.matrix)

    @property
    def cols_count(self):
        return len(self.matrix[0])

    @staticmethod
    def zero(rows, cols):
        m = []
        for i in range(rows):
            m_row = []
            for j in range(cols):
                m_row.append(0)
            m.append(m_row)
        return Matrix(m)

    @staticmethod
    def identity(n):
        m = []
        for i in range(n):
            m_row = []
            for j in range(n):
                m_row.append(1 if i == j else 0)
            m.append(m_row)
        return Matrix(m)

    def __sub__(self, other):
        if self.rows_count != other.rows_count or self.cols_count != other.cols_count:
            raise TypeError('Can\'t subtract {}x{} matrix from {}x{} matrix'.format(self.rows_count, self.cols_count, other.rows_count, other.cols_count))
        m = []
        for i in range(self.rows_count):
            m_row = []
            for j in range(self.cols_count):
                m_row.append(self.matrix[i][j] - other.matrix[i][j])
            m.append(m_row)
        return Matrix(m)

    def get_minor_matrix(self, i, j):
        minor_matrix = []
        for row in self.matrix[:i] + self.matrix[i+1:]:
            minor_matrix_row = []
            for item in row[:j] + row[j+1:]:
                minor_matrix_row.append(item)
            minor_matrix.append(minor_matrix_row)
        return Matrix(minor_matrix)
    
    def get_determinant(self):
        if self.rows_count == 1:
            return self.matrix[0][0]
        if self.rows_count == 2:
            return self.matrix[0][0]*self.matrix[1][1] - self.matrix[0][1]*self.matrix[1][0]
        
        determinant = 0
        for j in range(self.cols_count):
            minor_matrix = self.get_minor_matrix(0, j)
            determinant += (((-1) ** j) * self.matrix[0][j] * minor_matrix.get_determinant())

        return determinant
    
    def get_transposed(self):
        m = Matrix.zero(self.rows_count, self.cols_count)
        for i in range(self.rows_count):
            for j in range(i, self.cols_count):
                m.matrix[i][j], m.matrix[j][i] = self.matrix[j][i], self.matrix[i][j]
        return m

    def transpose(self):
        for i in range(self.rows_count):
            for j in range(i, self.cols_count):
                self.matrix[i][j], self.matrix[j][i] = self.matrix[j][i], self.matrix[i][j]

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

    @property
    def r(self):
        t = self.transient_states_count
        a = self.absorbing_states_count
        r = []
        for row in self.transient_rows:
            r_row = []
            for j in range(t, t+a):
                r_row.append(row[j])
            r.append(r_row)
        return Matrix(r)

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
    if len(m) == 1:
        return [1, 1]

    test_matrix = Matrix(
        [[1,2,3],
        [4,5,6],
        [7,8,9]]
    )

    print('test_matrix.matrix: {}'.format(test_matrix.matrix))
    print('test_matrix.get_transposed().matrix: {}'.format(test_matrix.get_transposed().matrix))

    probabilities = Matrix(get_probabilities(m))
    print('probabilities.matrix: {}'.format(probabilities.matrix))
    print('probabilities.get_minor_matrix(0,0).matrix: {}'.format(probabilities.get_minor_matrix(0,0).matrix))
    print('probabilities.get_determinant(): {}'.format(probabilities.get_determinant()))
    print('Matrix.identity(3).matrix: {}'.format(Matrix.identity(3).matrix))
    markov_chain = MarkovChain(probabilities)
    print('markov_chain.transient_row_indexes: {}'.format(markov_chain.transient_row_indexes))
    print('markov_chain.transient_rows: {}'.format(markov_chain.transient_rows))
    print('markov_chain.absorbing_row_indexes: {}'.format(markov_chain.absorbing_row_indexes))
    print('markov_chain.absorbing_rows: {}'.format(markov_chain.absorbing_rows))
    print('markov_chain.absorbing_states_count: {}'.format(markov_chain.absorbing_states_count))
    print('markov_chain.transient_states_count: {}'.format(markov_chain.transient_states_count))
    print('markov_chain.q.matrix: {}'.format(markov_chain.q.matrix))
    print('markov_chain.r.matrix: {}'.format(markov_chain.r.matrix))

    print('markov_chain.q.rows_count: {}'.format(markov_chain.q.rows_count))
    i = Matrix.identity(markov_chain.q.rows_count)
    print('i.matrix: {}'.format(i.matrix))
    iq = i - markov_chain.q
    print('iq.matrix: {}'.format(iq.matrix))
    print('iq.get_minor_matrix(0,0): {}'.format(iq.get_minor_matrix(0,0)))

    return 0
