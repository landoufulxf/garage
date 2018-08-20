import pickle
import unittest

from nose.plugins import attrib
import numpy as np

from garage.contrib.ros.envs.sawyer.pick_and_place_env import PickAndPlaceEnv


@attrib("ros")
class TestPickAndPlaceEnv(unittest.TestCase):

    def test_pickleable(self):
        initial_goal = np.array([1., 2.])
        initial_joint_pos = np.array([1., 2., 3.])
        env = PickAndPlaceEnv(initial_goal, initial_joint_pos)
        round_trip = pickle.loads(pickle.dumps(env))
        assert round_trip
        assert rount_trip.initial_goal == initial_goal
