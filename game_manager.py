from game import Game
import random
import string


class GameManager():
    games: dict

    def __init__(self) -> None:
        self.games = {}

    def new(self) -> str:
        while True:
            id = ''.join(
                [random.choice(string.ascii_letters + string.digits) for _ in range(8)])
            if id not in self.games.keys():
                break

        self.games[id] = Game()

        return id

    def validId(self, game_id: str) -> bool:
        return game_id in self.games.keys()

    def get(self, game_id: str) -> Game:
        return self.games[game_id]

    def remove(self, game_id: str) -> None:
        self.games.pop(game_id)
