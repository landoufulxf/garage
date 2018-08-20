import pickle
import unittest

from garage.tf.policies.categorical_mlp_policy import CategoricalMLPPolicy


class TestCategoricalMLPPolicy(unittest.TestCase):

    def test_pickleable(self):
        obj = CategoricalMLPPolicy(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip
