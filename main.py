import sys
from core.ShingleExtractor import extract_shingle_set
from core.ShingleVectorFactory import create_shingle_vector
from core.loader import Loader
from core.utils import k_shingle_cover
from core.algoritmo import Algoritmo
from core.utils import find_8_masked_shingle_vectors_sorted
from core.utils import maximum_count_covering
from core.utils import shingle_cover

if len(sys.argv) < 3:
	print("usage: main.py <datasets-folder> <dataset>")
	exit()


dataset_folder = sys.argv[1]
dataset = sys.argv[2]
loader = Loader()
pages = loader.load_pages(dataset_folder, dataset)

if len(sys.argv) > 3:
    input_size = int(sys.argv[3])
    pages = pages[:input_size]

hash_table = {}

## PASSO 1 v.0.1
algoritmo = Algoritmo()
hash_table = algoritmo.passo1(pages)


## PASSO 2 v.0.1 ## TO-BE-CONTINUED: per ora azzera tutti i conteggi, domattina mi ci metto e guardo dove ho sbagliato XD

for v in find_8_masked_shingle_vectors_sorted(hash_table):
    v_primo = maximum_count_covering(hash_table, v)
    #Decrementa del contteggio di v tutti quelli che coprono v ma non sono v' stesso
    for masked_shingle_vector in hash_table.keys():
        if(shingle_cover(masked_shingle_vector, v) and (masked_shingle_vector != v_primo)):
            hash_table[masked_shingle_vector] = hash_table[masked_shingle_vector] - hash_table[v]

# Buttata a caso la soglia per ora
threshold = 0
key_to_delete = []
for key in hash_table.keys():
    if(hash_table[key] < threshold):
        key_to_delete.append(key)
for key in key_to_delete:
    hash_table.pop(key)

#############################FINE PASSO 2 ######################################
    
print(hash_table)

    
         
        
 
## TODO: testing passo1
## TODO: testing passo2
    
webpage = pages[0]
shingle_set = extract_shingle_set(webpage, 10)
shingle_vector = create_shingle_vector(shingle_set)
for elem in tuple(k_shingle_cover(shingle_vector, 7)):
    print(elem.getContent())
print('Contenuto (hash) shingle_vector: ' + str(shingle_vector.getContent()))
print('Nome (webpage) shingle_vector: ' + shingle_vector.getWebpage().getName())
