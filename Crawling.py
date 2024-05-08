from InputClass import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class CrawlingPage( ):
    
    def __init__(self , inputClass : Crawled_Page):
        
        self.Myinput = inputClass
        
    def Driver(self):
        
        options = Options()
        options.headless = True 

        self.Myinput.driver = webdriver.Chrome(options=options)
        self.Myinput.driver.get(self.Myinput.URL)
        
        return self.Myinput
        


