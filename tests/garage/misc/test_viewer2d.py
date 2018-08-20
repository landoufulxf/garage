import pickle
import unittest

from garage.misc.viewer2d import Colors
from garage.misc.viewer2d import Viewer2D


class TestColors(unittest.TestCase):

    def test_pickleable(self):
        obj = Colors(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip


class TestViewer2D(unittest.TestCase):

    def test_pickleable(self):
        obj = Viewer2D(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip
