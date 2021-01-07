class ShingleVector:
    def __init__(self, webpage, content):
        # riferimento alla webpage da cui si è generato lo shingleVector
        self.webpage = webpage
        # vettore contenente gli 8 hash minimi della webpage
        self.content = content

    def getWebpage(self):
        return self.webpage

    def setShingle(self, shingle):
        self.shingle = shingle

    def getContent(self):
        return self.content

    def setContent(self, content):
        self.content = content
