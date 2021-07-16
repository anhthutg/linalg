import random
from linalg.matrix import Matrix

# =============================================================================

def test_order():
    u = Matrix((3,3))
    assert Matrix.order(u) == (3,3)

    v = Matrix([[1, 2, 3], [4, 5, 6]])
    assert Matrix.order(v) == (2,3)

def test_index():
    L = [[random.randint(0, 10) for _ in range(3)] for _ in range(3)]
    u = Matrix(L)
    for i, (x, y) in enumerate(zip(u, L)):
        assert x == y

#     u[0][0] = -u[0][0]
#     assert u[0][0] == -L[0][0]

# def test_add():
#     L1 = [[random.randint(0, 10) for _ in range(3)] for _ in range(3)]
#     u = Matrix(L1)
#     L2 = [[random.randint(0, 10) for _ in range(3)] for _ in range(3)]
#     v = Matrix(L2)

#     s = u + v

#     for i, (x, y, z) in enumerate(zip(u, v, s)):
#         assert x + y == z