import sys
import os
from core.utils import Logger
from evaluation_metrics import precision_recall

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
else:
	input_size = None

#singleton initialization
logger = Logger(verbosity)

vertex.clustering(dataset_folder, dataset, 10, 1024, 26, input_size)

ground_truth_path = os.path.join(dataset_folder, dataset + "_ground_truth.csv")
precision, recall, f1 = precision_recall("prediction.csv", ground_truth_path)
print("Precision: ", precision)
print("Recall: ", recall)
print("F1: ", f1)