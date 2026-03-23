def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 50
    if difficulty == "Hard":
        return 1, 100
    return 1, 100


def get_attempts_for_difficulty(difficulty: str) -> int:
    """Return the number of attempts allowed for a given difficulty."""
    attempt_limit_map = {
        "Easy": 8,
        "Normal": 6,
        "Hard": 5,
    }
    return attempt_limit_map.get(difficulty, 5)


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    if guess == secret:
<<<<<<< HEAD
        return "Win"

    if guess > secret:
        return "Too High"
    return "Too Low"
=======
        return "Win", "🎉 Correct!"

    if guess > secret:
        return "Too High", "📉 Go LOWER!"
    return "Too Low", "📈 Go HIGHER!"
>>>>>>> d837c6db99c335096133ea2b658bb0d7df7e2d16


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
<<<<<<< HEAD
=======
    # If the user wins then they should get points
>>>>>>> d837c6db99c335096133ea2b658bb0d7df7e2d16
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score
<<<<<<< HEAD
=======

>>>>>>> d837c6db99c335096133ea2b658bb0d7df7e2d16
