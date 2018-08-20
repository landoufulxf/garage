import pickle
import unittest

from garage.viskit.core import Selector


class TestSelector(unittest.TestCase):

    def test_pickleable(self):
        obj = Selector(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip
