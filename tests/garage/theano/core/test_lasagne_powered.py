import pickle
import unittest

from garage.theano.core.lasagne_powered import LasagnePowered


class TestLasagnePowered(unittest.TestCase):

    def test_pickleable(self):
        obj = LasagnePowered(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip
