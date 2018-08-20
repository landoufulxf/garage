import pickle
import unittest

from garage.tf.distributions.base import Distribution


class TestDistribution(unittest.TestCase):

    def test_pickleable(self):
        obj = Distribution(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip
