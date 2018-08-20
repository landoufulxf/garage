import pickle
import unittest

from garage.theano.algos.npo import NPO


class TestNPO(unittest.TestCase):

    def test_pickleable(self):
        obj = NPO(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip
