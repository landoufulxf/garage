import pickle
import unittest

from garage.theano.baselines.gaussian_mlp_baseline import GaussianMLPBaseline


class TestGaussianMLPBaseline(unittest.TestCase):

    def test_pickleable(self):
        obj = GaussianMLPBaseline(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip
