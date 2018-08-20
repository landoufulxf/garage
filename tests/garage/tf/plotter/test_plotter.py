import pickle
import unittest

from garage.tf.plotter.plotter import Op
from garage.tf.plotter.plotter import Plotter


class TestOp(unittest.TestCase):

    def test_pickleable(self):
        obj = Op(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip


class TestPlotter(unittest.TestCase):

    def test_pickleable(self):
        obj = Plotter(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip
