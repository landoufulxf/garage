import pickle
import unittest

from garage.envs.mujoco.hopper_env import HopperEnv


class TestHopperEnv(unittest.TestCase):

    def test_pickleable(self):
        obj = HopperEnv(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip
