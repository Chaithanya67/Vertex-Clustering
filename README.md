# Vertex-Clustering
Implementazione dell'algoritmo di clustering di [Vertex](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.453.9494&rep=rep1&type=pdf) descritto nella sezione III.a.\
Per creare il csv con la ground truth per valutare l'algoritmo lanciare il comando:
```
python3 ground_truth_builder.py <path-dataset>
```
Ad esempio: 
```
python3 ground_truth_builder.py ./datasets/movieDB
```

Poi eseguire l'algoritmo e creare il csv con le predizioni usare il comando:
```
python3 main.py <path-datasets> <directory-dataset>
```
Ad esempio: 
```
python3 main.py ./datasets movieDB
```

Infine per avere i risultati delle metriche eseguire il comando:
```
python3 evaluation_metrics.py --clustered ./prediction.csv --goldstandard ./ground_truth.csv
```

# Avvio rapido

Per testare in maniera veloce il funzionamento del metodo, si può utilizzare: 

	./fast_evaluation

Tale script è già impostate per effettuare tutti i passi precedenti sul dataset www.study.eu con i parametri ottimali stimati dai nostri test.
Ovviamente per fare test più approfonditi si consiglia la procedura riportata sopra, visto che tale script non permette modifiche ai parametri.

# Test

per eseguire tutti i test, usare nella cartella root del progetto il comando:

	python -m unittest
