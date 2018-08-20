import pickle
import unittest

from garage.misc.ext import AttrDict
from garage.misc.ext import LazyDict


class TestAttrDict(unittest.TestCase):

    def test_pickleable(self):
        obj = AttrDict(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip


class TestLazyDict(unittest.TestCase):

    def test_pickleable(self):
        obj = LazyDict(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip
