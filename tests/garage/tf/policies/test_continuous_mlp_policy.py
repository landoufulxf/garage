import pickle
import unittest

from garage.tf.policies.continuous_mlp_policy import ContinuousMLPPolicy


class TestContinuousMLPPolicy(unittest.TestCase):

    def test_pickleable(self):
        obj = ContinuousMLPPolicy(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip
