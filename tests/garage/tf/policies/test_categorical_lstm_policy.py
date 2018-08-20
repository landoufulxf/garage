import pickle
import unittest

from garage.tf.policies.categorical_lstm_policy import CategoricalLSTMPolicy


class TestCategoricalLSTMPolicy(unittest.TestCase):

    def test_pickleable(self):
        obj = CategoricalLSTMPolicy(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip
