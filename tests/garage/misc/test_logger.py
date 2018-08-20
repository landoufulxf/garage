import pickle
import unittest

from garage.misc.logger import MyEncoder
from garage.misc.logger import TerminalTablePrinter


class TestMyEncoder(unittest.TestCase):

    def test_pickleable(self):
        obj = MyEncoder(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip


class TestTerminalTablePrinter(unittest.TestCase):

    def test_pickleable(self):
        obj = TerminalTablePrinter(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip
