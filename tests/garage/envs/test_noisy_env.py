import pickle
import unittest

from garage.envs.noisy_env import DelayedActionEnv
from garage.envs.noisy_env import NoisyObservationEnv


class TestDelayedActionEnv(unittest.TestCase):

    def test_pickleable(self):
        obj = DelayedActionEnv(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip


class TestNoisyObservationEnv(unittest.TestCase):

    def test_pickleable(self):
        obj = NoisyObservationEnv(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip
