import pickle
import unittest

from garage.tf.core.parameterized import JointParameterized
from garage.tf.core.parameterized import Parameterized


class TestJointParameterized(unittest.TestCase):

    def test_pickleable(self):
        obj = JointParameterized(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip


class TestParameterized(unittest.TestCase):

    def test_pickleable(self):
        obj = Parameterized(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip
