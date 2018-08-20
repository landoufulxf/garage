import pickle
import unittest

from garage.tf.regressors.categorical_mlp_regressor import CategoricalMLPRegressor


class TestCategoricalMLPRegressor(unittest.TestCase):

    def test_pickleable(self):
        obj = CategoricalMLPRegressor(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip
