import pickle
import unittest

from garage.envs.box2d.parser.xml_types import AttrDecl
from garage.envs.box2d.parser.xml_types import XmlAttr
from garage.envs.box2d.parser.xml_types import XmlChild
from garage.envs.box2d.parser.xml_types import XmlChildren
from garage.envs.box2d.parser.xml_types import XmlElem


class TestAttrDecl(unittest.TestCase):

    def test_pickleable(self):
        obj = AttrDecl(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip


class TestXmlAttr(unittest.TestCase):

    def test_pickleable(self):
        obj = XmlAttr(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip


class TestXmlChild(unittest.TestCase):

    def test_pickleable(self):
        obj = XmlChild(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip


class TestXmlChildren(unittest.TestCase):

    def test_pickleable(self):
        obj = XmlChildren(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip


class TestXmlElem(unittest.TestCase):

    def test_pickleable(self):
        obj = XmlElem(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip
