import pickle
import unittest

from garage.tf.spaces.discrete import Discrete


class TestDiscrete(unittest.TestCase):

    def test_pickleable(self):
        obj = Discrete(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip
