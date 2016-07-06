#-----------------------------------------------------------------------------#
#              File: pirix_data.py                                            #
#              Author: Michael Hu                                             #
#              Date: January 31, 2015                                         #
#              Copyright pirixmanagement Corp.                                #
#-----------------------------------------------------------------------------#

#!/usr/bin/python
import urllib
import datetime
# import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame
import datetime as dt
import pandas.io.data as pd_data

#------------------------------------------------------------------------------
# Function: get_yahoo_finance_api_stat_common_url
#
# Description: get common segment of yahoo finance api key stat url
#
# Parameters: none
#
# Return: common_stat_url
#------------------------------------------------------------------------------    
def get_yahoo_finance_api_stat_common_url():
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
def get_yahoo_finance_api_history_common_url():
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
def construct_stat_url(url_common, symbol_list, info_list):
    
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
def construct_history_url(url_common, symbol, start_date, end_date):
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
def download_stat_csv(url):
    # TODO: add function to create customized file name and save directory
    urllib.urlretrieve(url, "key_stats.csv")

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
def download_history_csv(url, filename):
    urllib.urlretrieve(url, filename)
    
#------------------------------------------------------------------------------
# Function: get_stat_from_yahoo
#
# Description: get data key stats from YAHOO Finance
#
# Parameters: none
#
# Return: none
#------------------------------------------------------------------------------
def get_stat_from_yahoo():
    # TODO: read stock symbols/ info etc. from JSON format text based file
    stock_list = ['IRBT', 'XOP']
    # TODO: separate the info_list to a function for user to choose
    info_list  = ['n', 's', 'p', 'j3', 'x', 'j4', 'r', 'e', 'b4']
    download_url = construct_stat_url(get_yahoo_finance_api_stat_common_url(), 
                                      stock_list, 
                                      info_list)
    print("key stats url is " + str(download_url)) 
    download_stat_csv(download_url)

#------------------------------------------------------------------------------
# Function: get_history_feeds_from_yahoo
#
# Description: get history feeds from YAHOO Finance
#
# Parameters: none
#
# Return: none
#------------------------------------------------------------------------------
def get_history_feeds_from_yahoo():
    # TODO: add function allows user to select/add stock symbols
    stock_list = ['IRBT', 'XOP']
    dt_start   = datetime.date(2008, 1, 1)
    dt_end     = datetime.date.today()
    file_name  = ['IRBT.csv', 'XOP.csv']
    download_url = construct_history_url(get_yahoo_finance_api_history_common_url(), 
                                         stock_list[0],
                                         dt_start,
                                         dt_end)
    print("history url is " + str(download_url))
    download_history_csv(download_url, file_name[0])

#------------------------------------------------------------------------------
# Function: parse_data_from_csv
#
# Description: parse csv data file
#
# Parameters: none
#
# Return: none
#------------------------------------------------------------------------------    
def parse_data_from_csv():
    print("nothing yet ...")
    
    
def main():
#     get_stat_from_yahoo()
#     get_history_feeds_from_yahoo()
#     parse_data_from_csv()
    
    sp500 = pd_data.get_data_yahoo('RTN', 
                                   start=datetime.datetime(2000, 10, 1), 
                                   end=dt.datetime.today())
    print sp500.head()
    sp500.to_csv('RTN.csv')
    df = pd.read_csv('RTN.csv', index_col='Date', parse_dates=True)
    print df.head()
    
#     plt.clf()
#     plt.legend(['$SPX', 'XOM'])
#     plt.ylabel('Daily Returns')
#     plt.xlabel('Date')
#     plt.savefig('rets.pdf', format='pdf')
    
if __name__ == '__main__':
    main()