import pickle
import unittest

from garage.baselines.linear_feature_baseline import LinearFeatureBaseline


class TestLinearFeatureBaseline(unittest.TestCase):

    def test_pickleable(self):
        obj = LinearFeatureBaseline(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip
