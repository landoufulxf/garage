import pickle
import unittest

from garage.tf.samplers.batch_sampler import BatchSampler


class TestBatchSampler(unittest.TestCase):

    def test_pickleable(self):
        obj = BatchSampler(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip
