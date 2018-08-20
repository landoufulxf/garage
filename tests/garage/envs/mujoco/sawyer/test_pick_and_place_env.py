import pickle
import unittest

from garage.envs.mujoco.sawyer.pick_and_place_env import PickAndPlaceEnv
from garage.theano.envs import TheanoEnv
from garage.tf.envs.base import TfEnv
from nose2.tools import params


class TestPickAndPlaceEnv(unittest.TestCase):

    @params(TheanoEnv, TfEnv)
    def test_wrapped_pickleable(self, wrapper_cls):
        env = wrapper_cls(PickAndPlaceEnv())
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
