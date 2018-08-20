import pickle
import unittest

from garage.regressors.product_regressor import ProductRegressor


class TestProductRegressor(unittest.TestCase):

    def test_pickleable(self):
        obj = ProductRegressor(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip
