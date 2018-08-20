import pickle
import unittest

from garage.tf.algos.ddpg import DDPG


class TestDDPG(unittest.TestCase):

    def test_pickleable(self):
        obj = DDPG(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip
