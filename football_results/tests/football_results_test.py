import unittest
from src.football_results import *

class FootballResultsTest(unittest.TestCase):

    scores = {"home_score": 0, "away_score": 1}
  

    def test_football_results__returns_home_win_string(self):
        self.assertEqual("Home win", get_result(self.scores))

    
    # Test we get the right result string for a final score dictionary representing -

        # Home win
        # Away win
        # Draw

    # Test we get right list of result strings for a list of final score dictionaries. 


if __name__ == "__main__":
    unittest.main()
