import random
from linalg.vector import Vector

# =============================================================================

def test_len():
    u = Vector(5)
    assert len(u) == 5

    v = Vector([1, 2, 3])
    assert len(v) == 3

def test_index():
    L = [random.randint(0, 10) for _ in range(5)]
    u = Vector(L)
    for i, (x, y) in enumerate(zip(u, L)):
        assert x == y

    u[0] = -u[0]
    assert u[0] == -L[0]

def test_add():
    u = Vector([random.randint(0, 10) for _ in range(5)])
    v = Vector([random.randint(0, 10) for _ in range(5)])

    s = u + v

    for i, (x, y, z) in enumerate(zip(u, v, s)):
        assert x + y == z

def test_iadd():
    L1 = [random.randint(0, 10) for _ in range(5)]
    L2 = [random.randint(0, 10) for _ in range(5)]
    
    u = Vector(L1)
    v = Vector(L2)

    u += v
    for i, (x, y, z) in enumerate(zip(u, L1, L2)):
        assert x == y + z

def test_mul():
    L1 = [random.randint(0, 10) for _ in range(5)]

    u = Vector(L1)
    u_triple = u * 3
    for i, (x, y) in enumerate(zip(u_triple, L1)):
        assert x == y * 3

    u = Vector(L1)
    L2 = [random.randint(0, 10) for _ in range(5)]
    v = Vector(L2)

    prod = u * v
    for i, (p, x, y) in enumerate(zip(prod, L1, L2)):
        assert p == x * y

def test_imul():
    L1 = [random.randint(0, 10) for _ in range(5)]
    
    u = Vector(L1)
    u *= 2
    for i, (x, y) in enumerate(zip(u, L1)):
        assert x == y * 2
    
    u = Vector(L1)
    L2 = [random.randint(0, 10) for _ in range(5)]
    v = Vector(L2)

    u *= v
    for i, (p, x, y) in enumerate(zip(u, L1, L2)):
        assert p == x * y

def test_dot():
    L1 = [random.randint(0, 10) for _ in range(5)]
    L2 = [random.randint(0, 10) for _ in range(5)]

    u = Vector(L1)
    v = Vector(L2)

    assert Vector.dot(u, v) == Vector.dot_product(L1, L2)
# =============================================================================
