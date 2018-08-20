import pickle
import unittest

from garage.tf.optimizers.first_order_optimizer import FirstOrderOptimizer


class TestFirstOrderOptimizer(unittest.TestCase):

    def test_pickleable(self):
        obj = FirstOrderOptimizer(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip
