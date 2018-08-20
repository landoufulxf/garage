import pickle
import unittest

from garage.theano.algos.tnpg import TNPG


class TestTNPG(unittest.TestCase):

    def test_pickleable(self):
        obj = TNPG(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip
