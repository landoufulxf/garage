import pickle
import unittest

from garage.theano.spaces.product import Product


class TestProduct(unittest.TestCase):

    def test_pickleable(self):
        obj = Product(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip
