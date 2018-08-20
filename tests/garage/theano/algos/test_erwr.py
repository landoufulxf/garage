import pickle
import unittest

from garage.theano.algos.erwr import ERWR


class TestERWR(unittest.TestCase):

    def test_pickleable(self):
        obj = ERWR(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip
