import pickle
import unittest

from garage.tf.policies.uniform_control_policy import UniformControlPolicy


class TestUniformControlPolicy(unittest.TestCase):

    def test_pickleable(self):
        obj = UniformControlPolicy(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip
