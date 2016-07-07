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

import csv
import numpy as np
from _csv import reader
    
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
    
    res_folder = "/home/atlantis/projects/Coeus/res/"
    input_file_name = "tickers.csv"
    output_primary_stock = "primary_stocklist.txt"
    output_secondary_stock = "secondary_stocklist.txt"
    ticker_file = open(res_folder + input_file_name, 'rt')
    ticker_l = []
    try:
        reader = csv.reader(ticker_file)
        for row in reader:
            ticker_l.append(row[0])
        print ticker_l
    finally:
        ticker_file.close()
    
    # technical analysis
    ta = technical_analysis_engine()
    
    # get ticker list
    for idx_primary in range (0, len(ticker_l)):   # TODO: logic is disgusting, fix!
        primary_stock = ticker_l[idx_primary]
        for idx_secondary in range(idx_primary + 1, len(ticker_l)):
            secondary_stock = ticker_l[idx_secondary]
            print "primary stock is " + str(primary_stock)
            print "secondary stock is " + str(secondary_stock)
            
            corr = ta.get_correlation(str(primary_stock), str(secondary_stock), '2013-07-01', '2013-07-03')
    
            # collect stocks have strong correlation
            primary_stock_l = []
            secondary_stock_l = []
            if abs(corr) > 0.75:
                primary_stock_l.append(primary_stock)
                secondary_stock_l.append(secondary_stock)
                
    print "final list of strong correlation"
    for j in primary_stock_l:
        for k in secondary_stock_l:
            print(j, k)
    
    
    target = open(res_folder +  output_primary_stock, 'w')
    print "Opening the file " + res_folder +  output_primary_stock
    target.write("primary stocks:")
    target.write(primary_stock_l)
    target.close()
    
    
    target = open(res_folder +  output_secondary_stock, 'w')
    print "Opening the file " + res_folder +  output_secondary_stock
    target.write("secondary stocks:")
    target.write(secondary_stock_l)
    target.close()
    
    
if __name__ == '__main__':
    main()