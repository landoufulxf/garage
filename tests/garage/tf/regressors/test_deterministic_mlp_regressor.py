import pickle
import unittest

from garage.tf.regressors.deterministic_mlp_regressor import DeterministicMLPRegressor


class TestDeterministicMLPRegressor(unittest.TestCase):

    def test_pickleable(self):
        obj = DeterministicMLPRegressor(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip
