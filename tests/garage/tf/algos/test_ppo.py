import pickle
import unittest

from garage.tf.algos.ppo import PPO


class TestPPO(unittest.TestCase):

    def test_pickleable(self):
        obj = PPO(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip
