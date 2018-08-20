import pickle
import unittest

from garage.tf.algos.vpg import VPG


class TestVPG(unittest.TestCase):

    def test_pickleable(self):
        obj = VPG(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip
