import pickle
import unittest

from garage.envs.box2d.parser.xml_box2d import ExtraData
from garage.envs.box2d.parser.xml_box2d import Meta
from garage.envs.box2d.parser.xml_box2d import Meta
from garage.envs.box2d.parser.xml_box2d import Meta
from garage.envs.box2d.parser.xml_box2d import Meta
from garage.envs.box2d.parser.xml_box2d import Meta
from garage.envs.box2d.parser.xml_box2d import Meta
from garage.envs.box2d.parser.xml_box2d import Meta
from garage.envs.box2d.parser.xml_box2d import XmlBody
from garage.envs.box2d.parser.xml_box2d import XmlBox2D
from garage.envs.box2d.parser.xml_box2d import XmlControl
from garage.envs.box2d.parser.xml_box2d import XmlFixture
from garage.envs.box2d.parser.xml_box2d import XmlJoint
from garage.envs.box2d.parser.xml_box2d import XmlState
from garage.envs.box2d.parser.xml_box2d import XmlWorld


class TestExtraData(unittest.TestCase):

    def test_pickleable(self):
        obj = ExtraData(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip


class TestMeta(unittest.TestCase):

    def test_pickleable(self):
        obj = Meta(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip


class TestMeta(unittest.TestCase):

    def test_pickleable(self):
        obj = Meta(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip


class TestMeta(unittest.TestCase):

    def test_pickleable(self):
        obj = Meta(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip


class TestMeta(unittest.TestCase):

    def test_pickleable(self):
        obj = Meta(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip


class TestMeta(unittest.TestCase):

    def test_pickleable(self):
        obj = Meta(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip


class TestMeta(unittest.TestCase):

    def test_pickleable(self):
        obj = Meta(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip


class TestMeta(unittest.TestCase):

    def test_pickleable(self):
        obj = Meta(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip


class TestXmlBody(unittest.TestCase):

    def test_pickleable(self):
        obj = XmlBody(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip


class TestXmlBox2D(unittest.TestCase):

    def test_pickleable(self):
        obj = XmlBox2D(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip


class TestXmlControl(unittest.TestCase):

    def test_pickleable(self):
        obj = XmlControl(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip


class TestXmlFixture(unittest.TestCase):

    def test_pickleable(self):
        obj = XmlFixture(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip


class TestXmlJoint(unittest.TestCase):

    def test_pickleable(self):
        obj = XmlJoint(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip


class TestXmlState(unittest.TestCase):

    def test_pickleable(self):
        obj = XmlState(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip


class TestXmlWorld(unittest.TestCase):

    def test_pickleable(self):
        obj = XmlWorld(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip
