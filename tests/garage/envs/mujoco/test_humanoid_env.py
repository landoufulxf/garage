import pickle
import unittest

from garage.envs.mujoco.humanoid_env import HumanoidEnv


class TestHumanoidEnv(unittest.TestCase):

    def test_pickleable(self):
        obj = HumanoidEnv(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip
