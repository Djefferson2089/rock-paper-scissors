from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
import random


class Move(str, Enum):
    ROCK = "rock"
    PAPER = "paper"
    SCISSORS = "scissors"

    @classmethod
    def from_user_input(cls, raw: str):
        raw = raw.strip().lower()
        return {
            "r": cls.ROCK,
            "rock": cls.ROCK,
            "p": cls.PAPER,
            "paper": cls.PAPER,
            "s": cls.SCISSORS,
            "scissors": cls.SCISSORS,
        }.get(raw)


class Outcome(str, Enum):
    WIN = "win"
    LOSE = "lose"
    TIE = "tie"


@dataclass
class RoundResult:
    player: Move
    computer: Move
    outcome: Outcome


def random_move() -> Move:
    return random.choice(list(Move))


def decide(player: Move, computer: Move) -> Outcome:
    if player == computer:
        return Outcome.TIE

    wins_against = {
        Move.ROCK: Move.SCISSORS,
        Move.PAPER: Move.ROCK,
        Move.SCISSORS: Move.PAPER,
    }

    return Outcome.WIN if wins_against[player] == computer else Outcome.LOSE


def play_round(player: Move) -> RoundResult:
    computer = random_move()
    outcome = decide(player, computer)
    return RoundResult(player, computer, outcome)
