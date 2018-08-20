import pickle
import unittest

from garage.tf.regressors.gaussian_mlp_regressor import GaussianMLPRegressor


class TestGaussianMLPRegressor(unittest.TestCase):

    def test_pickleable(self):
        obj = GaussianMLPRegressor(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip
