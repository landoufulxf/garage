import pickle
import unittest

from nose.plugins import attrib
import numpy as np

from garage.contrib.ros.envs.sawyer.reacher_env import ReacherEnv


@attrib.attr("ros")
class TestReacherEnv(unittest.TestCase):

    def test_pickleable(self):
        initial_goal = np.array([1., 2., 3.])
        initial_joint_pos = np.array([1., 2.])
        obj = ReacherEnv(initial_goal, initial_joint_pos)
        round_trip = pickle.loads(pickle.dumps(env))
        assert round_trip
        assert round_trip.initial_goal == initial_goal
