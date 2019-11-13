# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 16:13:29 2019

@author: Money
"""

import requests
import json
    
def search_by_title(title, year=None):
    #The APi is provided by www.omdbapi.com
    
    url = "http://www.omdbapi.com/?t={0}&apikey=9adcf453".format(title)
    
    if year != None:
        url = url + '&y=' + str(year)
    
    response = requests.get(url)

    res = json.loads(response.text)
    return res


search_by_title('Les trois mousquetaires')