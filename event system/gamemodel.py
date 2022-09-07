from event import IObservable, Event


class GameModel(IObservable):
    def __init__(self):
        super(GameModel, self).__init__()
        self.ask_update = Event()

    def on_ask_update(self):
        print("ask for update")