import pickle
import unittest

from nose2.tools import params

from garage.envs.mujoco.sawyer.block_stacking_env import BlockStackingEnv
from garage.theano.envs import TheanoEnv
from garage.tf.envs.base import TfEnv
from tests.helpers import step_env


class TestBlockStackingEnv(unittest.TestCase):

    def test_pickleable(self):
        env = BlockStackingEnv()
        round_trip = pickle.loads(pickle.dumps(env))
        assert round_trip
        assert round_trip._green_bin_center == env._green_bin_center
        step_env(round_trip)
    test_pickleable.broken = True

    @params(TheanoEnv, TfEnv)
    def test_wrapped_pickleable(self, wrapper_cls):
        env = wrapper_cls(BlockStackingEnv())
        round_trip = pickle.loads(pickle.dumps(env))
        assert round_trip
        step_env(round_trip)
    test_wrapped_pickleable.broken = True
