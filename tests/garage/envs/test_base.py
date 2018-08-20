import pickle
import unittest

from garage.envs.base import GarageEnv


class TestGarageEnv(unittest.TestCase):

    def test_pickleable(self):
        obj = GarageEnv(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip
