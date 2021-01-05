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


def extract_shingle_set(web_page, window_size):
	extractor = TagExtractor()
	extractor.feed(web_page)
	tag_list = extractor.get_tags()
	index = 0
	shingle = []
	while index < (len(tag_list) - (window_size - 1)):
		window_index_end = index + window_size
		window_extracted = tag_list[index:window_index_end]
		shingle.append(window_extracted)
		index += 1

	return shingle

#probabilmente merita di andare in un altro file, forse ShingleVectorFactory
import numpy as np # per uint8, da valutare
import mmh3
from functools import partial

def get_hash_functions(k):
	hash = lambda seed, value: mmh3.hash(value, seed)
	hashes = [ partial(hash, i) for i in range(0,k)] 
	return hashes

def min_hash(shingle_set, hash_function):
	flatten_shingle = lambda shingle: [tag for window in shingle for tag in window]
	shingle_set = flatten_shingle(shingle_set)
	shingle_hashed = list(
		map(
			lambda tag: hash_function(tag) % 256, # da verificare
			shingle_set
		)
	)
	return min(shingle_hashed)

def create_shingle_vector(shingle_set):
	k_hash = get_hash_functions(8)
	shingle_vector = []
	for hash_function in k_hash:
		shingle_byte = min_hash(shingle_set, hash_function)
		shingle_vector.append(shingle_byte)
	return shingle_vector