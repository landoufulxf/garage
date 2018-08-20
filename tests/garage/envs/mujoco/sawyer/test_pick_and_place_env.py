import pickle
import unittest

from nose2.tools import params

from garage.envs.mujoco.sawyer.pick_and_place_env import PickAndPlaceEnv
from garage.theano.envs import TheanoEnv
from garage.tf.envs.base import TfEnv
from tests.helpers import step_env


class TestPickAndPlaceEnv(unittest.TestCase):

    @params(TheanoEnv, TfEnv)
    def test_wrapped_pickleable(self, wrapper_cls):
        env = wrapper_cls(PickAndPlaceEnv())
        round_trip = pickle.loads(pickle.dumps(env))
        assert round_trip
        step_env(round_trip)
    test_wrapped_pickleable.broken = True
