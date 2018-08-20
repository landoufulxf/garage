import pickle
import unittest

from garage.tf.core.network import ConvMergeNetwork
from garage.tf.core.network import ConvNetwork
from garage.tf.core.network import GRUNetwork
from garage.tf.core.network import LSTMNetwork
from garage.tf.core.network import MLP


class TestConvMergeNetwork(unittest.TestCase):

    def test_pickleable(self):
        obj = ConvMergeNetwork(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip


class TestConvNetwork(unittest.TestCase):

    def test_pickleable(self):
        obj = ConvNetwork(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip


class TestGRUNetwork(unittest.TestCase):

    def test_pickleable(self):
        obj = GRUNetwork(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip


class TestLSTMNetwork(unittest.TestCase):

    def test_pickleable(self):
        obj = LSTMNetwork(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip


class TestMLP(unittest.TestCase):

    def test_pickleable(self):
        obj = MLP(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip
