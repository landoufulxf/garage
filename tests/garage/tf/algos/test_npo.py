import pickle
import unittest

from garage.tf.algos.npo import NPO
from garage.tf.algos.npo import PGLoss


class TestNPO(unittest.TestCase):

    def test_pickleable(self):
        obj = NPO(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip


class TestPGLoss(unittest.TestCase):

    def test_pickleable(self):
        obj = PGLoss(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip
