import pickle
import unittest

from garage.algos.cma_es import CMAES
from tests.mock import PickleableMagicMock


class TestCMAES(unittest.TestCase):

    def test_pickleable(self):
        policy = PickleableMagicMock()
        env = PickleableMagicMock()
        cmaes = CMAES(env, policy, n_itr=1234)
        round_trip = pickle.loads(pickle.dumps(cmaes))
        assert round_trip
        assert round_trip.n_itr == cmaes.n_itr
