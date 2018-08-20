import pickle
import unittest

from garage.tf.envs.base import TfEnv
from garage.tf.envs.base import VecTfEnv
from garage.tf.envs.base import WrappedCls


class TestTfEnv(unittest.TestCase):

    def test_pickleable(self):
        obj = TfEnv(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip


class TestVecTfEnv(unittest.TestCase):

    def test_pickleable(self):
        obj = VecTfEnv(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip


class TestWrappedCls(unittest.TestCase):

    def test_pickleable(self):
        obj = WrappedCls(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip
