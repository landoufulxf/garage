import pickle
import unittest

from garage.theano.policies.deterministic_mlp_policy import DeterministicMLPPolicy


class TestDeterministicMLPPolicy(unittest.TestCase):

    def test_pickleable(self):
        obj = DeterministicMLPPolicy(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip
