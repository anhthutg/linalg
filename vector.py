class Vector:
    def __init__(self, obj):
        self._vec = Vector._build(obj)

    @staticmethod
    def _build(obj):
        vec = None
        if isinstance(obj, int):
            vec = [0] * obj
        elif isinstance(obj, list):
            vec = obj[:]
        else:
            raise ValueError('Invalid value.')
        return vec

    def __len__(self):
        return len(self._vec)

    def __getitem__(self, idx):
        return self._vec[idx]

    def __setitem__(self, idx, val):
        self._vec[idx] = val

    def __add__(self, other):
        if self.__len__() != other.__len__():
            raise ValueError('Matrices are not the same length.')
        
        return Vector([self._vec[i] + other._vec[i] for i in range(self.__len__())])

    def __iadd__(self, other):
        return Vector([self._vec[i] + self._vec[i] for i in range(self.__len__())])

    def __mul__(self, other):
        if isinstance(other, int):
            return Vector([self._vec[i] * other for i in range(self.__len__())])
        elif isinstance(other, Vector):
            if self.__len__() != other.__len__():
                raise ValueError('Matrices are not the same length.')
            return Vector([self._vec[i] * other._vec[i] for i in range(self.__len__())])

    # def __imul__(self, other):
    #     return Vector([self._vec[i] * self._vec[i] for i in range(self.__len__())])

    def dot(self, other):
        if self.__len__() != other.__len__():
            raise ValueError('Matrices are not the same length.')
        return Vector.dot_product(self, other)

    @staticmethod
    def dot_product(vec1, vec2):
        return sum(vec1[i] * vec2[i] for i in range(len(vec1)))

    def __repr__(self):
        return '<Vector %r' % self._vec

    __str__ = __repr__
