import pickle
import unittest

from garage.envs.identification_env import IdentificationEnv


class TestIdentificationEnv(unittest.TestCase):

    def test_pickleable(self):
        obj = IdentificationEnv(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip
