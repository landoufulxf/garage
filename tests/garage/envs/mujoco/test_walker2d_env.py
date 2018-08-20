import pickle
import unittest

from garage.envs.mujoco.walker2d_env import Walker2DEnv


class TestWalker2DEnv(unittest.TestCase):

    def test_pickleable(self):
        env = Walker2DEnv(ctrl_cost_coeff=3.)
        round_trip = pickle.loads(pickle.dumps(env))
        assert round_trip
        assert round_trip.ctrl_cost_coeff == env.ctrl_cost_coeff

        round_trip.reset()
        for _ in range(10):
            _, _, done, _ = round_trip.step(round_trip.action_space.sample())
            round_trip.render()
            if done:
                break
        round_trip.close()
