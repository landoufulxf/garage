import pickle
import unittest

from garage.tf.regressors.bernoulli_mlp_regressor import BernoulliMLPRegressor


class TestBernoulliMLPRegressor(unittest.TestCase):

    def test_pickleable(self):
        obj = BernoulliMLPRegressor(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip
