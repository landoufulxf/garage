import pickle
import unittest

from garage.tf.q_functions.base import QFunction


class TestQFunction(unittest.TestCase):

    def test_pickleable(self):
        obj = QFunction(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip
