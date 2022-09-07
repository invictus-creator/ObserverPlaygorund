"Each component stays synchronized through a mediator"
from interface_component import IComponent
from doctor.event.events import Event

class Component(IComponent):
    "Each component stays synchronized through a mediator"

    def __init__(self, mediator, name):
        self._mediator = mediator
        self._name = name
        self.falls_ill = Event()

    def notify(self, message):
        print(self._name + ": >>> Out >>> : " + message)
        self._mediator.notify(message, self)

    def receive(self, message):
        print(self._name + ": <<< In <<< : " + message)

    def catchs_a_cold(self):
        self.falls_ill(self._name)