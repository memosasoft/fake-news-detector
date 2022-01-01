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
memory = []
ua = UserAgent()

data_size = 0

# Website info
title = ""
description = ""

# Basic Knowledge List 
q_list          = []
bad_list        = []
stoplist        = []
spam_list       = []
good_list       = []
list_compromis  = []
acceptable_list = []

    # url file loading and cleaning process
def load_list(file_name, list):

    #print("Starting loading list")
    #print("with file name: " + file_name)

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

def load():

    global q_list          
    global bad_list        
    global stoplist      
    global spam_list      
    global good_list     
    global list_compromis 
    global acceptable_list

    print("This may take some time...")

    # Loading Knowledge List 
    stoplist = load_list("./smart_lists/stoplist", stoplist)
    print("stoplist loaded...")
    
    spam_list = load_list("./smart_lists/spam", spam_list)
    print("spam list loaded...")
    
    q_list = load_list("./smart_lists/quality", q_list)
    print("quality list loaded...")
    
    list_compromis = load_list("./smart_lists/compromised_domains", list_compromis)
    print("domains loaded...")
    
    bad_list = load_list("./smart_lists/bad_domains", bad_list)
    print("bad domains loaded...")
    
    good_list = load_list("./smart_lists/good_domains", good_list)
    print("good domains loaded...")
    
    acceptable_list = load_list("./smart_lists/top_domains_list_acceptable", acceptable_list)
    
    print("pronlem domains loaded...")
    print("Lists loaded - thank you")

def get_url(url):

    global data_size
    global title
    global description

    page = rq.get(url, headers={'User-Agent': ua.random},timeout=20)
    status_code = page.status_code
   
    finale_score = 0
    list = []
    if status_code == 200:  
        url_spectal = url.replace("https://", "")
        url_spectal = url.replace("http://", "")
        link_score = link_evaluation(url_spectal)
        #print("LINK SCORE: " + str(link_score))
        html = bs(page.text, 'lxml')
        text = html.find_all(text=True)
        title = html.find('title')
    
        output = ''
        blacklist = [
            '[document]',
            'noscript',
            'header',
            'html',
            'meta',
            'head', 
            'input',
            'script',
            # there may be more elements you don't want, such as "style", etc.
        ]

        for t in text:
            if t.parent.name not in blacklist:
                output += '{} '.format(t)

        #print(output)
        output = stop_list(str(output))

        data_size = len(output.split(" "))

        spam_score, output = spam_evaluation(str(output))
        #print("SPAM SCORE: " + str(spam_score))

        quality_score, output = quality_evaluation(str(output))
        #print("Q-SCORE: " + str(quality_score))
        
        content_score = content_evaluation(str(output))
        #print("TEXT SCORE: " + str(text_score))
        
        result = finale_verification(url, title, spam_score, quality_score, link_score, content_score)
        
        # Loop process
        input_user()

    return finale_score

stoplist_filter_counter = 0

def stop_list(text):
    global index
    stoplist_filter_counter = 0
    global stoplist
    for i in stoplist:
        text = text.replace(i,"") 
        spam_filstoplist_filter_counterter_counter = stoplist_filter_counter + 1
    return text

spam_filter_counter = 0

def spam_evaluation(text):
    
    full = ""
    spam_filter_counter = 0
    
    global spam_list

    for i in spam_list:

        i = i.replace("\n","")
    
        if text.find(i.replace("\n",""))>=0:
            text = text.replace(i,"")
            spam_filter_counter = spam_filter_counter + 1
            
            # full = full + " - " + i
            # print(full)   
    
    return spam_filter_counter, text

spam_quality_counter = 0

def quality_evaluation(text):
    
    full = ""
    spam_quality_counter = 0

    global q_list
    
    for i in q_list:
        if text.find(i.replace("\n",""))>=0:
            spam_quality_counter = spam_quality_counter + 1
            
            # full = full + " - " + i
            # print(full)   
     
    return spam_quality_counter, text

def link_evaluation(url):
    
    hit = 0
    
    global list_compromis
    
    for i in list_compromis:    
        if i.strip() in url.strip():
            hit = hit -5
            #print(hit)                   

    global bad_list
         
    for i in bad_list:
        if i.strip() in url.strip():
            hit = hit - 5  
            #print(hit)             
    
    global good_list

    for i in good_list:  
        if i.strip() in url.strip():
            hit = hit + 5
            #print(hit)                   

    global acceptable_list

    for i in acceptable_list:    
        if i.strip() in url.strip():
            hit = hit + 5 
            #print(hit)                   
        
    return hit

def content_evaluation(text):
    
    score = 25
    
    return score

def finale_verification(url, title, spam_score, quality_score, link_score, content_score):
    
    global data_size

    print("Web-Report  ")
    print("")
    print("title: " + str(title.get_text()))
    print("url: " + str(url))
    print("")  
    print("-------------------")
    print("SPAM             : " + str(spam_score))
    print("LINK             : " + str(link_score))
    print("QUALITY          : " + str(quality_score))
    print("DATA SIZE        : " + str(data_size) + " words in html")
    print("")
    print("SPAM    Ratio %  : " + str(spam_score/data_size))
    print("QUALITY Ratio %  : " + str(quality_score/data_size))
    
    score_alpha = (quality_score * link_score) - spam_score 

    if score_alpha > 0:
        pass_test = "Passed"    
    elif score_alpha == 0:
        pass_test = "uncertain"
    else:
        pass_test = "Failed"

    print("")
    print("CONTENT   : " + str(score_alpha))
    print("GLOBAL Q  : " + pass_test)
    
    if link_score >= 1:
        pass_test = "Safe Site - you can trust this source"
    elif link_score == 0:
        pass_test = "No information about source"
    else:
        pass_test = "Failed unsafe source"
    
    print("SECURITY  : " + pass_test)
    
    result = [spam_score, quality_score, link_score, score_alpha]

    return result

def input_user():
    url = input("Please insert URL: ")
    get_url(url)
    
def main():

    print("Loading...")
    load()
    print("data loaded..\n")
    input_user()

main() 