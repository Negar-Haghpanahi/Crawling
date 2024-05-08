from InputClass import *
from Crawling import CrawlingPage
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import firefox
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options


class Extract():
    
    def __init__(self , Inputclass : Crawled_Page):
        
        self.objclass = Inputclass
        self.url = Inputclass.URL
        
        
    def extract_html_from_page(self):
        
        # crawl = CrawlingPage(self.objclass)
        # self.objclass = crawl.Driver()
        options = Options()
        options.headless = True  # Set headless mode

        self.objclass.driver = webdriver.Firefox()
        self.objclass.driver.get(self.url)
        

        html_content = self.objclass.driver.page_source
        self.objclass.driver.quit()

        soup = BeautifulSoup(html_content, "html.parser")
        
        # Find the div with id "treetext" and class "BackText line-height-1-8 font-size-large"
        div_element = soup.find("div", id="treeText", class_="BackText line-height-1-8 font-size-large")
        if div_element:
            return str(div_element)
        else:
            return "Div with id 'treetext' and class 'BackText line-height-1-8 font-size-large' not found."

      

     
    
  
