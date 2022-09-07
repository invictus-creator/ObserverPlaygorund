from abc import ABCMeta, abstractmethod
from collections import defaultdict

class Event:
    def __init__(self):
        self.__eventhandlers = []

    def __iadd__(self, handler):
        self.__eventhandlers.append(handler)

    def __isub__(self, handler):
        self.__eventhandlers.remove(handler)

    def __call__(self, *args, **kwargs):
        for handler in self.__eventhandlers:
            handler(*args, **kwargs)


class IObservable(metaclass=ABCMeta):
    def __init__(self):
        self.__events = defaultdict(Event)

    def dispatch(self, name: str):
        self.__events[name]()

    def connect_to(self, name: str, event):
        self.__events[name] += event

    def unconnect_from(self, name: str, event):
        self.__events[name] -= event