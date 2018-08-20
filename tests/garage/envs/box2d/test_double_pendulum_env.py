import pickle
import unittest

from garage.envs.box2d.double_pendulum_env import DoublePendulumEnv


class TestDoublePendulumEnv(unittest.TestCase):

    def test_pickleable(self):
        obj = DoublePendulumEnv(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip
