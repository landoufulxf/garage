import pickle
import unittest

from garage.envs.box2d.car_parking_env import CarParkingEnv


class TestCarParkingEnv(unittest.TestCase):

    def test_pickleable(self):
        obj = CarParkingEnv(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip
