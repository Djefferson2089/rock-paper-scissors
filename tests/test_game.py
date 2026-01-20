from rps.game import Move, decide, Outcome


def test_tie():
    assert decide(Move.ROCK, Move.ROCK) == Outcome.TIE


def test_win():
    assert decide(Move.ROCK, Move.SCISSORS) == Outcome.WIN


def test_loss():
    assert decide(Move.ROCK, Move.PAPER) == Outcome.LOSE
