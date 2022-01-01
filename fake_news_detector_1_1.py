import time
import urllib.parse
from datetime import datetime
import requests as rq
from _ctypes import Array, Structure, Union
from bs4 import BeautifulSoup as bs
from fake_useragent import UserAgent

RELAX_TIME = 0.0000001
memory = []
ua = UserAgent()

data_size = 0

# Basic Knowledge List 
q_list          = []
bad_list        = []
stoplist        = []
spam_list       = []
good_list       = []
list_compromis  = []
acceptable_list = []

# spam counters
spam_quality_counter = 0
spam_filter_counter = 0
stoplist_filter_counter = 0

# Website info
title = ""
description = ""
data_size = 0
spam_score = 0
quality_score = 0
link_score = 0
content_check = False
security_check = False

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
    stoplist = load_list("./urls_information/stoplist", stoplist)
    print("stoplist loaded...")
    
    spam_list = load_list("./urls_information/spam", spam_list)
    print("spam list loaded...")
    
    q_list = load_list("./urls_information/quality", q_list)
    print("quality list loaded...")
    
    list_compromis = load_list("./urls_information/compromised_domains", list_compromis)
    print("domains loaded...")
    
    bad_list = load_list("./urls_information/bad_domains", bad_list)
    print("bad domains loaded...")
    
    good_list = load_list("./urls_information/good_domains", good_list)
    print("good domains loaded...")
    
    acceptable_list = load_list("./urls_information/top_domains_list_acceptable", acceptable_list)
    
    print("pronlem domains loaded...")
    print("Lists loaded - thank you")

def get_url(url):

    global data_size
    global title
    global description
    global spam_score 
    global quality_score 
    global link_score 

    global content_check
    global security_check 

    page = rq.get(url, headers={'User-Agent': ua.random},timeout=10)
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
        

        data_size = data_size
        title = title
        
        spam_score = spam_score
        quality_score = quality_score
        link_score = link_score

        finale_verification(url, content_score)
        
        # Loop process
        # input_user()

    return finale_score

def stop_list(text):
    global index
    stoplist_filter_counter = 0
    global stoplist
    for i in stoplist:
        text = text.replace(" " + i.replace("\n","") + " ","") 
        spam_filstoplist_filter_counterter_counter = stoplist_filter_counter + 1
    return text

def spam_evaluation(text):
    
    full = ""
    spam_filter_counter = 0
    
    global spam_list

    for i in spam_list:

        i = i.replace("\n","")
    
        if text.find(i.replace("\n",""))>=0:
            text = text.replace(" " + i + " ","")
            spam_filter_counter = spam_filter_counter + 1
            
            # full = full + " - " + i
            # print(full)   
    
    return spam_filter_counter, text

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

def content_evaluation(str):
    list_String = []
    for word in str.split(" "):
        list_String.append(word)
    
    listKeywords= list_String
    listSize = len(listKeywords)
    
    keywordCountList = []
    while listSize > 0:
        targetWord = listKeywords[0]
        count=0

        for i in range(0,listSize):
            if targetWord == listKeywords [i]:
                count = count +1

        wordAndCount = []
        wordAndCount.append(targetWord)
        wordAndCount.append(count)
        
        keywordCountList.append(wordAndCount)

        for i in range (0,count): 
            listKeywords.remove(targetWord) 
        listSize = len(listKeywords)
        
    return keywordCountList


def finale_verification(url, content_score):
    
    global data_size
    global title
    global description
    global spam_score 
    global quality_score 
    global link_score 

    global content_check
    global security_check 
    
    print("\nWeb-Report  ")
    print("")
    print("title: " + str(title.get_text()))
    print("url: " + str(url))
    print("")  
    print("-------------------")
    print("LINK             : " + str(link_score))
    print("SPAM             : " + str(spam_score))
    print("QUALITY          : " + str(quality_score))
    print("DATA SIZE        : " + str(data_size) + " words in html")
    print("")
    print("SPAM    Ratio %  : " + str(spam_score/data_size))
    print("QUALITY Ratio %  : " + str(quality_score/data_size))
    
    print_to_file("\nWeb-Report  ")
    print_to_file("")
    print_to_file("title: " + str(title.get_text()))
    print_to_file("url: " + str(url))
    print_to_file("")  
    print_to_file("-------------------")
    print_to_file("LINK             : " + str(link_score))
    print_to_file("SPAM             : " + str(spam_score))
    print_to_file("QUALITY          : " + str(quality_score))
    print_to_file("DATA SIZE        : " + str(data_size) + " words in html")
    print_to_file("")
    print_to_file("SPAM    Ratio %  : " + str(spam_score/data_size))
    print_to_file("QUALITY Ratio %  : " + str(quality_score/data_size))
    
    score_alpha = (quality_score * link_score) - spam_score 

    spam_score = spam_score
    quality_score = quality_score
    link_score = link_score
    content_score = score_alpha

    if score_alpha > 0:
        pass_test = "Passed"    
    elif score_alpha == 0:
        pass_test = "uncertain"
    else:
        pass_test = "Failed"

    print("")
    print("CONTENT   : " + str(score_alpha))
    print("GLOBAL Q  : " + pass_test)
    
    print_to_file("")
    print_to_file("CONTENT   : " + str(score_alpha))
    print_to_file("GLOBAL Q  : " + pass_test)

    content_check = False
    
    if link_score >= 1:
        pass_test = "Safe Site - you can trust this source"
    elif link_score == 0:
        pass_test = "No information about source"
    else:
        pass_test = "Failed unsafe source"
    
    print("SECURITY  : " + pass_test+"\n")
    print("\n----------------------------------\n\n")

    security_check = pass_test

def input_user():
    url = input("Please insert URL: ")
    get_url(url)
    
def main():
    print("Loading...")
    load()
    print("data loaded..\n")
    input_user()

def print_to_file(data):
    file = open("log.txt","a")
    file.write(data+"\n")

def verify_website(url):

    # Reinitiation
    global data_size
    global title
    global description
    global spam_score 
    global quality_score 
    global link_score 

    global content_check
    global security_check 

    # Website info
    title = ""
    description = ""
    data_size = 0
    spam_score = 0
    quality_score = 0
    link_score = 0
    content_check = False
    security_check = False
    
    load()
    get_url(url)
