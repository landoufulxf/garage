import pickle
import unittest

from garage.envs.grid_world_env import GridWorldEnv


class TestGridWorldEnv(unittest.TestCase):

    def test_pickleable(self):
        obj = GridWorldEnv(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip
