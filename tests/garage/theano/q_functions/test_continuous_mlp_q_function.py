import pickle
import unittest

from garage.theano.q_functions.continuous_mlp_q_function import ContinuousMLPQFunction


class TestContinuousMLPQFunction(unittest.TestCase):

    def test_pickleable(self):
        obj = ContinuousMLPQFunction(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip
