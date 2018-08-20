import pickle
import unittest

from garage.contrib.ros.envs.ros_env import RosEnv


class TestRosEnv(unittest.TestCase):

    def test_pickleable(self):
        ros_env = RosEnv(simulated=True)
        round_trip = pickle.loads(pickle.dumps(ros_env))
        assert round_trip
