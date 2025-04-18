from FactorFunction import Factors, Momentum6m
from MarketObject import MarketObject, load_data
from CalculateHoldings import rebalance_portfolio
import unittest
import pandas as pd

class TestFactorLakePortfolio(unittest.TestCase):
    def setUp(self):
        self.data = load_data()
        if 'Year' not in self.data.columns:
            self.data['Year'] = pd.to_datetime(self.data['Date']).dt.year
        self.start_year = 2002
        self.end_year = 2023
        self.initial_aum = 1
        self.expected_final_value = 4.39
        self.expected_growth = 339.42
        self.factors = [Momentum6m()]

    def test_portfolio_growth(self):
        portfolio_values = rebalance_portfolio(self.data, self.factors, self.start_year, self.end_year, self.initial_aum)
        final_aum = portfolio_values[-1]

        self.assertAlmostEqual(
            final_aum,
            self.expected_final_value,
            delta=0.01,
            msg=f'Expected portfolio values: ${self.expected_final_value}%, but got {final_aum}%'
        )

        overall_growth = (final_aum - self.initial_aum) / self.initial_aum * 100
        self.assertAlmostEqual(
            overall_growth,
            self.expected_growth,
            delta=0.1,
            msg=f'Expected overall growth: {self.expected_growth}%, but got {overall_growth}%'
        )

if __name__ == '__main__':
    unittest.main()
