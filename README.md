# Vertex-Clustering
Implementation of the clustering algorithm in [Vertex](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.453.9494&rep=rep1&type=pdf) described in the section III.a.\
To create the csv file with the ground truth to evaluate the algorithm run:
```
python3 ground_truth_builder.py <path-dataset>
```
For example: 
```
python3 ground_truth_builder.py ./datasets/movieDB
```

To execute the algorithm run:
```
python3 main.py <path-datasets> <directory-dataset>
```
For example: 
```
python3 main.py ./datasets movieDB
```

# Quick start
To test quickly all the functionalities simply run from the root directory: 

	./fast_evaluation.sh

This script will run all the previous described functionalities on the dataset www.study.eu with optimal parameters (estimated with our tests) already embedded.
Obviously if you want to test more in depth, we advice to use the procedure described above, because this script doesn't permit to change any parameter.

# Tests

To run all unit tests, run this command from the root directory:

	python -m unittest
