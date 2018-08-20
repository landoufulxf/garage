import pickle
import unittest

from garage.exploration_strategies.base import ExplorationStrategy


class TestExplorationStrategy(unittest.TestCase):

    def test_pickleable(self):
        es = ExplorationStrategy()
        round_trip = pickle.loads(pickle.dumps(es))
        assert es
