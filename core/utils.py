#per ora inserisco qui ciò che ancora non mi è chiaro dove mettere

def shingle_cover(shingle_a, shingle_b):
	assert len(shingle_a) == len(shingle_b), "shingle must have same length"
	for i in range(len(shingle_a)):
		with_mask = shingle_b[i] == None or shingle_a[i] == None #None non mi convince molto per modellare "*"
		if shingle_a[i] != shingle_b[i] and not with_mask:
			return False
	return True
