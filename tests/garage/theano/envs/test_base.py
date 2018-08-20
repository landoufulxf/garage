import pickle
import unittest

from garage.theano.envs.base import TheanoEnv


class TestTheanoEnv(unittest.TestCase):

    def test_pickleable(self):
        obj = TheanoEnv(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip
