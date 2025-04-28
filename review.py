from dataclasses import dataclass
from game import Game
from typing import Dict

@dataclass
class Review:
    game: Game
    score: int
    cost: float
    summary: str

    def __str__(self) -> str:
        genres = ", ".join(str(genre) for genre in self.game.genres)
        return (
            f"Game: {self.game.name}\n"
            f"Score: {self.score}/10\n"
            f"Genres: {genres}\n"
            f"Maturity Rating: {self.game.maturity_rating.name}\n"
            f"Cost: ${self.cost:.2f}\n"
            f"Art Style: {self.game.art_style.name}\n"
            f"Summary: {self.summary}\n"
        )