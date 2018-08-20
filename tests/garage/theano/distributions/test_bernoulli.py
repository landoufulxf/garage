import pickle
import unittest

from garage.theano.distributions.bernoulli import Bernoulli


class TestBernoulli(unittest.TestCase):

    def test_pickleable(self):
        obj = Bernoulli(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip
