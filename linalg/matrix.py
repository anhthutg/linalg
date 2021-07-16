class Matrix():
    def __init__(self, obj):
        self._mat = Matrix._build(obj)

    @staticmethod
    def _build(obj):
        mat = None
        if isinstance(obj, tuple) and len(obj) == 2:
            mat = [[0] * obj[1] for _ in range(obj[0])]
        elif isinstance(obj, list) and len(obj[0]) != 0:
            mat = obj[:]
        else:
            raise ValueError('Invalid value')
        return mat

    @property
    def num_rows(self):
        return len(self._mat)

    @property
    def num_cols(self):
        return len(self._mat[0])

    def order(self):
        return (self.num_rows, self.num_cols)

    def __getitem__(self, idx):
        return self._mat[idx]

    def __setitem__(self, idx, val):
        self._mat[idx[0]][idx[1]] = val

    def __add__(self, other):
        if self.num_rows != other.num_rows or self.num_cols != other.num_cols:
            raise ValueError('Matrices are not the same size')
        return Matrix([[self[i][j] + other[i][j] for j in range(self.num_cols)] for i in range(self.num_rows)])

    def __iadd__(self, other):
        if self.num_rows != other.num_rows or self.num_cols != other.num_cols:
            raise ValueError('Matrices are not the same size')
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self[i][j] += other[i][j]
        return self

    def __mul__(self, other):
        if isinstance(other, int):
            return Matrix([[self[i][j] * other for j in range(self.num_cols)] for i in range(self.num_rows)])
        elif isinstance(other, Matrix):
            if self.num_rows != other.num_rows or self.num_cols != other.num_cols:
                raise ValueError('Matrices are not the same size')
            return Matrix([[self[i][j] * other[i][j] for j in range(self.num_cols)] for i in range(self.num_rows)])

    def __imul__(self, other):
        if isinstance(other, int):
            return [[self[i][j] * other for j in range(self.num_cols)] for i in range(self.num_rows)]
        elif isinstance(other, Matrix):
            if self.num_rows != other.num_rows or self.num_cols != other.num_cols:
                raise ValueError('Matrices are not the same size')
            for i in range(self.num_rows):
                for j in range(self.num_cols):
                    self[i][j] *= other[i][j]
            return self

    def transpose(self):
        return Matrix([[self[j][i] for j in range(self.num_cols)] for i in range(self.num_rows)])

    def dot_product(self, other):
        if self.num_cols == other.num_rows:
            return Matrix([[sum([self[i][k] * other[k][j] for k in range(other.num_rows)]) for j in range(other.num_cols)] 
                            for i in range(self.num_rows)])

    def __repr__(self):
        return '<Matrix %r>' % self._mat

    __str__ = __repr__