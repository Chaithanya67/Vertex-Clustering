example_page = "<html><head></head><body><p><div></div></p></body></html>"

window_size = 2

from html.parser import HTMLParser

class TagExtractor(HTMLParser):
	def __init__(self):
		super().__init__()
		self.__tags = []

	def handle_starttag(self, tag, attrs):
		self.__tags.append(tag)

	def handle_endtag(self, tag):
		self.__tags.append(tag)

	def handle_data(self, data):
		pass 

	def get_tags(self):
		return self.__tags


def extract_shingle_set(web_page):
	extractor = TagExtractor()
	extractor.feed(web_page)
	tag_list = extractor.get_tags()
	index = 0
	shingle = []
	while index < (len(tag_list) - window_size):
		shingle.append(tag_list[index:(index+window_size)])
		index += 1

	return shingle

print(extract_shingle_set(example_page))