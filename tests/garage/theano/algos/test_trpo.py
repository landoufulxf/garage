import pickle
import unittest

from garage.theano.algos.trpo import TRPO


class TestTRPO(unittest.TestCase):

    def test_pickleable(self):
        obj = TRPO(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip
