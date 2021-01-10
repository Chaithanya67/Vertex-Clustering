import sys
import os
from core.utils import Logger


import vertex

if len(sys.argv) < 3:
	print("usage: main.py <datasets-folder> <dataset> <verbosity> <input-size>")
	exit()


dataset_folder = sys.argv[1]
dataset = sys.argv[2]


verbosity = 0
if len(sys.argv) > 3:
	verbosity = int(sys.argv[3])

if len(sys.argv) > 4:
    input_size = int(sys.argv[4])
    pages = pages[:input_size]

#singleton initialization
Logger(verbosity)
    
vertex.clustering(dataset_folder, dataset, 10, 512, 0)