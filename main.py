import sys
import os
from core.loader import Loader
from core.algoritmo import Algoritmo
from core.utils import Logger

if len(sys.argv) < 3:
	print("usage: main.py <datasets-folder> <dataset> <verbosity> <input-size>")
	exit()


dataset_folder = sys.argv[1]
dataset = sys.argv[2]
loader = Loader()
pages = loader.load_pages(dataset_folder, dataset)

verbosity = 0
if len(sys.argv) > 3:
	verbosity = int(sys.argv[3])

if len(sys.argv) > 4:
    input_size = int(sys.argv[4])
    pages = pages[:input_size]

def vertex_clustering(dataset, window_size=10, hash_module=256, threshold=1, verbosity=0, input_limit=None):
	#singleton initialization
	logger = Logger(verbosity)
	logger.print('\n\n\n############### INIZIO PASSO 1 ####################\n', 1)
	hash_table = {}
	algoritmo = Algoritmo()
	hash_table = algoritmo.passo1(pages, window_size, hash_module)

	Logger.print('\n\n\n############### FINE PASSO 1 ####################\n', 1)
	logger.print(hash_table, 3)

	logger.print('\n\n\n############### INIZIO PASSO 2 ####################\n', 1)
	hash_table = algoritmo.passo2(hash_table, threshold)


	## TODO: testing passo1
	## TODO: testing passo2
	## TODO: testing passo3
	## TODO: da rivedere bene come fare gli hash che per ora sono fortemente dipendenti dal modulo che scegliamo, anche alla luce dei risultati che raggiungiamo

	logger.print('\n\n\n############### FINE PASSO 2 ####################\n', 1)  
	logger.print(hash_table, 3)

	logger.print('\n\n\n############### INIZIO PASSO 3 ####################\n', 1)
	cluster ={}
	cluster = algoritmo.passo3(hash_table, pages)

	logger.print('\n\n\n################ FINE PASSO 3 ####################\n', 1)
	logger.print('Numero cluster ' + str(len(cluster)), 2)
	logger.print('\nClusters: \n', 2)
	logger.print(cluster, 2)

	file = open("prediction.csv", "w")
	index_cluster = 0
	for key in cluster:
	    logger.print("\ncluster\n", 3)
	    for page in cluster[key]:
	        file.write(page.name + ", " + str(index_cluster) + "\n")
	    index_cluster += 1

	file.close()
	        
    
vertex_clustering(os.path.join(dataset_folder, dataset), 10, 512, 0, verbosity=verbosity)