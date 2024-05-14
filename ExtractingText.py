from InputClass import *
from Crawling import CrawlingPage
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import firefox
from selenium.webdriver import Firefox



class Extract():
    
    def __init__(self , Inputclass : Crawled_Page):
        
        self.objclass = Inputclass
        self.url = Inputclass.URL
        # crawl = CrawlingPage(self.objclass)
        # self.objclass = crawl.Driver()
        options = Options()
        options.headless = True  # Set headless mode

        self.objclass.driver = webdriver.Firefox()
        self.objclass.driver.get(self.url)
            

        html_content = self.objclass.driver.page_source
        self.objclass.driver.quit()

        self.soup = BeautifulSoup(html_content, "html.parser")

    def extract_Header(self):

        div_element = self.soup.find("div", class_="col-md-11")
        if div_element:
                return str(div_element)
        else:
                return "Div is not found."
        

    def extract_Body(self):

        div_element = self.soup.find("div", id="treeText", class_="BackText line-height-1-8 font-size-large")
        # div_element = soup.find("div", id="treeText", class_="BackText line-height-1-8 font-size-large")
        div_element = soup.find_all("div", class_="col-md-11")
        if div_element:
            return str(div_element)
        else:
            return "Div is not found."
        
    
  












# from InputClass import *
# from Crawling import CrawlingPage
# from selenium import webdriver
# from bs4 import BeautifulSoup
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver import firefox
# from selenium.webdriver import Firefox



# class Extract():
    
#     def __init__(self , Inputclass : Crawled_Page):
        
#         self.objclass = Inputclass
#         self.url = Inputclass.URL
        
        
#     def extract_html_from_page(self):
        
#         # crawl = CrawlingPage(self.objclass)
#         # self.objclass = crawl.Driver()
#         options = Options()
#         options.headless = True  # Set headless mode

#         self.objclass.driver = webdriver.Firefox()
#         self.objclass.driver.get(self.url)
            

#         html_content = self.objclass.driver.page_source
#         self.objclass.driver.quit()

#         soup = BeautifulSoup(html_content, "html.parser")
        
#         # div_element = soup.find("div", id="treeText", class_="BackText line-height-1-8 font-size-large")
#         div_element = soup.find_all("div", class_="col-md-11")

#         if div_element:
#             return str(div_element)
#         else:
#             return "Div is not found."
        
    
  
