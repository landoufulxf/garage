import pickle
import unittest

from garage.envs.occlusion_env import OcclusionEnv


class TestOcclusionEnv(unittest.TestCase):

    def test_pickleable(self):
        obj = OcclusionEnv(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip
