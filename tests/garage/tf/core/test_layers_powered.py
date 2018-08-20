import pickle
import unittest

from garage.tf.core.layers_powered import LayersPowered


class TestLayersPowered(unittest.TestCase):

    def test_pickleable(self):
        obj = LayersPowered(*args, **kwargs)
        round_trip = pickle.loads(pickle.dumps(obj))
        assert round_trip
