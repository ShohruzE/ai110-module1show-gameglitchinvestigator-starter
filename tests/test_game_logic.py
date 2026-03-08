import sys
from pathlib import Path

# Ensure the project root is importable when tests run from inside `tests/`.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from logic_utils import (
    check_guess,
    get_range_for_difficulty,
    parse_guess,
    update_score,
)


def test_get_range_for_difficulty():
    assert get_range_for_difficulty("Easy") == (1, 20)
    assert get_range_for_difficulty("Normal") == (1, 50)
    assert get_range_for_difficulty("Hard") == (1, 100)


def test_parse_guess_valid_and_invalid():
    ok, val, err = parse_guess("42")
    assert ok and val == 42 and err is None

    ok, val, err = parse_guess("42.0")
    assert ok and val == 42 and err is None

    ok, val, err = parse_guess("")
    assert not ok and err is not None

    ok, val, err = parse_guess("abc")
    assert not ok and err == "That is not a number."


def test_check_guess_outcomes_and_messages():
    outcome, msg = check_guess(50, 50)
    assert outcome == "Win" and "Correct" in msg

    outcome, msg = check_guess(60, 50)
    assert outcome == "Too High" and "LOWER" in msg

    outcome, msg = check_guess(40, 50)
    assert outcome == "Too Low" and "HIGHER" in msg


def test_update_score_behavior():
    # Win scoring (attempt_number used directly by function)
    assert update_score(0, "Win", 1) == 80

    # Too High: even attempt -> +5, odd attempt -> -5
    assert update_score(10, "Too High", 2) == 15
    assert update_score(10, "Too High", 3) == 5

    # Too Low: -5
    assert update_score(10, "Too Low", 1) == 5
