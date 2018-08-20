import pickle
import unittest

from garage.envs.dm_control.dm_control_env import DmControlEnv


class TestDmControlEnv(unittest.TestCase):

    def test_pickleable(self):
        obj = DmControlEnv(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip
