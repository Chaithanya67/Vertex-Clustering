import sys
from core.ShingleExtractor import extract_shingle_set
from core.ShingleVectorFactory import create_shingle_vector
from core.loader import Loader


if len(sys.argv) < 2:
	print("usage: page-clustering <dataset-folder>")
	exit()

dataset_folder = sys.argv[1]
loader = Loader()
pages = loader.load_pages(dataset_folder, 'study')


webpage = pages[0]
shingle_set = extract_shingle_set(webpage, 8)
shingle_vector = create_shingle_vector(shingle_set)
print('Contenuto shingle_vector: ' + str(shingle_vector.getContent()))
print('Nome shingle_vector: ' + shingle_vector.getShingle().getWebpage().getName())