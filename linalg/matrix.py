import copy
from linalg.vector import Vector

"""
Matrix library
==============
Operators:
    - Addition/In-place addition/Right operand addition
    - Multiply by a number/matrix / Right operand multiplication
    - In-place multiply by a number/matrix
    - Dot product
    - Transpose
"""

# =============================================================================

class Matrix():
    """Matrix utility class

    Matrix object generated from a nested list where each element in a matrix representing a row
    """

    def __init__(self, obj):
        """Initialize a matrix with given dimension or from an input nested list of numbers
        """
        self._mat = Matrix._build(obj)

    @staticmethod
    def _build(obj):
        """Create a matrix from the given input

        Args:
            obj (tuple(int)/List[List[int]]): input dimension or input nested list
        Returns:
            List[List[int]]: nested list of numbers for matrix
        """
        mat = None
        if isinstance(obj, tuple) and len(obj) == 2:
            mat = [[0] * obj[1] for _ in range(obj[0])]
        elif isinstance(obj, list) and len(obj[0]) != 0:
            mat = copy.deepcopy(obj)
        else:
            raise ValueError('Invalid value')
        return mat

    @property
    def num_rows(self):
        """Returns the number of rows of the matrix

        Returns:
            (int) : number of rows
        """
        return len(self._mat)

    @property
    def num_cols(self):
        """Returns the number of columns of the matrix

        Returns:
            (int) : number of columns
        """
        return len(self._mat[0])

    def order(self):
        """Returns the dimension of the matrix

        Returns:
            (int, int) : matrix dimension
        """
        return (self.num_rows, self.num_cols)

    def __getitem__(self, idx):
        """Get the element of a matrix

        Args:
            idx [int][int] : index of element to get
        Returns:
            Element of given index
        """
        return self._mat[idx]

    def __setitem__(self, idx, val):
        """Assign the value val to an element of matrix

        Args:
            idx [int][int] : index of element to access
            val : value to assign
        """
        self._mat[idx] = val

    def __add__(self, other):
        """Implements the addition of 2 matrices

        Args:
            other (Matrix) : input matrix
        Returns:
            (Matrix) : sum of 2 matrices
        """
        if isinstance(other, Matrix):
            if self.num_rows != other.num_rows or self.num_cols != other.num_cols:
                raise ValueError('Matrices are not the same dimension')
            return Matrix([[self[i][j] + other[i][j] for j in range(self.num_cols)] for i in range(self.num_rows)])

    def __iadd__(self, other):
        """Implements the addition of 2 matrices with in-place change

        Args:
            other (Matrix) : input matrix
        Returns:
            self (Matrix) : current object
        """
        if isinstance(other, Matrix):
            if self.num_rows != other.num_rows or self.num_cols != other.num_cols:
                raise ValueError('Matrices are not the same dimension')
            for i in range(self.num_rows):
                for j in range(self.num_cols):
                    self[i][j] += other[i][j]
            return self

    def __radd__(self, other):
        """Implements the right operand addition

        Returns:
            (Matrix) : sum of 2 matrices
        """
        return self.__add__(other)

    def __mul__(self, other):
        """Implements the multiplication

        Args:
            other (Matrix/int) : input matrix or input number
        Returns:
            (Matrix) : multiplation of 2 matrices or a matrix by a number
        """
        if isinstance(other, int):
            return Matrix([[self[i][j] * other for j in range(self.num_cols)] for i in range(self.num_rows)])
        elif isinstance(other, Matrix):
            if self.num_rows != other.num_rows or self.num_cols != other.num_cols:
                raise ValueError('Matrices are not the same dimension')
            return Matrix([[self[i][j] * other[i][j] for j in range(self.num_cols)] for i in range(self.num_rows)])

    def __imul__(self, other):
        """Implements the multiplication with in-place change

        Args:
            other (Matrix/int) : input matrix or input number
        Returns:
            self (Matrix) : multiplation of 2 matrices or a matrix by a number
        """
        if isinstance(other, int):
            return [[self[i][j] * other for j in range(self.num_cols)] for i in range(self.num_rows)]
        elif isinstance(other, Matrix):
            if self.num_rows != other.num_rows or self.num_cols != other.num_cols:
                raise ValueError('Matrices are not the same dimension')
            for i in range(self.num_rows):
                for j in range(self.num_cols):
                    self[i][j] *= other[i][j]
            return self

    def __rmul__(self, other):
        """Implements the right operand multiplication

        Args:
            other (Vector/int) : input vector or input number
        Returns:
            (Matrix/Vector) : multiplication of a matrix by a vector/a matrix by a number or vice versa
        """
        if isinstance(other, int):
            return Matrix([[self[i][j] * other for j in range(self.num_cols)] for i in range(self.num_rows)])
        elif isinstance(other, Vector):
            if self.num_cols != len(other):
                raise ValueError('The number of columns of the matrix must be equal to the length of the vector')
            return Vector([sum(self[i][j] * other[j] for j in range(len(other))) for i in range(self.num_rows)])

    def transpose(self):
        """Returns the transpose of the matrix

        Returns:
            (Matrix) : transpose matrix
        """
        return Matrix(list(map(list, zip(*self))))

    def dot(self, other):
        """Implements the dot product of 2 matrices

        Args:
            self, other (Matrix) : input matrix
        Returns:
            (Matrix) : dot product of 2 matrices
        """
        if isinstance(other, Matrix):
            if self.num_cols != other.num_rows:
                raise ValueError('Matrices are not the same dimension')
            return Matrix([[sum([self[i][k] * other[k][j] for k in range(other.num_rows)]) for j in range(other.num_cols)] 
                            for i in range(self.num_rows)])

    @staticmethod
    def dot_product(mat1, mat2):
        """Implements the dot product of 2 nested lists

        Args:
            mat1, mat2 (List[List[int]]) : input nested list
        Returns:
            (List[List[int]]) : dot product of 2 nested lists
        """
        if len(mat1[0]) != len(mat2):
            raise ValueError('Matrices are not the same dimension')
        return [[sum([mat1[i][k] * mat2[k][j] for k in range(len(mat2))]) for j in range(len(mat2[0]))] 
                            for i in range(len(mat1))]

    def __repr__(self):
        return '<Matrix %r>' % self._mat

    __str__ = __repr__
    # def __str__(self):
    #     return self._mat

    def __eq__(self, other):
        return self._mat == other
    