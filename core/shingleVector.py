


class ShingleVector:
    
    
	def __init__(self, clusterName, content):
		self.name = clusterName
		self.content = content

	def getName(self):
		return self.name

	def setName(self, clusterName):
		self.name = clusterName
        
	def getContent(self):
		return self.content

	def setContent(self, content):
		self.content = content