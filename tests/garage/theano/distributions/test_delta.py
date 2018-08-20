import pickle
import unittest

from garage.theano.distributions.delta import Delta


class TestDelta(unittest.TestCase):

    def test_pickleable(self):
        obj = Delta(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip
