import pickle
import unittest

from garage.envs.mujoco.sawyer.block_stacking_env import BlockStackingEnv
from garage.theano.envs import TheanoEnv
from garage.tf.envs.base import TfEnv
from nose2.tools import params


class TestBlockStackingEnv(unittest.TestCase):

    def test_pickleable(self):
        env = BlockStackingEnv()
        round_trip = pickle.loads(pickle.dumps(env))
        assert round_trip
        assert round_trip._green_bin_center == env._green_bin_center

        round_trip.reset()
        for _ in range(10):
            _, _, done, _ = round_trip.step(round_trip.action_space.sample())
            round_trip.render()
            if done:
                break
        round_trip.close()
    test_pickleable.broken = True

    @params(TheanoEnv, TfEnv)
    def test_wrapped_pickleable(self, wrapper_cls):
        env = wrapper_cls(BlockStackingEnv())
        round_trip = pickle.loads(pickle.dumps(env))
        assert round_trip

        round_trip.reset()
        for _ in range(10):
            _, _, done, _ = round_trip.step(round_trip.action_space.sample())
            round_trip.render()
            if done:
                break
        round_trip.close()
    test_wrapped_pickleable.broken = True
