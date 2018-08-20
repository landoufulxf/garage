import pickle
import unittest

from garage.baselines.zero_baseline import ZeroBaseline


class TestZeroBaseline(unittest.TestCase):

    def test_pickleable(self):
        obj = ZeroBaseline(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip
