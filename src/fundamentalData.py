# -*- coding: utf-8 -*-

#-----------------------------------------------------------------------------#
#              File: fundamentalData.py                                       #
#              Author: Michael Hu                                             #
#              Date: May 23, 2015                                             #
#              Copyright pirixmanagement Corp.                                #
#-----------------------------------------------------------------------------#

#!/usr/bin/python
import urllib
import datetime
import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame
import Quandl as qd
import time
import os
from SECEdgar.crawler import SecCrawler


class fundamental_data_engine():
    ''' Atrributes '''
    # TODO: remove this section for security reason
    quandl_api_key = "g1_jQ_mqf2-9QZoLCVyN"
    company_name_dict = {}
    
    def __init__(self, quandl_api_key):
        self.quandl_api_key = "g1_jQ_mqf2-9QZoLCVyN"
        self.company_name_dict = {}
        
        
        
    # ------------------------------------------------------------------------- #
    #                                   Yahoo                                   #
    # ------------------------------------------------------------------------- #
    #------------------------------------------------------------------------------
    # Function: get_yahoo_finance_api_stat_common_url
    #
    # Description: get common segment of yahoo finance api key stat url
    #
    # Parameters: none
    #
    # Return: common_stat_url
    #------------------------------------------------------------------------------    
    def __get_yahoo_finance_api_stat_common_url(self):
        return "http://finance.yahoo.com/d/quotes.csv"
    
    #------------------------------------------------------------------------------
    # Function: get_yahoo_finance_api_history_common_url
    #
    # Description: get common segment of yahoo finance api history url
    #
    # Parameters: none
    #
    # Return: common_history_url
    #------------------------------------------------------------------------------   
    def __get_yahoo_finance_api_history_common_url(self):
        return "http://ichart.finance.yahoo.com/table.csv"
    
    #------------------------------------------------------------------------------
    # Function: construct_stat_url
    #
    # Description: get key stats feeds from YAHOO Finance
    #
    # Parameters: url_common
    #             symbol_list
    #             info_list
    #
    # Return: url
    #------------------------------------------------------------------------------    
    def __construct_stat_url(self, url_common, symbol_list, info_list):
        
        # process symbols
        url = str(url_common) + "?s="
        for i in range (0, len(symbol_list)):
            url = url + symbol_list[i]
            if i != (len(symbol_list) - 1):
                url = url + "+"
        
        # process stat
        url = str(url) + "&f="
        for i in range (0, len(info_list)):
            url = url + info_list[i]
        
        return url
    
    #------------------------------------------------------------------------------
    # Function: construct_history_url
    #
    # Description: get history feeds from YAHOO Finance
    #
    # Parameters: url_common
    #             symbol
    #             start_date
    #             end_date
    #
    # Return: url
    #------------------------------------------------------------------------------   
    def __construct_history_url(self, url_common, symbol, start_date, end_date):
        # process symbols
        url = str(url_common) + "?s=" + symbol
        
        # process date
        year_start  = start_date.year
        month_start = start_date.month
        day_start   = start_date.day
        
        year_end  = end_date.year
        month_end = end_date.month
        day_end   = end_date.day
        
        # construct url
        url = url + "&a=" + str(day_start) + "&b=" + str(month_start) + "&c=" + str(year_start) \
                  + "&d=" + str(day_end)   + "&e=" + str(month_end)   + "&f=" + str(year_end)
                  
        return url
    
    #------------------------------------------------------------------------------
    # Function: download_stat_csv
    #
    # Description: downlaod quote key stat data in csv format
    #
    # Parameters: url
    #
    # Return: none
    #------------------------------------------------------------------------------    
    def __download_stat_csv(self,url, filename):
        # TODO: add function to create customized file name and save directory
        urllib.urlretrieve(url, str(filename)+".csv")
    
    #------------------------------------------------------------------------------
    # Function: download_history_csv
    #
    # Description: downlaod stock history data in csv format
    #
    # Parameters: url
    #             filename
    #
    # Return: none
    #------------------------------------------------------------------------------        
    def __download_history_csv(self, url, filename):
        urllib.urlretrieve(url, filename)
        
    #------------------------------------------------------------------------------
    # Function: get_stat_from_yahoo
    #
    # Description: get data key stats from YAHOO Finance
    #
    # Parameters: tickerlist
    #
    # Return: none
    #------------------------------------------------------------------------------
    #===========================================================================
    # def get_stat_from_yahoo(self, tickerlist, metriclist):
    #     ''' get data key stats from YAHOO Finance '''
    #     # TODO: read stock symbols/ info etc. from JSON format text based file
    #     #    tickerlist = ['IRBT', 'XOP']
    #     # TODO: separate the info_list to a function for user to choose
    #     
    #     download_url = __construct_stat_url(__get_yahoo_finance_api_stat_common_url(), 
    #                                       tickerlist, 
    #                                       metriclist)
    #     print("key stats url is " + str(download_url)) 
    #     __download_stat_csv(download_url, 'tickerStats')
    #===========================================================================
    
    #------------------------------------------------------------------------------
    # Function: get_history_feeds_from_yahoo
    #
    # Description: get history feeds from YAHOO Finance
    #
    # Parameters: none
    #
    # Return: none
    #------------------------------------------------------------------------------
    #===========================================================================
    # def get_history_feeds_from_yahoo(self):
    #     ''' get history feeds from YAHOO Finance '''
    #     # TODO: add function allows user to select/add stock symbols
    #     stock_list = ['IRBT', 'XOP']
    #     dt_start   = datetime.date(2008, 1, 1)
    #     dt_end     = datetime.date.today()
    #     file_name  = ['IRBT.csv', 'XOP.csv']
    #     download_url = __construct_history_url(__get_yahoo_finance_api_history_common_url(), 
    #                                          stock_list[0],
    #                                          dt_start,
    #                                          dt_end)
    #     print("history url is " + str(download_url))
    #     __download_history_csv(download_url, file_name[0])
    #===========================================================================
    
    
    # ------------------------------------------------------------------------- #
    #                                   Quandal                                 #
    # ------------------------------------------------------------------------- #
    
    def test_get_aapl_fund_from_quandl(self):
        ''' test quandl database API using AAPL '''
        
    #    sales_quarter = qd.get("SEC/AAPL_SALESREVENUENET_Q")
    #    sales_annual = qd.get("SEC/AAPL_SALESREVENUENET_A")
        # Note: strive to use one call to get multiple databases to avoid reaching call limit per day
    #    sales_combo = qd.get(["SEC/AAPL_SALESREVENUENET_Q", "SEC/AAPL_SALESREVENUENET_A"])
    #    cost_of_goods_sold = qd.get("SEC/AAPL_COSTOFGOODSANDSERVICESSOLD_A")
    #    stockholder_equity= qd.get("SEC/AAPL_STOCKHOLDERSEQUITY_A")
    #    current_liability = qd.get("SEC/AAPL_LIABILITIESCURRENT_A")
    #    gross_profit = qd.get("SEC/AAPL_GROSSPROFIT_A")
    #    sga = qd.get("SEC/AAPL_SELLINGGENERALANDADMINISTRATIVEEXPENSE_A")
    #    cash = qd.get("DMDRN/AAPL_CASH")
        
    #    top_line_combo = qd.get(["SEC/AAPL_SALESREVENUENET_A", "SEC/AAPL_COSTOFGOODSANDSERVICESSOLD_A"])
    #    print top_line_combo
    #    print
    #    print top_line_combo.index.values
    #    print top_line_combo.columns.values
    #    print "cost of goods sold"
    #    print top_line_combo['SEC.AAPL_COSTOFGOODSANDSERVICESSOLD_A - Value']
        
        all_financial_ratio = qd.get("DMDRN/AAPL_ALLFINANCIALRATIOS")
        print all_financial_ratio.index.values    
        print all_financial_ratio.columns.values
        print 
        print all_financial_ratio
        
        # get the ratio dataframe; store column value into array as key to select ratios
        # here's a sneak peek 
        ''' ['Number of Shares Outstanding' '3-Year Regression Beta'
     '3-year Standard Deviation of Stock Price' 'Book Debt to Capital Ratio'
     'Book Value of Equity' 'Book Value of Assets' 'Capital Expenditures'
     'Cash' 'Cash as Percentage of Firm Value' 'Cash as Percentage of Revenues'
     'Cash as Percentage of Total Assets' 'Change in Non-Cash Working Capital'
     'Correlation with the Market' 'Current PE Ratio' 'Depreciation'
     'Dividend Yield' 'Dividends' 'Earnings Before Interest and Taxes'
     'EBIT for Previous Period'
     'Earnings Before Interest Taxes Depreciation and Amortization'
     'Effective Tax Rate' 'Effective Tax Rate on Income' 'Enterprise Value'
     'EV to Invested Capital Ratio' 'EV to Trailing Sales Ratio'
     'EV to EBIT Ratio' 'EV to EBITDA Ratio' 'EV To Sales Ratio'
     'Expected Growth in Earnings Per Share' 'Expected Growth in Revenues'
     'Free Cash Flow to Firm' 'Firm Value'
     'Ratio of Fixed Assets to Total Assets' 'Forward Earnings Per Share'
     'Forward PE Ratio' 'Growth in Earnings Per Share'
     'Previous Year Growth in Revenues' 'Hi-Lo Risk' 'Insider Holdings'
     'Institutional Holdings' 'Ratio of Intangible Assets to Total Assets'
     'Invested Capital' 'Market Capitalization' 'Market Debt to Equity Ratio'
     'Market Debt to Capital Ratio' 'Net Income' 'Net Margin'
     'Non-Cash Working Capital'
     'Non-Cash Working Capital as Percentage of Revenues' 'Payout Ratio'
     'Price to Book Value Ratio' 'PE to Growth Ratio'
     'Pre-Tax Operating Margin' 'Price to Sales Ratio' 'Reinvestment Amount'
     'Reinvestment Rate' 'Revenues' 'Return on Capital' 'Return on Equity'
     'Sales General and Administration Expenses' 'Stock Price' 'Total Debt'
     'Trading Volume' 'Trailing 12-month Revenues' 'Trailing Net Income'
     'Trailing PE Ratio' 'Trailing Revenues' 'Value Line Beta'
     'EV to Book Value Ratio'] '''
        
    #    plt.clf()
    #    mydata.plot(subplots = True, figsize = (16, 16))
    #    plt.legend(loc = 'best')                            
    #    plt.xlabel('Date')
    #    plt.ylabel('Sales Revenue Quarterly') 
        
        
    #    print "\n Sales Quarterly Net \n"
    #    print sales_quarter
    #    print "\n Sales Annually Net \n"
    #    print sales_annual
    #    print "\n**************************************"
    #    print "Sales Quarterly and Annually Net"
    #    print "\n**************************************"
    #    print sales_combo
    
    
    
    def get_company_name_cik_dict(self):
        return self.company_name_dict
    
    res_folder = '/home/atlantis/nest/Coeus/res'
    
    #===========================================================================
    # get_company_name_ticker_dict
    #===========================================================================
    #def get_company_name_ticker_dict(self):
        
    
    def build_company_list(self, file):
        
        # open the cik list file
        cik_file = open("/home/atlantis/nest/Coeus/res/cik.lst", "r")
        print "Opened file " + cik_file.name + " in "+ cik_file.mode + " mode."
        
        for i in range(0, 13):
            cik_file.readline();
        
        for line in range(14, 20491):
            line = cik_file.readline();
            #print "Content is ", line
            elem = line.split()
            #print "After split ", elem
            cik = elem[-1]
            #print "cik is ", cik
            name = elem[:-1]
            name = " ".join(name)
            #print "the company name is ", name
            
            # create the company cik dictionary
            self.company_name_dict[name] = cik
        
        print "company AAPL cik is " + self.company_name_dict['APPLE COMPUTER INC']
            
        # close the file
        cik_file.close()
    
    def get_all_filings(self, deadline):
        ''' get the SEC filings for all companies in US stock universe'''
        t1 = time.time()
     
        # create object
        seccrawler = SecCrawler()
     
        companyCode = 'AAPL'    # company code for apple 
        cik = '0000320193'      # cik code for apple
        date = '20160101'       # date from which filings should be downloaded
        count = '100'            # no of filings
     
        seccrawler.filing_10Q(str(companyCode), str(cik), str(date), str(count))
        seccrawler.filing_10K(str(companyCode), str(cik), str(date), str(count))
        seccrawler.filing_8K(str(companyCode), str(cik), str(date), str(count))
        seccrawler.filing_13F(str(companyCode), str(cik), str(date), str(count))
     
        t2 = time.time()
        print "Total Time taken: " + str(t2-t1),
        
    def get_country_unempoyment_rate(self, country_name):
        print "Country: " + country_name + " Unemployment Rate: N/A";
