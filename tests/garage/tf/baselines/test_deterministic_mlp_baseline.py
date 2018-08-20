import pickle
import unittest

from garage.tf.baselines.deterministic_mlp_baseline import DeterministicMLPBaseline


class TestDeterministicMLPBaseline(unittest.TestCase):

    def test_pickleable(self):
        obj = DeterministicMLPBaseline(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip
