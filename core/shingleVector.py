class ShingleVector:
    def __init__(self, webpage, content):
        # riferimento alla webpage da cui si è generato lo shingleVector
        # se viene creato un maskedShingleVector si può impostare a None (corretto?)
        self.webpage = webpage
        # vettore (tupla) contenente gli 8 hash minimi della webpage
        self.content = tuple(content)

    def __hash__(self):
        # il content impostato come tupla in ShingleVectorFactory (create_shingle_vector) non converte il tipo
        # è necessario che la chiave usata per il dizionario sia immutabile (convertita in __init__)
        return hash(self.content)

    def __eq__(self, other):
        # confronto effettivo tra le due liste di hash, i riferimenti in Python vengono confrontati con 'is'
        # non vengono confrontate le webpage (stessi vettori hash potrebbero avere diverse webpage associate)
        return (
                self.__class__ == other.__class__ and
                self.content == other.content
        )

    def getWebpage(self):
        return self.webpage

    def setShingle(self, shingle):
        self.shingle = shingle

    def getContent(self):
        return self.content

    def setContent(self, content):
        self.content = content
