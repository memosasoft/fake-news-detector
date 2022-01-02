import time
import urllib.parse

def start_test():

    list_of_lists = []
    list_of_category = []
    
    import fake_news_detector_1_2 as interface_fake
    
    url = "https://sectigostore.com/ssl-types"
    list_of_lists, list_of_category = interface_fake.first_call(url)

    url = "https://sectigostore.com/website-security"
    interface_fake.verify_website(url, list_of_lists, list_of_category)

    url = "https://transparencyreport.google.com/safe-browsing/search"
    interface_fake.verify_website(url, list_of_lists, list_of_category)
    
    url = "https://www.bbb.org/scamtracker/us/"
    interface_fake.verify_website(url, list_of_lists, list_of_category)
    
    url = "http://code.google.com/"
    interface_fake.verify_website(url, list_of_lists, list_of_category)
    
    url = "https://cse.google.com/"
    interface_fake.verify_website(url, list_of_lists, list_of_category)
    
    url = "https://help.yahoo.com/"
    interface_fake.verify_website(url, list_of_lists, list_of_category)
    
    url = "https://oag.ca.gov/"
    interface_fake.verify_website(url, list_of_lists, list_of_category)
    
    url = "https://sectigostore.com/"
    interface_fake.verify_website(url, list_of_lists, list_of_category)
    
    url = "https://www.canada.ca/"
    interface_fake.verify_website(url, list_of_lists, list_of_category)
    
    url = "https://www.cbc.ca/"
    interface_fake.verify_website(url, list_of_lists, list_of_category)
    
    url = "https://www.cnbc.com/"
    interface_fake.verify_website(url, list_of_lists, list_of_category)
    
    url = "https://www.consumer.ftc.gov/"
    interface_fake.verify_website(url, list_of_lists, list_of_category)
    
    url = "https://www.docusign.com/"
    interface_fake.verify_website(url, list_of_lists, list_of_category)
    
    url = "https://www.google.com/"
    interface_fake.verify_website(url, list_of_lists, list_of_category)
    
    url = "https://www.investopedia.com/"
    interface_fake.verify_website(url, list_of_lists, list_of_category)

    url = "https://www.wikihow.com/"
    interface_fake.verify_website(url, list_of_lists, list_of_category)

    url = "http://opensource.org/"
    interface_fake.verify_website(url, list_of_lists, list_of_category)

    url = "https://bitcoin.org/"
    interface_fake.verify_website(url, list_of_lists, list_of_category)

    url = "https://developer.bitcoin.org/"
    interface_fake.verify_website(url, list_of_lists, list_of_category)

    url = "https://play.google.com/"
    interface_fake.verify_website(url, list_of_lists, list_of_category)

    url = "https://stackoverflow.com/"
    interface_fake.verify_website(url, list_of_lists, list_of_category)

    url = "https://twitter.com/"
    interface_fake.verify_website(url, list_of_lists, list_of_category)

    url = "https://www.facebook.com/"
    interface_fake.verify_website(url, list_of_lists, list_of_category)

    url = "https://www.instagram.com/"
    interface_fake.verify_website(url, list_of_lists, list_of_category)

    url = "https://www.linkedin.com/"
    interface_fake.verify_website(url, list_of_lists, list_of_category)

    url = "https://www.programiz.com/"
    interface_fake.verify_website(url, list_of_lists, list_of_category)

    url = "https://www.youtube.com/"
    interface_fake.verify_website(url, list_of_lists, list_of_category)


def main():
    start_test()

main()