import pickle
import unittest

from garage.theano.core.network import ConvNetwork
from garage.theano.core.network import GRULayer
from garage.theano.core.network import GRUNetwork
from garage.theano.core.network import GRUStepLayer
from garage.theano.core.network import MLP


class TestConvNetwork(unittest.TestCase):

    def test_pickleable(self):
        obj = ConvNetwork(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip


class TestGRULayer(unittest.TestCase):

    def test_pickleable(self):
        obj = GRULayer(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip


class TestGRUNetwork(unittest.TestCase):

    def test_pickleable(self):
        obj = GRUNetwork(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip


class TestGRUStepLayer(unittest.TestCase):

    def test_pickleable(self):
        obj = GRUStepLayer(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip


class TestMLP(unittest.TestCase):

    def test_pickleable(self):
        obj = MLP(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip
