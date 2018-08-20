import pickle
import unittest

from garage.tf.envs.parallel_vec_env_executor import ParallelVecEnvExecutor


class TestParallelVecEnvExecutor(unittest.TestCase):

    def test_pickleable(self):
        obj = ParallelVecEnvExecutor(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip
