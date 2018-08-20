import pickle
import unittest

from garage.envs.mujoco.sawyer.sawyer_env import Configuration
from garage.envs.mujoco.sawyer.sawyer_env import SawyerEnv
from garage.envs.mujoco.sawyer.sawyer_env import SawyerEnvWrapper
from garage.theano.envs import TheanoEnv
from garage.tf.envs.base import TfEnv
from nose2.tools import params


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
        assert obs["desired_goal"] == start_goal

        round_trip.reset()
        for _ in range(10):
            _, _, done, _ = round_trip.step(round_trip.action_space.sample())
            round_trip.render()
            if done:
                break
        round_trip.close()
    test_wrapped_pickleable.broken = True


class TestSawyerEnvWrapper(unittest.TestCase):

    @params(TheanoEnv, TfEnv)
    def test_wrapped_pickleable(self):
        env = wrapper_cls(
            SawyerEnvWrapper(
                SawyerEnv(start_goal_config)
            )
        )
        round_trip = pickle.loads(pickle.dumps(env))
        assert round_trip

        rount_trip.reset()
        for _ in range(10):
            _, _, done, _ = round_trip.step(round_trip.action_space.sample())
            round_trip.render()
            if done:
                break
        round_trip.close()
    test_wrapped_pickleable.broken = True
