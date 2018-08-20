import pickle
import unittest

from garage.baselines.base import Baseline


class TestBaseline(unittest.TestCase):

    def test_pickleable(self):
        obj = Baseline(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip
