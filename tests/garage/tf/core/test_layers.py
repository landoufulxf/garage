import pickle
import unittest

from garage.tf.core.layers import BaseConvLayer
from garage.tf.core.layers import BatchNormLayer
from garage.tf.core.layers import ConcatLayer
from garage.tf.core.layers import Conv2DLayer
from garage.tf.core.layers import DenseLayer
from garage.tf.core.layers import DimshuffleLayer
from garage.tf.core.layers import DropoutLayer
from garage.tf.core.layers import ElemwiseSumLayer
from garage.tf.core.layers import FlattenLayer
from garage.tf.core.layers import G
from garage.tf.core.layers import GRULayer
from garage.tf.core.layers import GRUStepLayer
from garage.tf.core.layers import HeUniformInitializer
from garage.tf.core.layers import InputLayer
from garage.tf.core.layers import LSTMLayer
from garage.tf.core.layers import LSTMStepLayer
from garage.tf.core.layers import Layer
from garage.tf.core.layers import MergeLayer
from garage.tf.core.layers import NonlinearityLayer
from garage.tf.core.layers import OpLayer
from garage.tf.core.layers import OrthogonalInitializer
from garage.tf.core.layers import ParamLayer
from garage.tf.core.layers import Pool2DLayer
from garage.tf.core.layers import PseudoLSTMLayer
from garage.tf.core.layers import ReshapeLayer
from garage.tf.core.layers import SliceLayer
from garage.tf.core.layers import SpatialExpectedSoftmaxLayer
from garage.tf.core.layers import TfBasicLSTMLayer
from garage.tf.core.layers import TfGRULayer
from garage.tf.core.layers import XavierUniformInitializer


class TestBaseConvLayer(unittest.TestCase):

    def test_pickleable(self):
        obj = BaseConvLayer(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip


class TestBatchNormLayer(unittest.TestCase):

    def test_pickleable(self):
        obj = BatchNormLayer(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip


class TestConcatLayer(unittest.TestCase):

    def test_pickleable(self):
        obj = ConcatLayer(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip


class TestConv2DLayer(unittest.TestCase):

    def test_pickleable(self):
        obj = Conv2DLayer(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip


class TestDenseLayer(unittest.TestCase):

    def test_pickleable(self):
        obj = DenseLayer(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip


class TestDimshuffleLayer(unittest.TestCase):

    def test_pickleable(self):
        obj = DimshuffleLayer(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip


class TestDropoutLayer(unittest.TestCase):

    def test_pickleable(self):
        obj = DropoutLayer(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip


class TestElemwiseSumLayer(unittest.TestCase):

    def test_pickleable(self):
        obj = ElemwiseSumLayer(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip


class TestFlattenLayer(unittest.TestCase):

    def test_pickleable(self):
        obj = FlattenLayer(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip


class TestG(unittest.TestCase):

    def test_pickleable(self):
        obj = G(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip


class TestGRULayer(unittest.TestCase):

    def test_pickleable(self):
        obj = GRULayer(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip


class TestGRUStepLayer(unittest.TestCase):

    def test_pickleable(self):
        obj = GRUStepLayer(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip


class TestHeUniformInitializer(unittest.TestCase):

    def test_pickleable(self):
        obj = HeUniformInitializer(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip


class TestInputLayer(unittest.TestCase):

    def test_pickleable(self):
        obj = InputLayer(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip


class TestLSTMLayer(unittest.TestCase):

    def test_pickleable(self):
        obj = LSTMLayer(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip


class TestLSTMStepLayer(unittest.TestCase):

    def test_pickleable(self):
        obj = LSTMStepLayer(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip


class TestLayer(unittest.TestCase):

    def test_pickleable(self):
        obj = Layer(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip


class TestMergeLayer(unittest.TestCase):

    def test_pickleable(self):
        obj = MergeLayer(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip


class TestNonlinearityLayer(unittest.TestCase):

    def test_pickleable(self):
        obj = NonlinearityLayer(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip


class TestOpLayer(unittest.TestCase):

    def test_pickleable(self):
        obj = OpLayer(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip


class TestOrthogonalInitializer(unittest.TestCase):

    def test_pickleable(self):
        obj = OrthogonalInitializer(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip


class TestParamLayer(unittest.TestCase):

    def test_pickleable(self):
        obj = ParamLayer(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip


class TestPool2DLayer(unittest.TestCase):

    def test_pickleable(self):
        obj = Pool2DLayer(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip


class TestPseudoLSTMLayer(unittest.TestCase):

    def test_pickleable(self):
        obj = PseudoLSTMLayer(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip


class TestReshapeLayer(unittest.TestCase):

    def test_pickleable(self):
        obj = ReshapeLayer(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip


class TestSliceLayer(unittest.TestCase):

    def test_pickleable(self):
        obj = SliceLayer(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip


class TestSpatialExpectedSoftmaxLayer(unittest.TestCase):

    def test_pickleable(self):
        obj = SpatialExpectedSoftmaxLayer(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip


class TestTfBasicLSTMLayer(unittest.TestCase):

    def test_pickleable(self):
        obj = TfBasicLSTMLayer(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip


class TestTfGRULayer(unittest.TestCase):

    def test_pickleable(self):
        obj = TfGRULayer(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip


class TestXavierUniformInitializer(unittest.TestCase):

    def test_pickleable(self):
        obj = XavierUniformInitializer(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip
