import pickle
import unittest

from garage.theano.sampler.replay_pool import ReplayPool


class TestReplayPool(unittest.TestCase):

    def test_pickleable(self):
        obj = ReplayPool(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip
