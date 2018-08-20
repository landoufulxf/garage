import pickle
import unittest

from garage.tf.samplers.vectorized_sampler import VectorizedSampler


class TestVectorizedSampler(unittest.TestCase):

    def test_pickleable(self):
        obj = VectorizedSampler(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip
