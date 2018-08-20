import pickle
import unittest

from garage.envs.env_spec import EnvSpec


class TestEnvSpec(unittest.TestCase):

    def test_pickleable(self):
        obj = EnvSpec(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip
