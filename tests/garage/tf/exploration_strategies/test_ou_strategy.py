import pickle
import unittest

from garage.tf.exploration_strategies.ou_strategy import OUStrategy


class TestOUStrategy(unittest.TestCase):

    def test_pickleable(self):
        obj = OUStrategy(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip
