import pickle
import unittest

from garage.misc.nb_utils import Experiment
from garage.misc.nb_utils import ExperimentDatabase


class TestExperiment(unittest.TestCase):

    def test_pickleable(self):
        obj = Experiment(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip


class TestExperimentDatabase(unittest.TestCase):

    def test_pickleable(self):
        obj = ExperimentDatabase(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip
