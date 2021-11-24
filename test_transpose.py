import numpy as np
from random import randint
from op_v2 import Matrix
import unittest

def test_transpose_square():
    for i in range(100):
        m = Matrix(i, i, [randint(-10, 10)] for _ in range(i * i))
        m2 = np.array(m.values)
        assert m.transpose().values == m2.transpose().tolist()
