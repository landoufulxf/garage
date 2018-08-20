import pickle
import unittest

from garage.theano.algos.reps import REPS


class TestREPS(unittest.TestCase):

    def test_pickleable(self):
        obj = REPS(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip
