import pickle
import unittest

import gym
from nose2.tools import params

from garage.tf.envs.base import TfEnv
from garage.tf.envs.base import VecTfEnv
from garage.tf.envs.base import WrappedCls
from tests.helpers import step_env_with_gym_quirks


class TestTfEnv(unittest.TestCase):

    def test_pickleable(self):
        obj = TfEnv(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip

    @params(*list(gym.envs.registry.all()))
    def test_all_gym_envs(self, spec):
        env = TfEnv(spec.make())
        # TODO: make sure spaces are converted correctly
        step_env_with_gym_quirks(self, env, spec)

    @params(*list(gym.envs.registry.all()))
    def test_all_gym_envs_pickleable(self, spec):
        env = TfEnv(spec.make())
        round_trip = pickle.loads(pickle.dumps(envs))
        assert round_trip.env.spec == env.env.spec
        step_env_with_gym_quirks(self, round_trip, spec)


class TestVecTfEnv(unittest.TestCase):

    def test_pickleable(self):
        obj = VecTfEnv(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip


class TestWrappedCls(unittest.TestCase):

    def test_pickleable(self):
        obj = WrappedCls(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip
