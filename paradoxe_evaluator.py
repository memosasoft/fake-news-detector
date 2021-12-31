import requests
import urllib.parse

from bs4 import BeautifulSoup
from fake_useragent import UserAgent

def load_list(file, list):
    pass

def get_url(url):
    
    page = rq.get(current_url, headers={'User-Agent': ua.random},timeout=10)
    status_code = page.status_code
   
    finale_score = 0
    
    if "200" in status_code:
        link_score = link_evaluation(url)
        text = bs.find_all(text=True)

        text = stop_list(text)
        text_score = content_evaluation(text)
        
        spam_score = spam_evalution(text)
        quality_score = quality_evalution(text)
        link_score = link_evaluation(url)
        content_score = content_evaluation(text)
        finale_score = finale_verification(spam_score, quality_score, link_score, content_score)
      
    return finale_score

def stop_list(text):
    return text

def spam_evalution(text):


    return text

def quality_evalution(text):
    return text

def link_evaluation(url):
    score = 0
    return score

def content_evaluation(text):
    score = 0
    return score

def finale_verification(spam_score, quality_score, link_score, content_score):
    return finale_score


    # url file loading and cleaning process
def load_list(file_name, list):

    print("Starting loading list")
    print("with file name: " + file_name)

    memory = []

    # open file with list of url
    with open(file_name, "r") as file: 
        # reading each line     
        for string in file:    
            # inset in url list object 
            if string not in memory:
                list.append(string)
                memory.append(string)
        file.close()
    memory = []

    return list
