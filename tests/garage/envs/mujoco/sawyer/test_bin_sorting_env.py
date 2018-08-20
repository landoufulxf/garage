import pickle
import unittest

from nose2.tools import params

from garage.envs.mujoco.sawyer.bin_sorting_env import BinSortingEnv
from garage.theano.envs import TheanoEnv
from garage.tf.envs.base import TfEnv
from tests.helpers import step_env


class TestBinSortingEnv(unittest.TestCase):

    def test_pickleable(self):
        env = BinSortingEnv()
        round_trip = pickle.loads(pickle.dumps(env))
        assert round_trip
        assert round_trip._green_bin_center == env._green_bin_center
        step_env(round_trip)
    test_pickleable.broken = True

    @params(TheanoEnv, TfEnv)
    def test_wrapped_pickleable(self, wrapper_cls):
        env = wrapper_cls(BinSortingEnv())
        round_trip = pickle.loads(pickle.dumps(env))
        assert round_trip
        step_env(round_trip)
    test_wrapped_pickleable.broken = True
