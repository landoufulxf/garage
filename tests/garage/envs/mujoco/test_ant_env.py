import pickle
import unittest

from garage.envs.mujoco.ant_env import AntEnv


class TestAntEnv(unittest.TestCase):

    def test_pickleable(self):
        obj = AntEnv(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip
