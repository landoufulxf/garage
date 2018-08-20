import pickle
import unittest

from garage.envs.sliding_mem_env import SlidingMemEnv


class TestSlidingMemEnv(unittest.TestCase):

    def test_pickleable(self):
        obj = SlidingMemEnv(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip
