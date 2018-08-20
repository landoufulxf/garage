import pickle
import unittest

from garage.envs.mujoco.mujoco_env import MujocoEnv


class TestMujocoEnv(unittest.TestCase):

    def test_pickleable(self):
        obj = MujocoEnv(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip
