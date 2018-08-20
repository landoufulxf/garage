import pickle
import unittest

from garage.envs import EnvSpec
from garage.exploration_strategies.gaussian_strategy import GaussianStrategy
from garage.spaces import Box


class TestGaussianStrategy(unittest.TestCase):

    def test_pickleable(self):
        env_spec = EnvSpec(Box(-1., 1., shape=(2)), Box(-1., 1., shape=(1)))
        strategy = GaussianStrategy(env_spec)
        round_trip = pickle.loads(pickle.dumps(strategy))
        assert round_trip
        assert round_trip._action_space == strategy._action_space
