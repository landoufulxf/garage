import pickle
import unittest

from nose2.tools import params

from garage.envs.mujoco.sawyer.sawyer_env import Configuration
from garage.envs.mujoco.sawyer.sawyer_env import SawyerEnv
from garage.envs.mujoco.sawyer.sawyer_env import SawyerEnvWrapper
from garage.theano.envs import TheanoEnv
from garage.tf.envs.base import TfEnv
from tests.helpers import step_env


def start_goal_config():
    start = Configuration(
        gripper_pos=[1., 2., 3.],
        gripper_state=1,
        object_grasped=False,
        object_pos=[0, 0, -1])
    goal = Configuration(
        gripper_pos=[4., 5., 6.],
        gripper_state=1,
        object_grasped=False,
        object_pos=[0, 0, -1])
    return start, goal


class TestSawyerEnv(unittest.TestCase):
    @params(TheanoEnv, TfEnv)
    def test_wrapped_pickleable(self, wrapper_cls):
        env = wrapper_cls(SawyerEnv(start_goal_config))
        round_trip = pickle.loads(pickle.dumps(env))
        assert round_trip
        obs = round_trip.get_obs()
        _, goal = start_goal_config()
        assert obs["desired_goal"] == goal
        step_env(round_trip)

    test_wrapped_pickleable.broken = True


class TestSawyerEnvWrapper(unittest.TestCase):
    @params(TheanoEnv, TfEnv)
    def test_wrapped_pickleable(self, wrapper_cls):
        env = wrapper_cls(SawyerEnvWrapper(SawyerEnv(start_goal_config)))
        round_trip = pickle.loads(pickle.dumps(env))
        assert round_trip
        step_env(round_trip)

    test_wrapped_pickleable.broken = True
