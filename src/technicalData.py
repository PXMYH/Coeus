# -*- coding: utf-8 -*-

#-----------------------------------------------------------------------------#
#              File: technicalData.py                                         #
#              Author: Michael Hu                                             #
#              Date: May 23, 2015                                             #
#              Copyright pirixmanagement Corp.                                #
#-----------------------------------------------------------------------------#

#!/usr/bin/python
import pandas as pd
import datetime as dt
import pandas.io.data as data_fetch
import matplotlib.pyplot as plt
import Quandl as qd

#------------------------------------------------------------------------------
# Function: write_csv
#
# Description: write data into csv file format
#
# Parameters: data
#             filename
#
# Return: none
#------------------------------------------------------------------------------
def write_csv(data, filename):
    data.to_csv(str(filename) + '.csv')



# ------------------------------------------------------------------------- #
#                                   Yahoo                                   #
# ------------------------------------------------------------------------- #


#------------------------------------------------------------------------------
# Function: get_historical_price_from_yahoo
#
# Description: get history feeds from YAHOO Finance
#
# Parameters: tickerlist
#
# Return: none
#------------------------------------------------------------------------------    
def get_historical_price_from_yahoo(tickerlist):
    tickerdata = {}
    
    for ticker in tickerlist:
        tickerdata[ticker] = data_fetch.DataReader(
                                   ticker,
                                   'yahoo',
                                   start=dt.datetime(2000, 10, 1), 
                                   end=dt.datetime.today())
       
       # TODO: check why GOOG stock price information is incomplete 
#        print tickerdata[ticker].head()
#        tickerdata[ticker].plot(subplots = True, figsize = (8, 8))
     
        
    price = pd.DataFrame(
                              {tic: data['Adj Close']
                               for tic, data in tickerdata.items()}
                              )
                              
    # plot graphs 
    plt.clf()
    price.plot(subplots = True, figsize = (16, 16))
    plt.legend(loc = 'best')                            
    plt.xlabel('Date')
    plt.ylabel('Daily Returns')   
    plt.savefig('collection.pdf', format='pdf') 

    # save pdf plot                        
    
    write_csv(price, 'collection')
#    df = pd.read_csv('SPY.csv', index_col='Date', parse_dates=True)
#    print df.head() 
    
    
    
# ------------------------------------------------------------------------- #
#                                   Quandal                                 #
# ------------------------------------------------------------------------- #
    
def test_get_aapl_hist_price_from_quandl():
    hist_price = qd.get("WIKI/AAPL")
    print hist_price
    
    plt.clf()
    hist_price['Adj. Close'].plot(subplots = True, figsize = (8,16))
    plt.legend(loc = 'best')
    plt.xlabel('date')
    plt.ylabel('adj price')