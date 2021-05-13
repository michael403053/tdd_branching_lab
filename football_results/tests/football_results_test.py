import unittest
from src.football_results import *

class FootballResultsTest(unittest.TestCase):
    
    def test_football_results__returns_home_win_string(self):
        score = {"home_score": 2, "away_score": 1}
        self.assertEqual("Home win", get_result(score))  

    def test_football_results__returns_away_win_string(self):
        score = {"home_score": 1, "away_score": 2}
        self.assertEqual("Away win", get_result(score))

    def test_football_results__returns_draw_string(self):
        score = {"home_score": 2, "away_score": 2}
        self.assertEqual("Draw", get_result(score))

    def test_football_results__returns_list_of_results(self):
        scores = [
            {"home_score": 2, "away_score": 1},
            {"home_score": 1, "away_score": 2},
            {"home_score": 2, "away_score": 2},
        ]
        self.assertEqual(3, len(get_results(scores)))

    
    # Test we get the right result string for a final score dictionary representing -

        # Home win
        # Away win
        # Draw

    # Test we get right list of result strings for a list of final score dictionaries. 


if __name__ == "__main__":
    unittest.main()
