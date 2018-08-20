import pickle
import unittest

from garage.envs.mujoco.swimmer_env import SwimmerEnv


class TestSwimmerEnv(unittest.TestCase):

    def test_pickleable(self):
        obj = SwimmerEnv(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip
