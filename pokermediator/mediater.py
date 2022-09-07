from pokermediator.event import Event

class Mediator:
    def __init__(self):
        self.events = Event()

    def fire(self, args):
        self.events(args)