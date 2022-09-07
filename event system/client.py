from gamecontroller import GameController
from gamemodel import GameModel


controller = GameController()
model = GameModel()

model.connect_to('ask_update', controller.send_update)
model.connect_to('ask_update', model.on_ask_update)

model.dispatch('ask_update')