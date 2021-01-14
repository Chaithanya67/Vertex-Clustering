from core.algoritmo import Algoritmo
from core.loader import Loader
from core.utils import Logger


def clustering(dataset_folder, dataset, window_size=10, hash_module=1024, threshold=26, input_limit=None):
	loader = Loader()
	pages = loader.load_pages(dataset_folder, dataset)
	pages = pages[:input_limit]

	logger = Logger.get_instance()
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
	cluster = algoritmo.passo3(hash_table, pages, hash_module, window_size)

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