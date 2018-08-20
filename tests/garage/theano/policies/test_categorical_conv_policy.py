import pickle
import unittest

from garage.theano.policies.categorical_conv_policy import CategoricalConvPolicy


class TestCategoricalConvPolicy(unittest.TestCase):

    def test_pickleable(self):
        obj = CategoricalConvPolicy(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip
