import pickle
import unittest

from garage.theano.regressors.gaussian_conv_regressor import GaussianConvRegressor


class TestGaussianConvRegressor(unittest.TestCase):

    def test_pickleable(self):
        obj = GaussianConvRegressor(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip
