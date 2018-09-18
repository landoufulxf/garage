import pickle
import unittest

from nose2.tools import params

from garage.envs.mujoco.sawyer.reacher_env import ReacherEnv
from garage.theano.envs import TheanoEnv
from garage.tf.envs.base import TfEnv
from tests.helpers import step_env


class TestReacherEnv(unittest.TestCase):
    @params(TheanoEnv, TfEnv)
    def test_wrapped_pickleable(self, wrapper_cls):
        goal_position = [1., 2., 3.]
        env = wrapper_cls(ReacherEnv(goal_position))
        round_trip = pickle.loads(pickle.dumps(env))
        assert round_trip
        obs = round_trip.get_obs()
        assert obs["desired_goal"] == goal_position
        step_env(round_trip)

    test_wrapped_pickleable.broken = True
