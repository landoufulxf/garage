import pickle
import unittest

from garage.misc.instrument import BinaryOp
from garage.misc.instrument import StubAttr
from garage.misc.instrument import StubBase
from garage.misc.instrument import StubClass
from garage.misc.instrument import StubMethodCall
from garage.misc.instrument import StubObject
from garage.misc.instrument import VariantDict
from garage.misc.instrument import VariantGenerator


class TestBinaryOp(unittest.TestCase):

    def test_pickleable(self):
        obj = BinaryOp(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip


class TestStubAttr(unittest.TestCase):

    def test_pickleable(self):
        obj = StubAttr(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip


class TestStubBase(unittest.TestCase):

    def test_pickleable(self):
        obj = StubBase(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip


class TestStubClass(unittest.TestCase):

    def test_pickleable(self):
        obj = StubClass(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip


class TestStubMethodCall(unittest.TestCase):

    def test_pickleable(self):
        obj = StubMethodCall(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip


class TestStubObject(unittest.TestCase):

    def test_pickleable(self):
        obj = StubObject(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip


class TestVariantDict(unittest.TestCase):

    def test_pickleable(self):
        obj = VariantDict(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip


class TestVariantGenerator(unittest.TestCase):

    def test_pickleable(self):
        obj = VariantGenerator(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip
