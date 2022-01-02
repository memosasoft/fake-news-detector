import time
import urllib.parse
from datetime import datetime
import time
import requests

import requests as rq 
from _ctypes import Array, Structure, Union
from bs4 import BeautifulSoup as bs
from fake_useragent import UserAgent

RELAX_TIME = 0.0000001
ua = UserAgent()

def get_data(query):
    
    url = 'https://newsapi.org/v2/everything?q='+query+'&sortBy=popularity&apiKey=1456d6730b004831a5adfb81260d0536'
    
    page = rq.get(url, headers={'User-Agent': ua.random},timeout=10)
    status_code = page.status_code
 
    if status_code == 200:  
        for x in page:
            print(x)

query = input("What are you looking for")
get_data(query)