import pickle
import unittest

from garage.theano.optimizers.hf import HfOptimizer
from garage.theano.optimizers.hf import SequenceDataset


class TestHfOptimizer(unittest.TestCase):

    def test_pickleable(self):
        obj = HfOptimizer(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip


class TestSequenceDataset(unittest.TestCase):

    def test_pickleable(self):
        obj = SequenceDataset(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip
