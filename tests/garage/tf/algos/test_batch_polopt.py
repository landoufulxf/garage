import pickle
import unittest

from garage.tf.algos.batch_polopt import BatchPolopt


class TestBatchPolopt(unittest.TestCase):

    def test_pickleable(self):
        obj = BatchPolopt(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip
