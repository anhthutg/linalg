"""
Vector libraby
==============
Operators:
    - Addition/In-place addition
    - Multiply by a number/vector
    - In-place multiply by a number/vector
    - Dot product
"""


# =============================================================================

class Vector:
    """Vector utility class"""

    def __init__(self, obj):
        """Initialize a vector with given size or from an input list of numbers
        """
        self._vec = Vector._build(obj)

    @staticmethod
    def _build(obj):
        """Create a vector from the given input

        Args:
            obj (int/List[int]): input size or input list
        Returns:
            List[int]: list of numbers for vector
        """
        vec = None
        if isinstance(obj, int):
            vec = [0] * obj
        elif isinstance(obj, list):
            vec = obj[:]
        else:
            raise ValueError('Invalid value')
        return vec

    def __len__(self):
        """Returns the size of a vector

        Returns:
            (int) : length of vector
        """
        return len(self._vec)

    def __getitem__(self, idx):
        """Get the element of a vector

        Args:
            idx (int) : index of element to get
        Returns:
            Element of given index
        """
        return self._vec[idx]

    def __setitem__(self, idx, val):
        """Assign the value val to an element of vector

        Args:
            idx (int) : index of element to access
            val : value to assign
        """
        self._vec[idx] = val

    def __add__(self, other):
        """Implements the addition of 2 vectors

        Args:
            other (Vector) : input vector
        Returns:
            (Vector) : sum of 2 vectors
        """
        if len(self) != len(other):
            raise ValueError('Vectors are not the same size')
        
        return Vector([self[i] + other[i] for i in range(len(self))])

    def __iadd__(self, other):
        """Implements the addition of 2 vectors with in-place change

        Args:
            other (Vector) : input vector
        Returns:
            self (Vector) : current object
        """
        if len(self) != len(other):
            raise ValueError('Vectors are not the same size')
        for i, v in enumerate(other):
            self[i] += v
        return self

    def __mul__(self, other):
        """Implements the multiplcation

        Args:
            other (Vector/int) : input vector or input number
        Returns:
            (Vector) : multiplation of 2 vectors or a vector by a number
        """
        if isinstance(other, int):
            return Vector([self[i] * other for i in range(len(self))])
        elif isinstance(other, Vector):
            if len(self) != len(other):
                raise ValueError('Vectors are not the same size')
            return Vector([self[i] * other[i] for i in range(len(self))])

    def __imul__(self, other):
        """Implements the multiplcation with in-place change

        Args:
            self (Vector) : input vector
            other (Vector/int) : input vector or input number
        Returns:
            self (Vector) : multiplation of 2 vectors or a vector by a number
        """
        if isinstance(other, int):
            return [self[i] * other for i in range(len(self))]
        elif isinstance(other, Vector):
            if len(self) != len(other):
                raise ValueError('Vectors are not the same size')
            for i, v in enumerate(other):
                self[i] *= v
            return self

    def dot(self, other):
        """Implements the dot product of 2 vectors

        Args:
            self, other (Vector) : input vector
        Returns:
            (int) : dot product of 2 vectors
        """
        if len(self) != len(other):
            raise ValueError('Vectors are not the same size')
        return Vector.dot_product(self, other)

    @staticmethod
    def dot_product(vec1, vec2):
        """Implements the dot product of 2 lists

        Args:
            vec1, vec2 (List[int]) : input list
        Returns:
            (int) : dot product of 2 lists
        """
        if len(vec1) != len(vec2):
            raise ValueError('Vectors are not the same size')
        return sum(vec1[i] * vec2[i] for i in range(len(vec1)))

    def __repr__(self):
        return '<Vector %r>' % self._vec

    def __str__(self):
        return self._vec
    # __str__ = __repr__
