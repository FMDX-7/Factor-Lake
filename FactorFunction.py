from MarketObject import MarketObject, load_data
import pandas as pd

class Factors:
    @staticmethod
    def Momentum6m(ticker, market):
        ticker_data = market.stocks.loc[market.stocks['Ticker'] == ticker]

        #check to see if results are empty - molly
        if ticker_data.empty:
            print(f"{ticker} - not found in market data for {market.t} - SKIPPING")
            return None
        #column in excel sheet is called: 6-Mo Momentum %
       # return ticker_data['6-Mo Momentum %'].iloc[-1]
        try:
            return market.load_data.loc[market.load_data["Ticker"] == ticker, "6-Mo Momentum %"].values[0]
        except (KeyError, IndexError):
            return None