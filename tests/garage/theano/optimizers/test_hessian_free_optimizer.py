import pickle
import unittest

from garage.theano.optimizers.hessian_free_optimizer import HessianFreeOptimizer


class TestHessianFreeOptimizer(unittest.TestCase):

    def test_pickleable(self):
        obj = HessianFreeOptimizer(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip
