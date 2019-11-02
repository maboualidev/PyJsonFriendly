from abc import ABCMeta, abstractmethod
from json import JSONEncoder


class JsonFriendly(metaclass=ABCMeta):
    JSONEncoder.default = lambda self, obj: getattr(obj.__class__, "_as_json_friendly_obj", JSONEncoder.default)(obj)

    @abstractmethod
    def _as_json_friendly_obj(self):
        pass
