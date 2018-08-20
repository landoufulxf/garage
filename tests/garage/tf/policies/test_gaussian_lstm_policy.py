import pickle
import unittest

from garage.tf.policies.gaussian_lstm_policy import GaussianLSTMPolicy


class TestGaussianLSTMPolicy(unittest.TestCase):

    def test_pickleable(self):
        obj = GaussianLSTMPolicy(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip
