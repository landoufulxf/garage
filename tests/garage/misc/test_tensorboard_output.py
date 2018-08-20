import pickle
import unittest

from garage.misc.tensorboard_output import TensorBoardOutput


class TestTensorBoardOutput(unittest.TestCase):

    def test_pickleable(self):
        obj = TensorBoardOutput(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip
