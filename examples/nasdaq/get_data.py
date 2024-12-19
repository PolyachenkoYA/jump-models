"""
This script retrieves the daily closing price data for 
the Nasdaq-100 index from Yahoo Finance via its Python API.

Users do not need to run this script manually, as the return data 
is already saved in `example/Nasdaq/data/`. 
"""

from utils_dir import *
include_home_dir()

import numpy as np
import pandas as pd
import yfinance as yf
from datetime import datetime

from jumpmodels.utils import check_dir_exist

 #= "NDX"   # Nasdaq-100 Index

def get_data(TICKER, start=None, end=None, to_save=True, name_prefix=''):
	if(start is None):
		#start = "1985-10-01"
		start = 'max'
	if(end is None):
		end = datetime.today().strftime('%Y-%m-%d')
	
	# download closing prices
	if(len(start) == 10):
		close: pd.Series = yf.download(name_prefix+TICKER, start=start, end=end)['Close']
	else:
		close: pd.Series = yf.download(name_prefix+TICKER, period=start)['Close']
	# convert to ret
	ret = close.pct_change()
	# concat as df
	df = pd.DataFrame({"close": close.to_numpy().flatten(), "ret": ret.to_numpy().flatten()}, index=close.index.date)
	df.index.name = "date"
	
	# save
	if(to_save):
		curr_dir = get_curr_dir()
		data_dir = f"{curr_dir}/data/"; check_dir_exist(data_dir)
		pd.to_pickle(df, f"{data_dir}{TICKER}.pkl")
		np.round(df, 6).to_csv(f"{data_dir}{TICKER}.csv")
	
	print("Successfully downloaded data for ticker:", TICKER)
	
	return df

if __name__ == "__main__":
	get_data()
