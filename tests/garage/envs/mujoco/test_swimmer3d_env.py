import pickle
import unittest

from garage.envs.mujoco.swimmer3d_env import Swimmer3DEnv


class TestSwimmer3DEnv(unittest.TestCase):

    def test_pickleable(self):
        obj = Swimmer3DEnv(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip
