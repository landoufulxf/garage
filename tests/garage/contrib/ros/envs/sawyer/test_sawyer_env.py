import pickle
import unittest

from nose.plugins import attrib

from garage.contrib.ros.envs.sawyer.sawyer_env import SawyerEnv


@attrib.attr("ros")
class TestSawyerEnv(unittest.TestCase):

    def test_pickleable(self):
        env = SawyerEnv(True)
        round_trip = pickle.loads(pickle.dumps(env))
        assert round_trip
