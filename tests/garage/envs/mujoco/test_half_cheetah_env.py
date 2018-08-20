import pickle
import unittest

from garage.envs.mujoco.half_cheetah_env import HalfCheetahEnv


class TestHalfCheetahEnv(unittest.TestCase):

    def test_pickleable(self):
        obj = HalfCheetahEnv(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip
