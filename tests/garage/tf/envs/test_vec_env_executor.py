import pickle
import unittest

from garage.tf.envs.vec_env_executor import VecEnvExecutor


class TestVecEnvExecutor(unittest.TestCase):

    def test_pickleable(self):
        obj = VecEnvExecutor(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip
