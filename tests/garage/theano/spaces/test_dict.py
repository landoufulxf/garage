import pickle
import unittest

from garage.theano.spaces.dict import Dict


class TestDict(unittest.TestCase):

    def test_pickleable(self):
        obj = Dict(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip
