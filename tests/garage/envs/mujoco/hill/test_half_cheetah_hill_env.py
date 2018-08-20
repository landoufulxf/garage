import pickle
import unittest

from garage.envs.mujoco.hill.half_cheetah_hill_env import HalfCheetahHillEnv


class TestHalfCheetahHillEnv(unittest.TestCase):

    def test_pickleable(self):
        env = HalfCheetahHillEnv(regen_terrain=False)
        round_trip = pickle.loads(pickle.dumps(env))
        assert round_trip
        assert round_trip.difficulty == env.difficulty

        round_trip.reset()
        for _ in range(10):
            _, _, done, _ = round_trip.step(round_trip.action_space.sample())
            round_trip.render()
            if done:
                break
        round_trip.close()
