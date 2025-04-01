from MarketObject import load_data, MarketObject
from portfolio import Portfolio
from CalculateHoldings import rebalance_portfolio
import pandas as pd

def main():
    ### Load market data ###
    print("Loading market data...")
    rdata = load_data()

    ### Data preprocessing ###
    print("Processing market data...")
    rdata['Ticker'] = rdata['Ticker-Region'].dropna().apply(lambda x: x.split('-')[0].strip())
    rdata['Year'] = pd.to_datetime(rdata['Date']).dt.year
    rdata = rdata[['Ticker', 'Ending Price', 'Year', '6-Mo Momentum %']]

    ### Rebalancing portfolio across years ###
    print("Rebalancing portfolio...")
    final_portfolio = rebalance_portfolio(rdata, start_year=2002, end_year=2023, initial_aum=1)
    
    # Sample data (you would replace this with your actual FactSet_df)
    data = {
        'Year': [2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023],
        'Percent_Change': [None, 34.62, 17.48, 16.56, 8.65, 11.01, -15.63, -11.08, 11.89, -4.73, 30.01, 28.22, 2.6, -0.09, 13.71, 19.11, 13.8, -10.21, -1.03, 46.21, -24.48, 7.23]
    }
    
    FactSet_df = pd.DataFrame(data)
    
    # Calculate percent change for each year (from 2003 to 2023)
    FactSet_df['Benchmark_Change'] = FactSet_df['Percent_Change'].pct_change() * 100
    
    # Store the benchmark returns in a list (excluding the first year, which will be NaN)
    benchmark_returns = FactSet_df['Benchmark_Change'].dropna().tolist()

    # Ensure benchmark returns and portfolio returns align in length
    min_length = min(len(portfolio_returns), len(benchmark_returns))
    portfolio_returns = portfolio_returns[:min_length]
    benchmark_returns = benchmark_returns[:min_length]

    ### Calculate and display Information Ratio ###
    information_ratio = calculate_information_ratio(portfolio_returns, benchmark_returns)
    if information_ratio is not None:
        print(f"Information Ratio of the backtest: {information_ratio:.4f}")
    else:
        print("Information Ratio could not be calculated due to zero tracking error.")


if __name__ == "__main__":
    main()
