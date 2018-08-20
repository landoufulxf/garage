from garage.core import Serializable


class ExplorationStrategy(Serializable):
    def __init__(self):
        Serializable.quick_init(self, locals())

    def get_action(self, t, observation, policy, **kwargs):
        raise NotImplementedError

    def reset(self):
        pass
