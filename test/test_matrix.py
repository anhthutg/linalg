import random
from linalg.matrix import Matrix
from linalg.vector import Vector

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
    
    u[0][0] = -u[0][0]
    assert u[0][0] == -L[0][0]

def test_add():
    u = Matrix([[random.randint(0, 10) for _ in range(3)] for _ in range(3)])
    v = Matrix([[random.randint(0, 10) for _ in range(3)] for _ in range(3)])

    s = u + v

    for i, (x, y, z) in enumerate(zip(u, v, s)):
        assert Vector.__str__(Vector(x) + Vector(y)) == z

def test_iadd():
    L1 = [[random.randint(0, 10) for _ in range(3)] for _ in range(3)]
    L2 = [[random.randint(0, 10) for _ in range(3)] for _ in range(3)]
    
    u = Matrix(L1)
    v = Matrix(L2)

    u += v

    for i, (x, y, z) in enumerate(zip(u, L1, L2)):
        assert x == Vector.__str__(Vector(y) + Vector(z))

def test_mul():
    L1 = [[random.randint(0, 10) for _ in range(3)] for _ in range(3)]
    
    u = Matrix(L1)
    u_triple = u * 3

    for i, (x, y) in enumerate(zip(u_triple, L1)):
        assert x == Vector.__str__(Vector(y) * 3)

    u = Matrix(L1)
    L2 = [[random.randint(0, 10) for _ in range(3)] for _ in range(3)]
    v = Matrix(L2)

    prod = u * v
    for i, (p, x, y) in enumerate(zip(prod, L1, L2)):
        assert p == Vector.__str__(Vector(x) * Vector(y))

def test_imul():
    L1 = [[random.randint(0, 10) for _ in range(3)] for _ in range(3)]
    
    u = Matrix(L1)
    u *= 2
    for i, (x, y) in enumerate(zip(u, L1)):
        assert x == Vector.__str__(Vector(y) * 2)
    
    u = Matrix(L1)
    L2 = [[random.randint(0, 10) for _ in range(3)] for _ in range(3)]
    v = Matrix(L2)

    u *= v
    for i, (p, x, y) in enumerate(zip(u, L1, L2)):
        assert p == Vector.__str__(Vector(x) * Vector(y))

def test_dot():
    L1 = [[random.randint(0, 10) for _ in range(3)] for _ in range(3)]
    L2 = [[random.randint(0, 10) for _ in range(3)] for _ in range(3)]
     
    s1 = Matrix.dot_product(L1, L2)
    
    u = Matrix(L1)
    v = Matrix(L2)
    
    s2 = Matrix.dot(u, v)
    
    assert Matrix.__str__(s2) == s1

def test_transpose():
    L = [[random.randint(0, 10) for _ in range(3)] for _ in range(3)]
    u = Matrix(L)

    t1 = Matrix.transpose(u)
    # t2 = [[L[j][i] for j in range(len(L[0]))] for i in range(len(L))]
    t2 = list(map(list, zip(*L)))

    assert Matrix.__str__(t1) == t2

# =============================================================================