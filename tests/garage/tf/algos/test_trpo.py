import pickle
import unittest

from garage.tf.algos.trpo import KLConstraint
from garage.tf.algos.trpo import TRPO


class TestKLConstraint(unittest.TestCase):

    def test_pickleable(self):
        obj = KLConstraint(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip


class TestTRPO(unittest.TestCase):

    def test_pickleable(self):
        obj = TRPO(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip
