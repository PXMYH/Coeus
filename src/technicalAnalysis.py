# -*- coding: utf-8 -*-

#-----------------------------------------------------------------------------#
#              File: technicalAnalysis.py                                     #
#              Author: Michael Hu                                             #
#              Date: July 6, 2016                                             #
#              Copyright pirixmanagement Corp.                                #
#-----------------------------------------------------------------------------#

import numpy as np
from yahoo_finance import Share
from scipy.stats.stats import pearsonr

class technical_analysis_engine():
    
    def __init__(self):
        print "technical analysis initalized ..."
        
    # download stock price based on tick
    def __get_history_stock(self, ticker, start_date, end_date):
        print "ticker " + str(ticker)
        stock = Share(ticker)
        stock_price_l = []
        stock_history_struct_arr = stock.get_historical(start_date, end_date)
        print "history price stucture array " + str(stock_history_struct_arr)
        for idx in range(0, len(stock_history_struct_arr)):
            stock_price_l.append(stock_history_struct_arr[idx]['Close'])
            print "current price " + str(stock_history_struct_arr[idx]['Close'])
            print stock_price_l
        stock_price_l = np.array(stock_price_l).astype(np.float)
        print str(ticker) + " price = " + str(stock_price_l)
        return stock_price_l
    
    def get_correlation(self, ticker_primary, ticker_secondary, start_date, end_date):
        # declare price history list
        primary_stock_price_history_l = []
        secondary_stock_price_history_l = []
        
        print "primary ticker " + str(ticker_primary)+ " secondary ticker " + str(ticker_secondary)
        
        # get stock price history
        primary_stock_price_history_l = self.__get_history_stock(ticker_primary, start_date, end_date)
        print "primary stock history " + str(primary_stock_price_history_l)
        secondary_stock_price_history_l = self.__get_history_stock(ticker_secondary, start_date, end_date)
        print "secondary stock history " + str(secondary_stock_price_history_l)
        
        
        if len(secondary_stock_price_history_l) == 0:
            print "empty list!"
        # error handling
        if len(primary_stock_price_history_l) == 0 or len(secondary_stock_price_history_l) == 0: # TODO: change to try, catch later
            corr_coeff = 0
            corr_p = 0
            print "inside!"
        else:
            # get pearson coefficient
            corr_coeff, corr_p = pearsonr(primary_stock_price_history_l, secondary_stock_price_history_l)
            
            print "correlation between " + str(ticker_primary) + " and " + str(ticker_secondary) + " = " + str(corr_coeff)
            print "correlation p = " + str(corr_p)
        
        return corr_coeff
        
        