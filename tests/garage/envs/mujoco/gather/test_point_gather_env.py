import pickle
import unittest

from garage.envs.mujoco.gather.point_gather_env import PointGatherEnv


class TestPointGatherEnv(unittest.TestCase):

    def test_pickleable(self):
        env = PointGatherEnv(n_apples=1)
        round_trip = pickle.loads(pickle.dumps(env))
        assert round_trip
        assert round_trip.n_apples == env.n_apples

        round_trip.reset()
        for _ in range(10):
            _, _, done, _ = round_trip.step(round_trip.action_space.sample())
            round_trip.render()
            if done:
                break
        round_trip.close()
    test_pickleable.broken = True
