

class WebDriver():
     
    def __init__(self) -> None:
        super().__init__()
        self.URL = ''
        self.driver =''


class Crawled_Page(WebDriver):

    def __init__(self) -> None:
        super().__init__()
        self.Xpath = ''
        self.inner_class_name = ''
        self.href = ''
        self.subURL =[]
        self.name_element = []