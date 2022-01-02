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

fraud           = []
scam            = []
ransomware      = []
porn            = []
phishing        = []
crypto          = []
ads             = []
drugs           = []
piracy         = []
governement     = []
abuse           = []

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

#!/usr/local/bin/python
import configparser
configuration = configparser.ConfigParser()
configuration.read('config.env')
LIMIT_FOR_DATA_FILE = configuration.get('CONFIG','LIMIT_FOR_DATA_FILE')

list_of_lists = []
list_of_category = []

    # url file loading and cleaning process
def load_list(file_name, x_list):

    #print("Starting loading list")
    #print("with file name: " + file_name)
    import time

    print("loading list " + str(file_name))
    memory = []
    counter = 0

    # open file with list of url
    with open(file_name, "r") as file: 
        # reading each line   
        for string in file:    
            # inset in url list object 
            if string not in memory:
                x_list.append(string)
                memory.append(string)
                counter = counter + 1

            if (counter>int(LIMIT_FOR_DATA_FILE)):
                file.close()
                memory = []
                return x_list   
        file.close()
    memory = []

    return x_list

def load():

    global q_list          
    global bad_list        
    global stoplist      
    global spam_list      
    global good_list     
    global list_compromis 
    global acceptable_list

    # More list data
    global fraud
    global scam
    global ransomware
    global porn
    global phishing
    global crypto
    global ads
    global drugs
    global piracy
    global governement
    global abuse

    global list_of_lists
    global list_of_category

    print("This may take some time...")
    # Loading Knowledge List 
    stoplist = load_list("./urls_information/stoplist.filter", stoplist)
    #print("stoplist loaded...")
    
    spam_list = load_list("./urls_information/spam.filter", spam_list)
    #print("spam list loaded...")
    
    q_list = load_list("./urls_information/quality.keywords", q_list)
    #print("quality list loaded...")
    
    list_compromis = load_list("./urls_information/compromised_domains", list_compromis)
    #print("domains loaded...")
    
    bad_list = load_list("./urls_information/bad_domains", bad_list)
    #print("bad domains loaded...")
    
    good_list = load_list("./urls_information/good_domains", good_list)
    #print("good domains loaded...")
    
    acceptable_list = load_list("./urls_information/top_domains_list_acceptable", acceptable_list)  
    
    print("Finishing core keywords and domain loading...")
    print("Lists loaded - thank you")
    print("Starting list loading process...")

    list_of_lists = []
    list_of_category = []

    # INITIAL PROTOTYPE LISTS
    list_container = spam_list
    list_of_category = "SPAM"
    list_of_lists.append(list_container)

    list_container = q_list
    list_of_category = "QUALITY"
    list_of_lists.append(list_container)

    list_container = list_compromis
    list_of_category = "DOMAIN_COMPROMISED"
    list_of_lists.append(list_container)

    list_container = bad_list
    list_of_category = "BAD_DOMAINS"
    list_of_lists.append(list_container)

    list_container = good_list
    list_of_category = "GOOD_DOMAINS"
    list_of_lists.append(list_container)

    list_container = acceptable_list
    list_of_category = "ACCEPTABLE_DOMAINS"
    list_of_lists.append(list_container)

    print("LOADING NEW LIST DATA - The Block List Project")
    print("Please patience...")
    print("We have much data to load please go get a some coffee")
       
    # FOUND - https://github.com/blocklistproject

    import os
    your_path = '/home/linux/Bureau/Programmation/fake-news-1.0/urls_information/'
    files = os.listdir(your_path)
    
    x_list = []
    list_container = []
    list_of_category = []

    for file in files:
        if os.path.isfile(os.path.join(your_path, file)):
            file_name = your_path + file
            x_list = load_list(file_name, x_list)
            list_of_lists.append(x_list) 
            list_of_category.append(str(file)) 
            str(file)
            list_of_lists
            
    return list_of_lists, list_of_category


def get_url_bypass(url, x_list_of_lists, x_list_of_category):
    global list_of_lists
    global list_of_category
    
    list_of_lists = x_list_of_lists
    list_of_category = x_list_of_category
    get_url(url)
    
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

        finale_verification(url, content_score, output)
        
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

def finale_verification(url, content_score, output):
    
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

    print("CONTENT   : " + str(score_alpha))
    print("GLOBAL Q  : " + pass_test)
    
    print_to_file("CONTENT   : " + str(score_alpha))
    print_to_file("GLOBAL Q  : " + pass_test)

    content_check = pass_test
    
    if link_score >= 1:
        pass_test = "Safe Site - you can trust this source"
    elif link_score == 0:
        pass_test = "No information about source"
    else:
        pass_test = "Failed unsafe source"
    
    print("SECURITY  : " + pass_test+"\n")
    print("\n----------------------------------\n\n")
    
    print_to_file("SECURITY  : " + pass_test+"\n")
    print_to_file("\n----------------------------------\n\n")

    security_check = pass_test

    run_data_list(url, content_score, output)

def run_data_list(url, content_score, output):
    
    global list_of_lists
    global list_of_category
    
    counter = 0
    index = 0
        
    for x_list in list_of_lists: 
    
        counter = 0
    
        for i in x_list:
            
            i = i.replace("\n","")
            #print("Looking for: " + i)

            if output.find(i)>=0:
                counter = counter + 1
                #print("keyword text match : " + i)
            if url.find(i)>=0:
                counter = counter + 1
                #print("url domain match : " + i)
        
        if len(list_of_category) > index:
            #print("Hits " + str(counter))
            print("For this list: " + str(list_of_category[index]) + " VALUE: " + str(counter))
            print_to_file("For this list: " + str(list_of_category[index]) + " V00ALUE: " + str(counter))
            counter = 0
            index = index + 1
            
        else:
            counter = 0
            index = index + 1
            
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

def first_call(url):
    
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
    
    list_of_lists, list_of_category = load()
    get_url(url)

    return list_of_lists, list_of_category

def verify_website(url, list_of_lists, list_of_category):
    get_url_bypass(url, list_of_lists, list_of_category)