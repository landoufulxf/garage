import pickle
import unittest

import gym
from nose2.tools import params

from garage.theano.envs.base import TheanoEnv
from tests.helpers import step_env_with_gym_quirks


class TestTheanoEnv(unittest.TestCase):

    def test_pickleable(self):
        obj = TheanoEnv(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip

    @params(*list(gym.envs.registry.all()))
    def test_all_gym_envs(self, spec):
        env = TheanoEnv(spec.make())
        # TODO: make sure spaces are correctly converted
        step_env_with_gym_quirks(self, env, spec)

    @params(*list(gym.envs.registry.all()))
    def test_all_gym_envs_pickleable(self, spec):
        env = TheanoEnv(spec.make())
        round_trip = pickle.loads(pickle.dumps(envs))
        assert round_trip.env.spec == env.env.spec
        step_env_with_gym_quirks(self, round_trip, spec)
