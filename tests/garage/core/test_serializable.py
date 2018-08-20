import pickle
import unittest

from garage.core.serializable import Serializable


class TestSerializable(unittest.TestCase):

    def test_pickleable(self):
        obj = Serializable(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip
