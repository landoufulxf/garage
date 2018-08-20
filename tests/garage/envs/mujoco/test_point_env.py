import pickle
import unittest

from garage.envs.mujoco.point_env import PointEnv


class TestPointEnv(unittest.TestCase):

    def test_pickleable(self):
        obj = PointEnv(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip
