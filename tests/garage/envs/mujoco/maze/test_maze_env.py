import pickle
import unittest

from garage.envs.mujoco.maze.maze_env import MazeEnv


class TestMazeEnv(unittest.TestCase):

    def test_must_subclass(self):
        # MazeEnv needs to be subclassed and subclasses specify a model class
        with self.assertRaises(NotImplementedError):
            env = MazeEnv()
