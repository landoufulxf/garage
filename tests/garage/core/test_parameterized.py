import pickle
import unittest

from garage.core.parameterized import Parameterized


class TestParameterized(unittest.TestCase):

    def test_pickleable(self):
        obj = Parameterized(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip
