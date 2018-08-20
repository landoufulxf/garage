import pickle
import unittest

from garage.envs.box2d.parser.xml_attr_types import Angle
from garage.envs.box2d.parser.xml_attr_types import Bool
from garage.envs.box2d.parser.xml_attr_types import Choice
from garage.envs.box2d.parser.xml_attr_types import Either
from garage.envs.box2d.parser.xml_attr_types import Float
from garage.envs.box2d.parser.xml_attr_types import Hex
from garage.envs.box2d.parser.xml_attr_types import Int
from garage.envs.box2d.parser.xml_attr_types import List
from garage.envs.box2d.parser.xml_attr_types import String
from garage.envs.box2d.parser.xml_attr_types import Tuple
from garage.envs.box2d.parser.xml_attr_types import Type


class TestAngle(unittest.TestCase):

    def test_pickleable(self):
        obj = Angle(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip


class TestBool(unittest.TestCase):

    def test_pickleable(self):
        obj = Bool(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip


class TestChoice(unittest.TestCase):

    def test_pickleable(self):
        obj = Choice(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip


class TestEither(unittest.TestCase):

    def test_pickleable(self):
        obj = Either(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip


class TestFloat(unittest.TestCase):

    def test_pickleable(self):
        obj = Float(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip


class TestHex(unittest.TestCase):

    def test_pickleable(self):
        obj = Hex(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip


class TestInt(unittest.TestCase):

    def test_pickleable(self):
        obj = Int(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip


class TestList(unittest.TestCase):

    def test_pickleable(self):
        obj = List(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip


class TestString(unittest.TestCase):

    def test_pickleable(self):
        obj = String(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip


class TestTuple(unittest.TestCase):

    def test_pickleable(self):
        obj = Tuple(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip


class TestType(unittest.TestCase):

    def test_pickleable(self):
        obj = Type(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip
