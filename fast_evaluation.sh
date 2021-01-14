#!/bin/bash

python3 main.py $1 $2 $3 &&
python3 evaluation_metrics.py --clustered prediction.csv --goldstandard golden_set.csv