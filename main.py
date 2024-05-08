from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import firefox
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options


from Crawling import *
from InputClass import *
from MarkDown import *



def Crawling(inputclass : Crawled_Page):
    
    # inputclass= CrawlingPage(inputclass)
    # inputclass = inputclass.driver()
    options = Options()
    options.headless = True  # Set headless mode

    inputclass.driver = webdriver.Firefox()
 

    inputclass.driver.get(inputclass.URL)
    div_elements = inputclass.driver.find_elements(By.CLASS_NAME, inputclass.inner_class_name)


    for div_element in div_elements:
    
        links = div_element.find_elements(By.XPATH, inputclass.Xpath ) 
        for link in links:
        
            # print("Link Text:", link.text)
            # print("Link URL:", link.get_attribute("href")) 
            inputclass.subURL.append(link.get_attribute("href"))
            
    inputclass.driver.quit()
    
    return inputclass


if __name__ == '__main__':
    
    text = ""
    Crawl_class = Crawled_Page()
    Crawl_class.URL = "https://ara.jri.ac.ir/"
    Crawl_class.inner_class_name = "col-md-4.col-sm-6"
    Crawl_class.Xpath = ".//a[@href]"
    Crawl_class = Crawling(Crawl_class)
    count =0
    
    for sub_url in Crawl_class.subURL:

        if count < 2:   
            Crawl_class.URL = sub_url
            outputObj = MarkdownText(Crawl_class)
            
            text = text + outputObj.make_Markdown() 
            count = count + 1
                
        outputObj.Save_Markdown(text)
            
        
        


    