import pickle
import unittest

from garage.envs.box2d.box2d_viewer import Box2DViewer
from garage.envs.box2d.box2d_viewer import PygameDraw


class TestBox2DViewer(unittest.TestCase):

    def test_pickleable(self):
        obj = Box2DViewer(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip


class TestPygameDraw(unittest.TestCase):

    def test_pickleable(self):
        obj = PygameDraw(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip
