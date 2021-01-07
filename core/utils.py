#per ora inserisco qui ciò che ancora non mi è chiaro dove mettere

def shingle_cover(shingle_vector_a, shingle_vector_b):
	assert len(shingle_vector_a) == len(shingle_vector_b), "shingle must have same length"
	for i in range(len(shingle_vector_a)):
		with_mask = shingle_vector_b[i] == None or shingle_vector_a[i] == None #None non mi convince molto per modellare "*"
		if shingle_vector_a[i] != shingle_vector_b[i] and not with_mask:
			return False
	return True


#Crea tutti i masked_shingle_vector 6/8, 7/8, 8/8 di uno shingle_vector
def k_shingle_cover(shingle_vector_content, k):
    masked_shingle_vectors =[]
    if(k<6):
        raise Exception("Minimum k for k_shingle_cover is 6")
    if(k == 6):
        #6/8
        masked_shingle_vectors.extend(shingle_cover_only_6(shingle_vector_content))
        #7/8
        masked_shingle_vectors.extend(shingle_cover_only_7(shingle_vector_content))
        #8/8
        masked_shingle_vectors.append(shingle_vector_content)
        
    if(k == 7):
        #7/8
        masked_shingle_vectors.extend(shingle_cover_only_7(shingle_vector_content))
        #8/8
        masked_shingle_vectors.append(shingle_vector_content)
    if (k == 8):
        #8/8
        masked_shingle_vectors.append(shingle_vector_content)           
            
    return masked_shingle_vectors

def shingle_cover_only_6(shingle_vector_content):
    length = len(shingle_vector_content)
    masked_shingle_vectors =[]
    for i in range(length):
        temp = []
        temp.extend(shingle_vector_content)
        temp[i] = None
        for j in range(i+1,length):
            masked_shingle_vector = []
            masked_shingle_vector.extend(temp)
            masked_shingle_vector[j] = None
            masked_shingle_vectors.append(masked_shingle_vector)
    return masked_shingle_vectors

def shingle_cover_only_7(shingle_vector_content):
    length = len(shingle_vector_content)
    masked_shingle_vectors =[]
    for i in range(length):
        masked_shingle_vector = []
        masked_shingle_vector.extend(shingle_vector_content)
        masked_shingle_vector[i] = None
        masked_shingle_vectors.append(masked_shingle_vector)
    return masked_shingle_vectors
