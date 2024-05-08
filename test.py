from selenium import webdriver
from selenium.webdriver.common.by import By
import os

# Start a Selenium webdriver
# driver = webdriver.Chrome()
driver = webdriver.Chrome(executable_path=os.path.abspath("C:\Program Files\chromedriver.exe"))
# Open the webpage
driver.get("https://ara.jri.ac.ir/")

# Find all div elements with the specified class name
div_elements = driver.find_elements(By.CLASS_NAME, "col-md-4.col-sm-6")

# Markdown output
markdown_output = ""
for div_element in div_elements:
    # Find all links within the div using XPath
    links = div_element.find_elements(By.XPATH, ".//a[@href]")  # Update XPath as per your HTML structure
    
    # Loop through each link within the div
    for link in links:
        # Get link text and URL
        link_text = link.text
        link_url = link.get_attribute("href")
        
        # Format as Markdown
        markdown_output += f"[{link_text}]({link_url})\n"

# Print or save Markdown output
print(markdown_output)

# Close the webdriver
driver.close()
driver.quit()
