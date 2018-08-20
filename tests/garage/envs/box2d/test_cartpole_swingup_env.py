import pickle
import unittest

from garage.envs.box2d.cartpole_swingup_env import CartpoleSwingupEnv


class TestCartpoleSwingupEnv(unittest.TestCase):

    def test_pickleable(self):
        obj = CartpoleSwingupEnv(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip
