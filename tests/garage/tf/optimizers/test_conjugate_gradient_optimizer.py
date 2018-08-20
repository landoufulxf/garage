import pickle
import unittest

from garage.tf.optimizers.conjugate_gradient_optimizer import ConjugateGradientOptimizer
from garage.tf.optimizers.conjugate_gradient_optimizer import FiniteDifferenceHvp
from garage.tf.optimizers.conjugate_gradient_optimizer import PerlmutterHvp


class TestConjugateGradientOptimizer(unittest.TestCase):

    def test_pickleable(self):
        obj = ConjugateGradientOptimizer(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip


class TestFiniteDifferenceHvp(unittest.TestCase):

    def test_pickleable(self):
        obj = FiniteDifferenceHvp(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip


class TestPerlmutterHvp(unittest.TestCase):

    def test_pickleable(self):
        obj = PerlmutterHvp(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip
