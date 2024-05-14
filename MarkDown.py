from InputClass import *
from ExtractingText import Extract 
from bs4 import BeautifulSoup
 
 
class MarkdownText():
    
    def __init__(self , inputclass : Crawled_Page):
        
        self.markdownObj =  inputclass 
        self.markdown_output = ""
        
    
    def make_Markdown(self):
        textObj = Extract(self.markdownObj)
        markdown_text = ''

        html_content = textObj.extract_Header()
        soup = BeautifulSoup(html_content, "html.parser")

        for col_md_11_tag in soup.find_all(class_="col-md-11"):

            text_with_spaces = col_md_11_tag.get_text("\n", strip=True)

            # Check if the extracted text contains <h1> tag
            if "<h1>" in str(col_md_11_tag):
                # Convert to Markdown heading
                text_with_spaces = "# " + text_with_spaces
            # Check if the extracted text contains <b> tag
            elif "<b>" in str(col_md_11_tag):
                # Convert to Markdown heading level 2
                text_with_spaces = "## " + text_with_spaces



            markdown_text += text_with_spaces + "\n\n"

        html_content = textObj.extract_Body()
        
        # Parse HTML content
        soup = BeautifulSoup(html_content, "html.parser")
        #header part

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
            # print("h1 tag is :" , h1_tag.string)
        
        # Convert <br> tags to Markdown line breaks
        for br_tag in soup.find_all("br"):
            br_tag.replace_with("\n\n")
            # print("b1 tag is :" ,br_tag.string)
        
        # Remove any remaining HTML tags\

        for div in soup.find_all("div", class_="dropdown font-weight-bold position-absolute top-50px"):
            div.extract()  # Remove the div from the soup
        
        markdown_text += soup.get_text(separator="\n")
        
        
        # Find elements with specified style attribute

      

        self.markdown_output += markdown_text + "\n\n" 
        return self.markdown_output



    def Save_Markdown(self, text):
        with open("output.md", "w", encoding="utf-8") as file:
            file.write(text)






# from InputClass import *
# from ExtractingText import Extract 
# from bs4 import BeautifulSoup
 
 
# class MarkdownText():
    
#     def __init__(self , inputclass : Crawled_Page):
        
#         self.markdownObj =  inputclass 
#         self.markdown_output = ""
        
#     def skip_element(self, element):
#         # Skip <div> elements with class 'tab16'
#         if element.name == 'div' and 'tab16' in element.get('class', []):
#             return False

#         if element.name == 'div' and  'col-md-9 col-md-offset-1 BackText text-align-right  background-color-whitesmoke margin-top-50px' in element.get('class', []):
#             return False
#         if element.name == 'tbody' and element.find_parent('table', class_='width-100'):
#             return False

#         return True


#     def make_Markdown(self):
#         textObj = Extract(self.markdownObj)
#         html_content = textObj.extract_html_from_page()
        
#         # Parse HTML content
#         soup = BeautifulSoup(html_content, "html.parser")
        
#         # Convert <h1> tags to Markdown headings
#         markdown_text = soup.get_text(separator="\n")
#         # Find <h1> tag with specific class
#         h1_tag = soup.find("h1", class_="Title3D")
        
#         # Extract text content from <span> inside <h1>
#         if h1_tag:
#             title_text = h1_tag.get_text(strip=True)
#             markdown_text += f"\n\n# {title_text}\n\n"
        
#         # for h1_tag in soup.find_all("h1"):
#         #     h1_tag.string = f"# {h1_tag.string}\n\n"

#         # Convert <br> tags to Markdown line breaks
#         for br_tag in soup.find_all("br"):
#             br_tag.replace_with("\n\n")

#         for h1_b in  soup.find_all("b", text="پیام:"):
#             h1_b.string = f"## {h1_b.string}\n\n"
     
#         # Remove any remaining HTML tags
#         markdown_text = ""
#         for element in soup.find_all(self.skip_element):
#             markdown_text += element.get_text(separator="\n") + "\n"

#         self.markdown_output = markdown_text + "\n\n" 
#         return self.markdown_output


#     def Save_Markdown(self, text):
#         with open("output.md", "w", encoding="utf-8") as file:
#             file.write(text)
