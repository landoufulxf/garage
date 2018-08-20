import pickle
import unittest

from garage.envs.box2d.mountain_car_env import MountainCarEnv


class TestMountainCarEnv(unittest.TestCase):

    def test_pickleable(self):
        obj = MountainCarEnv(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip
