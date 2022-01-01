import time
import urllib.parse

def start_test():
    import fake_news_detector_1_1 as interface_fake
    
    url = "https://sectigostore.com/ssl-types"
    interface_fake.verify_website(url)

    url = "https://sectigostore.com/website-security"
    interface_fake.verify_website(url)

    url = "https://transparencyreport.google.com/safe-browsing/search"
    interface_fake.verify_website(url)
    
    url = "https://www.bbb.org/scamtracker/us/"
    interface_fake.verify_website(url)
    
    url = "http://code.google.com/"
    interface_fake.verify_website(url)
    
    url = "https://cse.google.com/"
    interface_fake.verify_website(url)
    
    url = "https://help.yahoo.com/"
    interface_fake.verify_website(url)
    
    url = "https://oag.ca.gov/"
    interface_fake.verify_website(url)
    
    url = "https://sectigostore.com/"
    interface_fake.verify_website(url)
    
    url = "https://www.canada.ca/"
    interface_fake.verify_website(url)
    
    url = "https://www.cbc.ca/"
    interface_fake.verify_website(url)
    
    url = "https://www.cnbc.com/"
    interface_fake.verify_website(url)
    
    url = "https://www.consumer.ftc.gov/"
    interface_fake.verify_website(url)
    
    url = "https://www.docusign.com/"
    interface_fake.verify_website(url)
    
    url = "https://www.google.com/"
    interface_fake.verify_website(url)
    
    url = "https://www.investopedia.com/"
    interface_fake.verify_website(url)
    
    url = "https://www.wikihow.com/"
    interface_fake.verify_website(url)
    
def main():
    start_test()

main()