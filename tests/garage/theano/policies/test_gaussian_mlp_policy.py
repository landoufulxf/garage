import pickle
import unittest

from garage.theano.policies.gaussian_mlp_policy import GaussianMLPPolicy


class TestGaussianMLPPolicy(unittest.TestCase):

    def test_pickleable(self):
        obj = GaussianMLPPolicy(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip
