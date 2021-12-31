import time
import urllib.parse
from datetime import datetime
# Python program to AI smart spider project
import time
import requests

import requests as rq 
from _ctypes import Array, Structure, Union
from bs4 import BeautifulSoup as bs
from fake_useragent import UserAgent

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

RELAX_TIME = 0.0000001
memory = []
ua = UserAgent()

stoplist = []
stoplist = load_list("./smart_lists/stoplist", stoplist)

spam_list = []
spam_list = load_list("./smart_lists/spam", spam_list)

q_list = []
q_list = load_list("./smart_lists/quality", q_list)

list_compromis = []
list_compromis = load_list("./smart_lists/compromised_domains", list_compromis)

bad_list = []
bad_list = load_list("./smart_lists/bad_domains", bad_list)

good_list = []
good_list = load_list("./smart_lists/good_domains", good_list)

acceptable_list = []
acceptable_list = load_list("./smart_lists/top_domains_list_acceptable", acceptable_list)

def get_url(url):
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

        spam_score, output = spam_evaluation(str(output))
        #print("SPAM SCORE: " + str(spam_score))

        quality_score, output = quality_evaluation(str(output))
        #print("Q-SCORE: " + str(quality_score))
        
        content_score = content_evaluation(str(output))
        #print("TEXT SCORE: " + str(text_score))
        
        finale_score = finale_verification(spam_score, quality_score, link_score, content_score)
      
    return finale_score

def stop_list(text):
    hit = 0
    global stoplist
    for i in stoplist:
        text = text.replace(i,"") 
    return text

def spam_evaluation(text):
    
    full = ""
    hit = 0
    
    global spam_list

    for i in spam_list:

        i = i.replace("\n","")
    
        if text.find(i.replace("\n",""))>=0:
            text = text.replace(i,"")
            hit = hit + 1
            
            # full = full + " - " + i
            # print(full)   
    
    return hit, text

def quality_evaluation(text):
    
    full = ""
    hit = 0

    global q_list
    
    for i in q_list:
        if text.find(i.replace("\n",""))>=0:
            hit = hit + 1
            
            # full = full + " - " + i
            # print(full)   
     
    return hit, text

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

def finale_verification(spam_score, quality_score, link_score, content_score):
    
    print("Final report\n")
    print("SPAM:    " + str(spam_score))
    print("QUALITY: " + str(quality_score))
    print("LINK:    " + str(link_score))
    
    score_alpha = quality_score * link_score/1.2 - spam_score 

    if score_alpha > 0:
        pass_test = "Passed"    
    elif score_alpha == 0:
        pass_test = "Medium"
    else:
        pass_test = "Failed"

    print("CONTENU: " + str(score_alpha))
    print("TEST A : " + pass_test)
    
    if link_score >= 1:
        pass_test = "Passed"
    else:
        pass_test = "Failed"
    
    print("TEST B : "+ pass_test)
    return 0

url = input("What web site URL do you want to veridy? ")
get_url(url)