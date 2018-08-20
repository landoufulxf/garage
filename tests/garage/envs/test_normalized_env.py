import pickle
import unittest

from garage.envs.normalized_env import NormalizedEnv


class TestNormalizedEnv(unittest.TestCase):

    def test_pickleable(self):
        obj = NormalizedEnv(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip
