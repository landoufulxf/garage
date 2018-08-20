import pickle
import unittest

from garage.envs.box2d.box2d_env import Box2DEnv


class TestBox2DEnv(unittest.TestCase):

    def test_pickleable(self):
        obj = Box2DEnv(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip
