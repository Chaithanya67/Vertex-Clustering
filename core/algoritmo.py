from core.ShingleExtractor import extract_shingle_set
from core.ShingleVectorFactory import create_shingle_vector
from core.utils import k_shingle_cover
from core.utils import find_8_masked_shingle_vectors_sorted
from core.utils import maximum_count_covering
from core.utils import shingle_cover
from core.utils import Logger

class Algoritmo:
    
    def passo1(self, pages, window_size=10, hash_module=256):
        logger = Logger.get_instance()
        hash_table = {}
        for page in pages:
            logger.print("Processing page: " + page.name, 2)
            shingle_set = extract_shingle_set(page, window_size) 
            shingle_vector = create_shingle_vector(shingle_set, hash_module)
            masked_shingle_vectors = k_shingle_cover(shingle_vector, 6)
            for masked_shingle_vector in masked_shingle_vectors:
                #Ecco la bruttura
                if (masked_shingle_vector.getContent() in hash_table):
                    hash_table[masked_shingle_vector.getContent()] = hash_table.get(masked_shingle_vector.getContent()) + 1
                else:
                    hash_table[masked_shingle_vector.getContent()] = 1
        
        return hash_table
    
    def passo2(self, hash_table, threshold):
        
        for v in find_8_masked_shingle_vectors_sorted(hash_table):
            v_primo = maximum_count_covering(hash_table, v)
            #Decrementa del contteggio di v tutti quelli che coprono v ma non sono v' stesso
            for masked_shingle_vector in hash_table.keys():
                if(shingle_cover(masked_shingle_vector, v) and (masked_shingle_vector != v_primo)):
                    hash_table[masked_shingle_vector] = hash_table[masked_shingle_vector] - hash_table[v]

        # Buttata a caso la soglia per ora
        key_to_delete = []
        for key in hash_table.keys():
            if(hash_table[key] < threshold):
                key_to_delete.append(key)
        for key in key_to_delete:
            hash_table.pop(key)
        
        return hash_table
    
    def passo3(self, hash_table, pages, hash_module, window_size):
        cluster ={}
        for v in hash_table.keys():
            cluster[v] = []
        for page in pages:
            shingle_set = extract_shingle_set(page, window_size) 
            v = create_shingle_vector(shingle_set, hash_module)
            v_primo = maximum_count_covering(hash_table, v.getContent())
            if(v_primo != None):
                cluster[v_primo].append(page)
        
        return cluster


    
    
