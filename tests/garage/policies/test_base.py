import pickle
import unittest

import numpy as np

from garage.envs import EnvSpec
from garage.policies.base import Policy
from garage.policies.base import StochasticPolicy
from garage.spaces import Box


class TestPolicy(unittest.TestCase):

    def test_pickleable(self):
        env_spec = EnvSpec(
            Box(-1, 1, shape=(2)),
            Box(-1, 1, shape=(3)),
        )
        policy = Policy(env_spec)
        # Policy subclasses need to implement
        # Parameterized.get_params_internal()
        with self.assertRaises(NotImplementedError):
            round_trip = pickle.loads(pickle.dumps(policy))


class TestStochasticPolicy(unittest.TestCase):

    def test_pickleable(self):
        env_spec = EnvSpec(
            Box(-1, 1, shape=(2)),
            Box(-1, 1, shape=(3)),
        )
        policy = StochasticPolicy(env_spec)
        # StochasticPolicy subclasses need to implement
        # Parameterized.get_params_internal()
        with self.assertRaises(NotImplementedError):
            round_trip = pickle.loads(pickle.dumps(policy))
