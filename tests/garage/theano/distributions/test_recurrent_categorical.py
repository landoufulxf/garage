import pickle
import unittest

from garage.theano.distributions.recurrent_categorical import RecurrentCategorical


class TestRecurrentCategorical(unittest.TestCase):

    def test_pickleable(self):
        obj = RecurrentCategorical(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip
