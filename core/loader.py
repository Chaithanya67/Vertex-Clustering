import os
from core.webpage import Webpage

class Loader:
    
    def load_pages(self,path,site):
        pages = []
        path = os.path.join(path,site)
        files = sorted(os.listdir(path))
        for filename in files:
            filename = os.path.join(path,filename)
            webpage = self.load_webpage(filename)
            pages.append(webpage)
        return pages
    
    def load_webpage(self, filename):
        webpage_file = open(filename, "r", encoding="utf-8")
        #NB: questa regola di estrazione del nome va bene per tutti e tre i dataset
        name = filename[(filename.rfind('/')+1):filename.rfind('.')]
        webpage = Webpage(name, webpage_file.read())
        webpage_file.close()
        return webpage