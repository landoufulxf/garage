import pickle
import unittest

from garage.envs.dm_control.dm_control_viewer import DmControlViewer


class TestDmControlViewer(unittest.TestCase):

    def test_pickleable(self):
        obj = DmControlViewer(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip
