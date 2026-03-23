from logic_utils import check_guess
import pytest

# Section 1: Guessing the Logic Tests
def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High", "📉 Go LOWER!"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low", "📉 Go HIGHER!"

# Section 2: 

def user_select():
    # If the user selects Easy there should be more player attempts
    # If the user selects Normal there should be less attempts then easy
    # Lastly, If the user selects Hard it should be the least attempts out of all 3 levels.
    result = user_select("Easy")
    assert result == "You have 8 try attempts"

    result = user_select("Normal")
    assert result == "You have 6 try attempts"

    result = user_select("Hard")
    assert result == "You have 5 try attempts"
 
 # Section 3: Run the pytest
    if __name__ == "__main__":
        pytest.main(["-v,__file__"])