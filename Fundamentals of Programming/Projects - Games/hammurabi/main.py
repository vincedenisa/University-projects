from controller import Controller
from repo import Repo
from ui import UI
from validator import Validator


def start():
    repo = Repo()
    validator = Validator()
    controller = Controller(repo, validator)
    ui = UI(controller)
    ui.run_the_game_for_every_year()

start()