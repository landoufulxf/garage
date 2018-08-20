import pickle
import unittest

from garage.algos.cem import CEM
from tests.mock import PickleableMagicMock


class TestCEM(unittest.TestCase):

    def test_pickleable(self):
        policy = PickleableMagicMock()
        env = PickleableMagicMock()
        cem = CEM(policy, env, n_itr=1234)
        round_trip = pickle.loads(pickle.dumps(cem))
        assert round_trip
        assert cem.n_itr == round_trip.n_itr
