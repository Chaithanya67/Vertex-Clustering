class Shingle:
    def __init__(self, webpage, content):
        # riferimento alla pagina web dove si trova lo shingle
        self.webpage = webpage
        # contiene la lista di tag (shingle singolo)
        self.content = content

    def getWebpage(self):
        return self.webpage

    def setWebpage(self, webpage):
        self.webpage = webpage

    def getContent(self):
        return self.content

    def setContent(self, content):
        self.content = content
