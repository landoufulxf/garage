import pickle
import unittest

from garage.tf.policies.base import Policy
from garage.tf.policies.base import StochasticPolicy


class TestPolicy(unittest.TestCase):

    def test_pickleable(self):
        obj = Policy(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip


class TestStochasticPolicy(unittest.TestCase):

    def test_pickleable(self):
        obj = StochasticPolicy(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip
