import sys
from core.ShingleExtractor import extract_shingle_set
from core.ShingleVectorFactory import create_shingle_vector
from core.loader import Loader
from core.utils import k_shingle_cover


if len(sys.argv) < 3:
	print("usage: main.py <datasets-folder> <dataset>")
	exit()

dataset_folder = sys.argv[1]
dataset = sys.argv[2]
loader = Loader()
pages = loader.load_pages(dataset_folder, dataset)


hash_table = {}

## PASSO 1 v.0.1
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

print(hash_table)
         
        
        
## TODO: find 8/8 masked_shingle_vector o salvate all'inizio
## TODO: maximum count covering 
## TODO: decrement counts in H
## TODO: create maskedShingleVector as a ShingleVector object (k_shingle_cover)
    
webpage = pages[0]
shingle_set = extract_shingle_set(webpage, 10)
shingle_vector = create_shingle_vector(shingle_set)
for elem in tuple(k_shingle_cover(shingle_vector, 7)):
    print(elem.getContent())
print('Contenuto (hash) shingle_vector: ' + str(shingle_vector.getContent()))
print('Nome (webpage) shingle_vector: ' + shingle_vector.getWebpage().getName())
