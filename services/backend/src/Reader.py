import pdfplumber


class Reader:
    symbols = "#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
    paperContent = None
    text = ""
    def __init__(self, paperFilePath = None):
        if paperFilePath is not None:
            self.paperContent = pdfplumber.open(paperFilePath).pages
        self.filePath = paperFilePath

    def setPaperContent(self, paper):
        self.paperContent = paper

    def displayPaperContent(self,  page_start=0, page_end=5):
        for page in self.paperContent[page_start:page_end]:
            print(page.extract_text())

    def returnPaperContent(self):
        content = ""
        for page in self.paperContent:
            content += self.eliminateSymbols(page.extract_text())
            content += "\n"
        return content

    def eliminateSymbols(self, content):
        return "".join(ch for ch in content if ch.isalnum() or ch.isspace() or ch in self.symbols)
    
    def pages(self):
        return len(self.paperContent)





