import pickle
import unittest

from garage.theano.baselines.gaussian_conv_baseline import GaussianConvBaseline


class TestGaussianConvBaseline(unittest.TestCase):

    def test_pickleable(self):
        obj = GaussianConvBaseline(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip
