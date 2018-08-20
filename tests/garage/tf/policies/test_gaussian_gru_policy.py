import pickle
import unittest

from garage.tf.policies.gaussian_gru_policy import GaussianGRUPolicy


class TestGaussianGRUPolicy(unittest.TestCase):

    def test_pickleable(self):
        obj = GaussianGRUPolicy(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip
