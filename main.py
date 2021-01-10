import sys
from core.loader import Loader
from core.algoritmo import Algoritmo

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


## PASSO 1 v.0.1
hash_table = {}
algoritmo = Algoritmo()
hash_table = algoritmo.passo1(pages)

print('\n\n\n############### FINE PASSO 1 ####################\n')
print(hash_table)

## PASSO 2 v.0.1
hash_table = algoritmo.passo2(hash_table, 26)


## TODO: testing passo1
## TODO: testing passo2
## TODO: testing passo3
## TODO: da rivedere bene come fare gli hash che per ora sono fortemente dipendenti dal modulo che scegliamo, anche alla luce dei risultati che raggiungiamo

print('\n\n\n############### FINE PASSO 2 ####################\n')  
print(hash_table)

## PASSO 3 v.0.1
cluster ={}
cluster = algoritmo.passo3(hash_table, pages)

print('\n\n\n################ FINE PASSO 3 ####################\n')
print('Numero cluster ' + str(len(cluster)))
print('\nClusters: \n')
print(cluster)

file = open("prediction.csv", "w")
index_cluster = 0
for key in cluster:
    print("\ncluster\n")
    for page in cluster[key]:
        file.write(page.name + ", " + str(index_cluster) + "\n")
    index_cluster += 1

file.close()
        
    
