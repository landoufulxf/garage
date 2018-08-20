import pickle
import unittest

from garage.misc.console import Message
from garage.misc.console import SimpleMessage


class TestMessage(unittest.TestCase):

    def test_pickleable(self):
        obj = Message(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip


class TestSimpleMessage(unittest.TestCase):

    def test_pickleable(self):
        obj = SimpleMessage(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip
