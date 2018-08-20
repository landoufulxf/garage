import pickle
import unittest

from garage.envs.box2d.cartpole_env import CartpoleEnv


class TestCartpoleEnv(unittest.TestCase):

    def test_pickleable(self):
        obj = CartpoleEnv(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip
