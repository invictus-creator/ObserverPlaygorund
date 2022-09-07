"Each component stays synchronized through a mediator"
from interface_component import IComponent

class GameObserver(IComponent):
    "Each component stays synchronized through a mediator"

    def __init__(self, mediator, name):
        self._mediator = mediator
        self._name = name

    def observe_hole_cards(self):
        found_card = int(input("is there hole card (0 or 1): "))
        # when card is found update hero state

    def notify(self, message):
        print(self._name + ": >>> Out >>> : " + message)
        self._mediator.notify(message, self)

    def receive(self, message):
        print(self._name + ": <<< In <<< : " + message)
