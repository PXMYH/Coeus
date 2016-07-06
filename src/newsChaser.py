# -*- coding: utf-8 -*-

#-----------------------------------------------------------------------------#
#              File: feedChaser.py                                            #
#              Author: Michael Hu                                             #
#              Date: May 24, 2015                                             #
#              Copyright pirixmanagement Corp.                                #
#-----------------------------------------------------------------------------#

#!/usr/bin/python
import urllib
import datetime
import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame
import Quandl as qd
import feedparser as fp

def fetch_news_feed_from_yahoo():
    python_wiki_rss_url = "http://www.python.org/cgi-bin/moinmoin/RecentChanges?action=rss_rc"
    feed = fp.parse( python_wiki_rss_url )
    print feed
    print
    
    
    yahoo_feed_url = "http://finance.yahoo.com/rss/headline?s=yhoo"
    yahoo_feed = fp.parse(yahoo_feed_url)
    print yahoo_feed
    
# -*- coding: utf-8 -*-

#-----------------------------------------------------------------------------#
#              File: feedChaser.py                                            #
#              Author: Michael Hu                                             #
#              Date: Nov 18, 2015                                             #
#              Copyright pirixmanagement Corp.                                #
#-----------------------------------------------------------------------------#

#!/usr/bin/python

import urllib2


# 
def fetch_press_release(symbol):
    # translate symbol to company name and website
    response = urllib2.urlopen('http://www.irobot.com/')
    html = response.read()
    print html
    
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 23:43:43 2015

@author: ProjectX
"""

from collections import Counter

def word_count(paragraph):
    words = paragraph.split()
    word_count = Counter(words)
    print "word count of paragrah is " + str(word_count)
    

def words_total_count(paragraph):
    count = len(paragraph.split())
    print "total number of words in this paragraph is " + str(count)
    



# -----------------------------------------------------------------------------
# Main Control
# ----------------------------------------------------------------------------- 
file_dir = "../res/"
file_name = "pr_fomc_july.txt"
file_path = file_dir + file_name

file_descriptor = open(file_path, 'r')
content = file_descriptor.read()
word_count(content)
print
print
words_total_count(content)

    