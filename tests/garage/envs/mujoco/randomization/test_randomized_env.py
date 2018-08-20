import pickle
import unittest

from garage.envs.mujoco import SwimmerEnv
from garage.envs.mujoco.randomization import Distribution
from garage.envs.mujoco.randomization import Method
from garage.envs.mujoco.randomization import randomize
from garage.envs.mujoco.randomization import Variations


class TestRandomizedEnv(unittest.TestCase):

    def test_pickleable(self):
        variations = Variations()
        variations.randomize() \
                .at_xpath(".//geom[@name='torso']") \
                .attribute("density") \
                .with_method(Method.COEFFICIENT) \
                .sampled_from(Distribution.UNIFORM) \
                .with_range(0.5, 1.5) \
                .add()

        env = randomize(SwimmerEnv(), variations)

        round_trip = pickle.loads(pickle.dumps(env))
        assert round_trip
        assert round_trip._variations == env._variations

        for _ in range(5):
            round_trip.reset()
            for _ in range(10):
                _, _, done, _ = round_trip.step(
                    round_trip.action_space.sample())
                round_trip.render()
                if done:
                    break
            round_trip.close()

    test_pickleable.broken = True

