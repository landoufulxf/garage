import pickle
import unittest

from garage.envs.mujoco.inverted_double_pendulum_env import InvertedDoublePendulumEnv


class TestInvertedDoublePendulumEnv(unittest.TestCase):

    def test_pickleable(self):
        obj = InvertedDoublePendulumEnv(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip
