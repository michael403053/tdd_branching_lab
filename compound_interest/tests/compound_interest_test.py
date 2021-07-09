import unittest

from src.compound_interest import CompoundInterest

class CompoundInterestTest(unittest.TestCase):

    def test_compound_interest__100_returns_732(self):
        investment = {
            "principal": 100,
            "rate": 0.1,
            "years": 20,
            "per_year": 12, 
            "investment_per_month": 1000
        }

        self.assertEqual(732.81, CompoundInterest.get_interest_total(investment))

    def test_compound_interest__add_monthly_investment(self):
        investment = {
            "principal": 100,
            "rate": 0.05,
            "years": 10,
            "per_year": 12, 
            "investment_per_month": 1000
        }

        self.assertEqual(156093.99, CompoundInterest.get_interest_total_deposits(investment))

    # Tests

    # Should return 732.81 given 100 principal, 10 percent, 20 years

    # Should return 181.94 given 100 principal, 6 percent, 10 years

    # Should return 149,058.55 given 100000 principal, 5 percent, 8 years

    # Should return 0.00 given 0 principal, 10 percent, 1 year

    # Should return 100.00 given 100 principal, 0 percent, 10 years


    # Extention tests

    # Should return 118,380.16 given 100 principal, 5 percent, 8 years, 1000 per month

    # Should return 156,093.99 given 100 principal, 5 percent, 10 years, 1000 per month

    # Should return 475,442.59 given 116028.86, 7.5 percent, 8 years, 2006 per month

    # Should return 718,335.96 given 116028.86 principal, 9 percent, 12 years, 1456 per month

