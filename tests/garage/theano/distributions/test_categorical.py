import pickle
import unittest

from garage.theano.distributions.categorical import Categorical


class TestCategorical(unittest.TestCase):

    def test_pickleable(self):
        obj = Categorical(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip
