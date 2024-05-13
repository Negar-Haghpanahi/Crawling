from InputClass import *
from ExtractingText import Extract 
from bs4 import BeautifulSoup
 
 
class MarkdownText():
    
    def __init__(self , inputclass : Crawled_Page):
        
        self.markdownObj =  inputclass 
        self.markdown_output = ""
        
    
    def make_Markdown(self):
        textObj = Extract(self.markdownObj)
        html_content = textObj.extract_html_from_page()
        
        # Parse HTML content
        soup = BeautifulSoup(html_content, "html.parser")
        
        # Convert <h1> tags to Markdown headings
        markdown_text = soup.get_text(separator="\n")
        # Find <h1> tag with specific class
        h1_tag = soup.find("h1", class_="Title3D")
        
        # Extract text content from <span> inside <h1>
        if h1_tag:
            title_text = h1_tag.get_text(strip=True)
            markdown_text += f"\n\n## {title_text}\n\n"
        
        for h1_tag in soup.find_all("h1"):
            h1_tag.string = f"# {h1_tag.string}\n\n"

        # Convert <br> tags to Markdown line breaks
        for br_tag in soup.find_all("br"):
            br_tag.replace_with("\n\n")

        for h1_b in  soup.find_all("b", text="پیام:"):
            h1_b.string = f"## {h1_b.string}\n\n"
     
        # Remove any remaining HTML tags
        
        
        # Find elements with specified style attribute

      

        self.markdown_output += markdown_text + "\n\n" 
        return self.markdown_output
            
    def Save_Markdown(self, text):
        with open("output.md", "w", encoding="utf-8") as file:
            file.write(text)
