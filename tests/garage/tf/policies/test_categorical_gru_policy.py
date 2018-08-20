import pickle
import unittest

from garage.tf.policies.categorical_gru_policy import CategoricalGRUPolicy


class TestCategoricalGRUPolicy(unittest.TestCase):

    def test_pickleable(self):
        obj = CategoricalGRUPolicy(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip
