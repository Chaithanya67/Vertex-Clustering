from core.ShingleExtractor import extract_shingle_set
from core.ShingleVectorFactory import create_shingle_vector
from core.utils import k_shingle_cover

class Algoritmo:
    
    def passo1(self, pages):
        
        hash_table = {}
        for page in pages:
            shingle_set = extract_shingle_set(page, 8) 
            shingle_vector = create_shingle_vector(shingle_set)
            masked_shingle_vectors = k_shingle_cover(shingle_vector, 6)
            for masked_shingle_vector in masked_shingle_vectors:
                #Ecco la bruttura
                if (masked_shingle_vector.getContent() in hash_table):
                    hash_table[masked_shingle_vector.getContent()] = hash_table.get(masked_shingle_vector.getContent()) + 1
                else:
                    hash_table[masked_shingle_vector.getContent()] = 1
        
        return hash_table
    
    