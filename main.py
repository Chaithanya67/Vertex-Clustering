import sys
from core.ShingleExtractor import extract_shingle_set
from core.ShingleVectorFactory import create_shingle_vector
from core.loader import Loader


if len(sys.argv) < 3:
	print("usage: main.py <datasets-folder> <dataset>")
	exit()

dataset_folder = sys.argv[1]
dataset = sys.argv[2]
loader = Loader()
pages = loader.load_pages(dataset_folder, dataset)


hash_table = {}


#for page in pages:
#     shingle_set = extract_shingle_set(page, 8) 
#     shingle_vector = create_shingle_vector(shingle_set)
#     masked_shingle_vectors = []
        
        
        
        
    
webpage = pages[0]
shingle_set = extract_shingle_set(webpage, 8)
shingle_vector = create_shingle_vector(shingle_set)
print('Contenuto shingle_vector: ' + str(shingle_vector.getContent()))
print('Nome shingle_vector: ' + shingle_vector.getShingle().getWebpage().getName())
