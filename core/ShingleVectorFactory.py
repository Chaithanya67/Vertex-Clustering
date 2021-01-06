import numpy as np # per uint8, da valutare
import mmh3
from functools import partial
from core.shingleVector import ShingleVector

def get_hash_functions(k):
	hash = lambda seed, value: mmh3.hash(value, seed)
	hashes = [ partial(hash, i) for i in range(0,k)] 
	return hashes

def min_hash(shingle_set, hash_function):
	flatten_shingle = lambda shingles: [tag for shingle in shingles for window in shingle.getContent() for tag in window]
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
	return ShingleVector(shingle_set[0].getName(),shingle_vector)