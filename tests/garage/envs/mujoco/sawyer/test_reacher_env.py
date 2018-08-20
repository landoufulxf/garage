import pickle
import unittest

from garage.envs.mujoco.sawyer.reacher_env import ReacherEnv
from garage.theano.envs import TheanoEnv
from garage.tf.envs.base import TfEnv
from nose2.tools import params


class TestReacherEnv(unittest.TestCase):

    @params(TheanoEnv, TfEnv)
    def test_wrapped_pickleable(self, wrapper_cls):
        goal_position = [1., 2., 3.]
        env = wrapper_cls(ReacherEnv(goal_position))
        round_trip = pickle.loads(pickle.dumps(env))
        assert round_trip
        obs = round_trip.get_obs()
        assert obs["desired_goal"] == goal_position

        round_trip.reset()
        for _ in range(10):
            _, _, done, _ = round_trip.step(round_trip.action_space.sample())
            round_trip.render()
            if done:
                break
        round_trip.close()
    test_wrapped_pickleable.broken = True
