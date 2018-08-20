import pickle
import unittest

from garage.theano.optimizers.penalty_lbfgs_optimizer import PenaltyLbfgsOptimizer


class TestPenaltyLbfgsOptimizer(unittest.TestCase):

    def test_pickleable(self):
        obj = PenaltyLbfgsOptimizer(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip
