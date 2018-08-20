import pickle
import unittest

from garage.envs.mujoco.simple_humanoid_env import SimpleHumanoidEnv


class TestSimpleHumanoidEnv(unittest.TestCase):

    def test_pickleable(self):
        obj = SimpleHumanoidEnv(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip
