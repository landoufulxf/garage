import pickle
import unittest

from garage.envs import EnvSpec
from garage.exploration_strategies.ou_strategy import OUStrategy
from garage.spaces import Box


class TestOUStrategy(unittest.TestCase):

    def test_pickleable(self):
        env_spec = EnvSpec(Box(-1., 1., shape=(2)), Box(-1., 1., shape=(1)))
        strategy = OUStrategy(env_spec)
        round_trip = pickle.loads(pickle.dumps(strategy))
        assert round_trip
        assert round_trip.action_space == strategy.action_space
