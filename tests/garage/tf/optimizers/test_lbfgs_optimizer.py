import pickle
import unittest

from garage.tf.optimizers.lbfgs_optimizer import LbfgsOptimizer


class TestLbfgsOptimizer(unittest.TestCase):

    def test_pickleable(self):
        obj = LbfgsOptimizer(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip
