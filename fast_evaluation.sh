#!/bin/bash

python3 main.py datasets study 1 &&
python3 evaluation_metrics.py --clustered prediction.csv --goldstandard datasets/study_ground_truth.csv