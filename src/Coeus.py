# -*- coding: utf-8 -*-

#-----------------------------------------------------------------------------#
#              File: Coeus.py                                              #
#              Author: Michael Hu                                             #
#              Date: January 31, 2015                                         #
#              Copyright pirixmanagement Corp.                                #
#-----------------------------------------------------------------------------#

#!/usr/bin/python
#import technicalData as techData
#import fundamentalData as fundData
#import newsChaser
#import pressReleaseCrawler
#from fundamentalData import fundamental_data_engine as fde
from technicalAnalysis import technical_analysis_engine
    
def main():
    # TODO: move the ticker list to a separate configuration file
    #tickerlist = ['AAPL', 'GOOG', 'FB', 'AMZN', 'IRBT', 'CIEN', 'SPY']
    # b4 book value 
    # d divident/share
    # e earning/share
    # f6 float shares
    # j2 shares outstanding
    # j4 EBITA
    # n name
    # p5 price/sales
    # p6 price/book
    # r P/E ratio
    # r5 PEG ratio
    # s symbol
    # s6 revenue
    # s7 short ratio
    # v volume
    # x stock exchange
    
    # unformated list array
#    metriclist  = ['b4', 'd', 'e', 'f6', 'j2', 'j4', 'n', 'p5', 'p6', 
#                   'r', 'r5', 's', 's6', 's7', 'x']
    # TODO: compile the optimal list order and match the metric with name
    # name,symbol,revenue,EBITA,book value,earning/share,volume,price/sales,
    # price/book,P/E ratio,PEG ratio, divident/share, float share,share outstanding,
    # short ratio, stock exchange
#    metriclist = ['n', 's', 's6', 'j4', 'b4', 'e', 'v', 'p5', 'p6', 
#                  'r', 'r5', 'd', 'f6', 'j2', 's7', 'x']
#    techData.get_historical_price_from_yahoo(tickerlist)
#    fundData.get_stat_from_yahoo(tickerlist, metriclist)
#    fundData.test_get_aapl_fund_from_quandl()
#    techData.test_get_aapl_hist_price_from_quandl()
#    newsChaser.fetch_news_feed_from_yahoo()
    
    
    ### fetch press release and perform analysis
    
    
    # update NYSE & NASDAQ stock list
    
    # convert list to JSON format
    
    # fetch press release
    #pressReleaseCrawler.fetch_press_release('IRBT')
    
    # analyze the press release
    
    # get fundamental data
    #fde.get_all_filings('20160101')  
    #fde.build_company_list("/home/atlantis/nest/Coeus/res/cik.lst")
    
    # technical analysis
    ta = technical_analysis_engine()
    ta.get_correlation('YHOO', 'CIEN', '2015-07-06', '2016-07-06')
    
if __name__ == '__main__':
    main()