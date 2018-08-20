import pickle
import unittest

from garage.theano.core.lasagne_layers import BatchNormLayer
from garage.theano.core.lasagne_layers import OpLayer
from garage.theano.core.lasagne_layers import ParamLayer


class TestBatchNormLayer(unittest.TestCase):

    def test_pickleable(self):
        obj = BatchNormLayer(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip


class TestOpLayer(unittest.TestCase):

    def test_pickleable(self):
        obj = OpLayer(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip


class TestParamLayer(unittest.TestCase):

    def test_pickleable(self):
        obj = ParamLayer(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip
