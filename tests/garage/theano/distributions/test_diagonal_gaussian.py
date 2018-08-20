import pickle
import unittest

from garage.theano.distributions.diagonal_gaussian import DiagonalGaussian


class TestDiagonalGaussian(unittest.TestCase):

    def test_pickleable(self):
        obj = DiagonalGaussian(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip
